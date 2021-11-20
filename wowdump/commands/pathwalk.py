from .. import csvcache
from ..dumputil import DataOutput, fileparse, get_contenthash
from ..filters import check_filtered
from ..pathwalk import pathwalk


def cmd_pathwalk(args):
    # FIXME: Should we just blanket-initialize this in main()?
    # Path(args.listfile).unlink(missing_ok=True)
    if args.resolve:
        csvcache.init("listfile", args.listfile)
    else:
        csvcache.init("listfile", None)

    # FIXME: better error handling (or error handling at all)
    with DataOutput(args.output) as out:
        target = fileparse(args.file)

        # out.write(f"# path = {file}")
        if not check_filtered(args, "/contenthash"):
            h = get_contenthash(args.file)
            out.write(f"/contenthash = {h}")

        for line in pathwalk(args, target, ""):
            out.write(line)

    return 0
