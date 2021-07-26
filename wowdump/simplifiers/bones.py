# simplifiers for bone-related things (when we have them)
def simplify_fourbone(d, _parent, _cachecon, _args) -> str:
    return f"[ {d[0]}, {d[1]}, {d[2]}, {d[3]} ]"


fourbone_re = r"^/model/vertices/\d+/(bone_indices|bone_weights)$"


simplifiers = [
    (fourbone_re, simplify_fourbone),
]
