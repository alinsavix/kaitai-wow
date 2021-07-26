# simplify flags
# FIXME: Should the output be inside { } or something?
def simplify_flags(d, _parent, _cachecon, _args):
    if not isinstance(d, dict):
        return d

    flags = []
    for k, v in d.items():
        if v:
            flags.append(k)

    if len(flags) == 0:
        return "none"

    return ", ".join(flags)


flags_re = r"/(global_)?flags$"


simplifiers = [
    (flags_re, simplify_flags),
]
