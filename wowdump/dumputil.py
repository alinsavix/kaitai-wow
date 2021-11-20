import hashlib
import inspect
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, TextIO, Union, cast

from kaitaistruct import KaitaiStruct

from . import filetypes


# a simple class for letting us hand around an open file so we can
# retarget outputs if/when needed
class DataOutput(object):
    fileName: Optional[str] = None
    fileHandle: TextIO
    is_stdout: bool

    def __init__(self, fn: Optional[str]):
        self.fileName = fn

    def __enter__(self):
        if self.fileName is not None:
            self.fileHandle = open(self.fileName, "w")
            self.is_stdout = False
        else:
            self.fileHandle = sys.stdout
            self.is_stdout = True

        return self

    def __exit__(self, _ex_type, _ex_value, _ex_traceback):
        # only close if not stdout
        if not self.is_stdout:
            self.fileHandle.close()
            return False

    def write(self, outstr: str) -> None:
        print(outstr, file=self.fileHandle, flush=self.is_stdout)


# generate the contenthash for a file, which is just an md5sum of the file
def get_contenthash(file: Union[str, Path]) -> str:
    file = Path(file)
    with file.open("rb") as f:
        h = hashlib.md5()
        chunk = f.read(8192)
        while chunk:
            h.update(chunk)
            chunk = f.read(8192)

    return h.hexdigest()


def fileparse(file: Union[str, Path]) -> KaitaiStruct:
    # FIXME: commented out code is previous error handling, figure out if
    # we need that still, and how, and where
    # try:
    #     target = load_wowfile(file)
    # except (ValueError, OSError) as e:
    #     print(f"ERROR: {e}", file=sys.stderr)
    #     return 65  # os.EX_DATAERR
    return filetypes.load_wowfile(file)


# "kaitai type"
def ktype(v: object) -> str:
    logger = logging.getLogger()
    if inspect.isclass(v):
        logger.debug("var is type class, skipping")
        return "skip"

    if inspect.ismethod(v) or inspect.isbuiltin(v):
        logger.debug("var is is method or builtin, skipping")
        return "skip"

    if isinstance(v, type):
        logger.debug("var is defines a datatype, skipping")
        return "skip"

    if isinstance(v, list):
        logger.debug("var is type list")
        return "list"

    if isinstance(v, KaitaiStruct):
        logger.debug(f"var is a kaitai type {type(v)}")
        return "kaitai"

    if type(v) in [int, float, str, bool]:
        logger.debug("var is a base type")
        return "base"

    # otherwise is a dict type
    # FIXME: I think dict type, anyhow
    logger.debug("var is (probably) a dict type")
    return "dict"


KTTree = Union[Dict[Union[str, int], Any], List[Any]]
def kttree(obj: object, path: str = "") -> KTTree:
    r: Dict[Union[str, int], Any] = {}
    lgkttree = logging.getLogger("kttree")
    lgkttree.debug(f"kttree path: {path}")
    # debug(f"in: path: {path}  type: {type(obj)} {whatis(obj)}")

    value: Union[KTTree, KaitaiStruct, int, float, str, bool]

    for k in dir(obj):
        if k[0] == "_":
            continue

        lgkttree.debug(f"getattr {k} from obj type {type(obj)}")
        v = getattr(obj, k)

        if inspect.isclass(v):
            # debug(f"is class, skipping")
            pass
        elif inspect.ismethod(v) or inspect.isbuiltin(v):
            # debug(f"is method or builtin, skipping")
            pass
        elif isinstance(v, type):
            # debug(f"defines a datatype, skipping")
            pass
        else:
            if isinstance(v, list):
                # disp(f"{path}/{k}[]", f"array processing (len {len(v)})")
                value = []
                for i, el in enumerate(v):
                    # debug(f"appending {el}")
                    if type(el) in [int, float, str]:
                        # disp(f"{path}[{i}]", f"final ({el})")
                        value.append(el)
                    else:
                        # disp(f"{path}[{i}]", "array descent")
                        cast(List[Any], value).append(kttree(el, f"{path}/{k}[{i}]"))
            elif isinstance(v, KaitaiStruct):
                if k == "data":
                    # disp(f"{path}", "kaitai data descent")
                    value = kttree(v, f"{path}/{k}")
                else:
                    # disp(f"{path}.{k}", "kaitai descent")
                    # debug(f"recursing kaitai value, type: {type(k)}")
                    value = kttree(v, f"{path}/{k}")
            else:
                # log(f"using plain value: {v} {whatis(v)}")
                if type(v) in [int, float, str, bool]:
                    # disp(f"{path}.{k}", f"final ({v})")
                    value = v
                else:
                    # FIXME: figure out m2track better
                    # if k == "m2array_type" or k == "m2track_type":
                    #     # disp(f"{path}.{k}", "ignored")
                    #     pass
                    # else:
                    #     # disp(f"{path}.{k}", f"descend (type {type(v)}")
                    #     value = kttree(v, f"{path}/{k}")
                    if k == "m2array_type":
                        pass
                    else:
                        value = kttree(v, f"{path}/{k}")

            if value is not None:
                r[k] = value

    # debug(f"out:  returning {r}")
    return r


def whatis(obj: object) -> Set[str]:
    objis: Set[str] = set()

    if inspect.ismodule(obj):
        objis.add("module")
    if inspect.isclass(obj):
        objis.add("class")
    if inspect.ismethod(obj):
        objis.add("method")
    if inspect.isfunction(obj):
        objis.add("function")
    if inspect.isgeneratorfunction(obj):
        objis.add("generatorfunction")
    if inspect.isgenerator(obj):
        objis.add("generator")
    if inspect.iscoroutinefunction(obj):
        objis.add("coroutinefunction")
    if inspect.iscoroutine(obj):
        objis.add("coroutine")
    if inspect.isawaitable(obj):
        objis.add("awaitable")
    if inspect.isasyncgenfunction(obj):
        objis.add("asyncgenfunction")
    if inspect.isasyncgen(obj):
        objis.add("asyncgen")
    if inspect.istraceback(obj):
        objis.add("traceback")
    if inspect.isframe(obj):
        objis.add("frame")
    if inspect.iscode(obj):
        objis.add("code")
    if inspect.isbuiltin(obj):
        objis.add("builtin")
    if inspect.isroutine(obj):
        objis.add("routine")
    if inspect.isabstract(obj):
        objis.add("abstract")
    if inspect.ismethoddescriptor(obj):
        objis.add("methoddescriptor")
    if inspect.isdatadescriptor(obj):
        objis.add("datadescriptor")
    if inspect.isgetsetdescriptor(obj):
        objis.add("getsetdescriptor")
    if inspect.ismemberdescriptor(obj):
        objis.add("memberdescriptor")

    if isinstance(obj, KaitaiStruct):
        objis.add("kaitaistruct")

    return objis
