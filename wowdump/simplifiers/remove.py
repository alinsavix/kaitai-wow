# simplifier to just remove stuff
def simplify_remove(d, _parent, _cachecon, _args) -> str:
    return None


# Runtime data that doesn't exist in WoW data files (usually just zeroes that
# are filled in after the structure is loaded into memory verbatim
runtime_re = r"/runtime_data$"


# Values believed to be unused
unused_re = r"unused\d*$"

# Chunk type identifiers before being reversed for human consumption
raw_chunk_re = r"chunk_type_raw$"


# mapping
simplifiers = [
    (runtime_re, simplify_remove),
    (unused_re, simplify_remove),
    (raw_chunk_re, simplify_remove),
]
