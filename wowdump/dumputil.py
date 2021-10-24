import inspect

import logging
from kaitaistruct import KaitaiStruct


# "kaitai type"
def ktype(v):
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


def kttree(obj, path: str = ""):
    r = {}
    lgkttree = logging.getLogger("kttree")
    lgkttree.debug(f"kttree path: {path}")
    # debug(f"in: path: {path}  type: {type(obj)} {whatis(obj)}")

    value = None

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
                        value.append(kttree(el, f"{path}/{k}[{i}]"))
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


def whatis(obj):
    objis = []

    if inspect.ismodule(obj):
        objis.append("module")
    if inspect.isclass(obj):
        objis.append("class")
    if inspect.ismethod(obj):
        objis.append("method")
    if inspect.isfunction(obj):
        objis.append("function")
    if inspect.isgeneratorfunction(obj):
        objis.append("generatorfunction")
    if inspect.isgenerator(obj):
        objis.append("generator")
    if inspect.iscoroutinefunction(obj):
        objis.append("coroutinefunction")
    if inspect.iscoroutine(obj):
        objis.append("coroutine")
    if inspect.isawaitable(obj):
        objis.append("awaitable")
    if inspect.isasyncgenfunction(obj):
        objis.append("asyncgenfunction")
    if inspect.isasyncgen(obj):
        objis.append("asyncgen")
    if inspect.istraceback(obj):
        objis.append("traceback")
    if inspect.isframe(obj):
        objis.append("frame")
    if inspect.iscode(obj):
        objis.append("code")
    if inspect.isbuiltin(obj):
        objis.append("builtin")
    if inspect.isroutine(obj):
        objis.append("routine")
    if inspect.isabstract(obj):
        objis.append("abstract")
    if inspect.ismethoddescriptor(obj):
        objis.append("methoddescriptor")
    if inspect.isdatadescriptor(obj):
        objis.append("datadescriptor")
    if inspect.isgetsetdescriptor(obj):
        objis.append("getsetdescriptor")
    if inspect.ismemberdescriptor(obj):
        objis.append("memberdescriptor")

    if isinstance(obj, KaitaiStruct):
        objis.append("kaitaistruct")

    return objis
