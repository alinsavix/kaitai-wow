# right now, this is just going to be for wrangling the WoW listfile, but
# we're going to make it a bit more general so that later on we can, well,
# make it more general. Doesn't even really cache CSV files at the moment,
# just the almost-CSV that is the standard WoW tooling listfile
import csv
import logging
import sqlite3
import time
from pathlib import Path
from typing import Dict, Optional, Union, cast

from ppretty import ppretty


# Pass None as file to disable cache
# FIXME: wrong pattern for that?
class ListfileCache(object):
    name: str
    nocache: bool
    listfile: Optional[Path]
    cachefile: Path
    db: sqlite3.Connection

    # FIXME: should much of this be in a separate function?
    def __init__(self, cachename: str, listfile: Optional[Union[str, Path]]):
        log = logging.getLogger("csvcache")
        self.name = cachename

        if listfile is None:
            self.nocache = True
            self.listfile = None
            log.debug("not resolving, not initializing cache")
            return

        listfile = Path(listfile)
        self.listfile = Path(listfile)

        if not self.listfile.exists():
            log.warning(f"{self.listfile} does not exist, not resolving fileids")
            self.nocache = True
            return

        self.nocache = False

        self.cachefile = Path(str(self.listfile) + ".cache")
        self.populate()

    # This is a bit ugly, we're actually having 'populate' create the database,
    # too, since it needs to see if it exists at all to figure out if it should
    # populate.

    def __populate_needed(self) -> bool:
        log = logging.getLogger("csvcache")

        if self.nocache:
            log.debug("nocache set, cache population not needed")
            return False

        if not self.cachefile.exists():
            log.debug(f"{self.cachefile} doesn't exist, population needed")
            return True

        if self.listfile is None:
            log.warning(f"__populate_needed called when self.listfile is None")
            return False

        if self.listfile.stat().st_mtime <= self.cachefile.stat().st_mtime:
            log.debug(f"{self.cachefile} exists and is up to date, population not needed")
            return False

        # else
        log.debug(f"{self.cachefile} exists but is out of date, population needed")
        return False


    def populate(self, force: bool = False) -> None:
        log = logging.getLogger("csvcache")

        assert self.listfile is not None
        assert self.cachefile is not None

        if not self.__populate_needed():
            if not force:
                # print(self.cachefile)
                self.db = sqlite3.connect(self.cachefile)
                return

            # else
            log.debug(f"{self.cachefile} doesn't need population, but population forced")

        # This creates a new handle... an existing one -should- get cleaned
        # up when the reference to it here disappears.
        # FIXME: verify that sqlite3 throws an exception if connect() fails
        self.db = sqlite3.connect(self.cachefile)

        # actually do the rebuild
        log.debug("starting cache rebuild")
        started = time.time()
        cur = self.db.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS fdids (
                id INTEGER NOT NULL PRIMARY KEY,
                name VARCHAR
            );
            """)

        # Make sure it's empty -- it's almost definitely faster to just reload
        # everything than to check if each indiviual row needs updating anyhow
        cur.execute("DELETE FROM fdids;")

        with self.listfile.open("r") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            to_db = [(row[0], row[1]) for row in reader]

        cur.executemany("INSERT INTO fdids (id, name) VALUES (?, ?);", to_db)
        self.db.commit()

        runtime = time.time() - started
        log.debug(f"cache rebuilt with {len(to_db)} entries in {runtime:.2f}s")

    # accept a string just as a convenience feature
    # FIXME: check if we actually use that convenience feature
    def get_by_id(self, id: Union[int, str]) -> Optional[str]:
        log = logging.getLogger("csvcache")
        if self.nocache:
            log.debug("not resolving, not getting fileid")
            return None

        id = int(id)
        cur = self.db.cursor()
        q = "SELECT name FROM fdids WHERE id=?"

        try:
            res = cur.execute(q, [id]).fetchone()
        except sqlite3.Error as e:
            log.error(f"Unexpected sqlite error: {e}")
            raise e

        if res is not None:
            return cast(str, res[0])

        # else
        return None


caches: Dict[str, ListfileCache] = {}

# is this an ok name? is it ok to assume this will always be accessed as
# something like "listfile.get()"?
def get(cachename: str) -> ListfileCache:
    # log = logging.getLogger("csvcache")

    if cachename in caches:
        # log.debug(f"getting existing cache {cachename}: {ppretty(caches[cachename])}")
        return caches[cachename]

    raise ValueError(f"unknown cache: {cachename}")


def init(cachename: str, file: Optional[Union[str, Path]]) -> ListfileCache:
    log = logging.getLogger("csvcache")
    file = Path(file) if file is not None else None
    # If it already exists, call populate() to reload things if it makes sense
    if cachename in caches:
        c = caches[cachename]
        # import sys
        # print(ppretty(c), file=sys.stderr)

        if c.nocache and file is None:
            log.debug(f"reinitializing nocache cache {cachename}, doing nothing")
            return c

        lfile = getattr(c, "listfile", None)
        if not c.nocache and lfile is not None and lfile == file:
            log.debug(f"reinitializing existing cache {cachename} from {file}")
            c.populate()
            return c

        # and by "reinitialize" we mean "make from scratch"
        log.debug(f"reinitializing existing cache {cachename} from NEW file {file}")
    else:
        log.debug(f"initializing new cache {cachename} from {file}")

    caches[cachename] = ListfileCache(cachename, file)
    log.debug(f"initialized cache {cachename} as: {ppretty(caches[cachename])}")
    return caches[cachename]
