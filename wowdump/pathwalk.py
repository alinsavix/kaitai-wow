import argparse
import logging
from typing import Dict, Iterable, List

from kaitaistruct import KaitaiStruct

from .dumputil import ktype, whatis
from .filters import check_filtered, check_geometrypath
from .simplifiers import check_simplify

# from ppretty import ppretty


# pathwalk is used by more than just the 'pathwalk' command, and it's  fairly
# big and complicated, so it gets its own file

def pathwalk(args: argparse.Namespace, obj: KaitaiStruct, path: str) -> Iterable[str]:
    lgsimplify = logging.getLogger("simplify")
    lgdisp = logging.getLogger("disposition")

    logger = logging.getLogger()
    logger.debug(f"in: path: {path}  type: {type(obj)} {whatis(obj)}")

    # I don't thiiiiiiiink we get called with an object that isn't a
    # kaitai type, so even though we used to have to figure out object
    # type here, seems like we don't, at this point?
    obj_keys = cacheattrs(obj)

    # if path == "/skin/bulkes/0":
    #     print("breakpoint")

    for k in obj_keys:
        workpath = f"{path}/{k}"

        # if workpath == "/model/vertices":
        #     print("breakpoint")

        logger.debug(f"getattr {k} from obj type {type(obj)}")
        v = getattr(obj, k)

        kt = ktype(v)

        logger.debug(f"checking for array elision for {workpath}")
        # this is probably a code smell, if not worse. If our current level
        # isn't geometry, but we add a '/0' to it and it is, that means it's
        # the very top of a geometry tree, and we can save ourselves the
        # effort of descending into it (and thus reading & parsing it) by
        # just escaping now.
        if not args.geometry and not check_geometrypath(workpath) and check_geometrypath(f"{workpath}/0"):
            if not check_filtered(args, workpath):
                yield f"{workpath}/... = [geometry data elided, use --geometry to include]"
            continue

        # if we have ofs_xxx or num_xxx, and *also* just have xxx,
        # we don't need the offset/size anymore
        if args.hide_unneeded and isinstance(k, str) and (k.startswith("ofs_") or k.startswith("num_")):
            m2a_suffix = k[len("ofs_"):]
            if m2a_suffix in obj_keys:
                continue

        # FIXME: Where is the best place for simplifiers? Here?
        lgsimplify.debug(f"checking simplifier for {workpath}")
        s = check_simplify(workpath) if args.simplify else None
        if s:
            lgsimplify.debug(f"using simplifier for {workpath}")

            # if getting simplified, it's a "final" path, so check filtering
            if check_filtered(args, workpath):
                continue

            # FIXME: this feels sloppy
            if kt == "base" or kt == "list":
                simplified = s(v, obj, args)
            else:
                simplified = s(v, obj, args)
            if simplified is not None:
                yield f"{workpath} = {simplified}"

            # We either simplified w/ output, or simplified out of existence.
            # either way, move on
            continue

        if kt == "list":
            lgdisp.debug(f"{workpath}[] --> array processing (len {len(v)})")

            # everything in an array shoooould have the same contents, so no
            # benefit to checking for a simplifier match for each, just check
            # for the first element and keep it
            s = check_simplify(f"{workpath}/0") if args.simplify else None

            for i, el in enumerate(v):
                arraypath = f"{workpath}/{i}"
                elt = ktype(el)

                # if --geometry is specified, we still want to limit it to just
                # our array limit of entries, unless we've set arraylimit=0
                if check_geometrypath(arraypath) and args.arraylimit > 0 and i >= args.arraylimit:
                    logger.debug(
                        f"eliding remaining geometry entries for {workpath}")
                    if not check_filtered(args, arraypath):
                        remaining = len(v) - args.arraylimit
                        yield f"{workpath}/... = [{remaining} elided of {len(v)} total]"
                    break

                # if we're going to elide all arrays (via --elide-all), check
                # that, too, and bail if we've hit the limit
                if args.elide_all and args.arraylimit > 0 and i >= args.arraylimit:
                    logger.debug(
                        f"eliding remaining array entries for {workpath}")
                    if not check_filtered(args, arraypath):
                        remaining = len(v) - args.arraylimit
                        yield f"{workpath}/... = [{remaining} elided of {len(v)} total]"
                    break

                # FIXME: dedupe dedupe
                # s = check_simplify(arraypath) if args.simplify else None
                if s:
                    lgsimplify.debug(f"using simplifier for {arraypath}")

                    # if getting simplified, it's a "final" path, so check filtering
                    if check_filtered(args, arraypath):
                        continue

                    lgsimplify.debug(
                        f"array simplify type: {type(el)}   value: {el}")
                    # FIXME: this feels sloppy
                    if elt == "base" or elt == "list":
                        simplified = s(el, v, args)
                    else:
                        simplified = s(el, v, args)
                    if simplified is not None:
                        yield f"{arraypath} = {simplified}"

                    # We either simplified w/ output, or simplified out of existence.
                    # either way, move on
                    continue

                # if elt in [int, float, str]:
                if elt == "base":
                    # we're at a final path, check filtering
                    if check_filtered(args, workpath):
                        continue

                    if isinstance(el, str):
                        el = el.rstrip("\0")
                    lgdisp.debug(f"array {arraypath} --> final ({el})")
                    yield f"{arraypath} = {el}"
                else:
                    lgdisp.debug(f"{arraypath} --> array descent")
                    yield from pathwalk(args, el, arraypath)

        elif kt == "kaitai":
            # FIXME: I think we're supposed to do one of these without the {k}
            if k == "data":
                lgdisp.debug(f"{workpath} --> kaitai data descent")
                yield from pathwalk(args, v, workpath)
            else:
                lgdisp.debug(f"{workpath} --> kaitai descent type {type(k)}")
                # debug(f"recursing kaitai value, type: {type(k)}")
                yield from pathwalk(args, v, workpath)

        elif kt == "base":
            # we're at a final path, check filtering
            if check_filtered(args, workpath):
                continue

            if isinstance(v, str):
                v = v.rstrip("\0")

            lgdisp.debug(f"{workpath} --> final ({v})")
            yield f"{workpath} = {v}"

        else:
            lgdisp.debug(f"{workpath} --> descend (type {type(v)}")
            yield from pathwalk(args, v, workpath)


# When dealing with big files with a lot of fields, we end up spending a
# good bit of time filtering through the various attributes on each object
# to find the ones we need to actually descend through and such. By pulling
# that filtering logic into a separate funciton that caches the results, we
# can gain some performance on big objects (and make the main walk function
# a little easier to read). Some testing on `valeera.m2` suggests that on
# large files dumped with `--geometry` save about 5% runtime. Definitely
# not great, but no real downsides, either. At least, don't think so. All
# the unit tests pass!
#
# FIXME: how much overhead to passing objects here? Is there any better way?
# Can we just pass the type itself instead?
attrcache: Dict[type, List[str]] = {}

def cacheattrs(obj: object) -> List[str]:
    t = type(obj)

    if t in attrcache:
        return attrcache[t]

    cacheentry = []

    obj_keys = dir(obj)

    for k in obj_keys:
        if k[0] == "_":
            continue

        # FIXME: figure out what to do with m2track
        if k == "m2array_type":
            continue

        v = getattr(obj, k)

        # FIXME: Can we economize here, any?
        kt = ktype(v)
        if kt == "skip":  # class, method, datatype
            continue

        # looks like k is something we want to keep
        cacheentry.append(k)

    attrcache[t] = cacheentry
    return cacheentry
