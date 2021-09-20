import inspect
import os
import re
import sys
import time
from typing import Any, Callable, Dict, List, Optional

import logging
from kaitaistruct import BytesIO, KaitaiStream, KaitaiStruct
from ppretty import ppretty

def kttree(obj, path: str=""):
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
            if type(v) == type([]):
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
