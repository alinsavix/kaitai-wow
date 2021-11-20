import argparse
import re

# from typing import Optional, Union, TextIO

# rudamentary filtering
#
# behavior depends on whether keep or discard filters are provided,
# or both.
#
# no filter -- allow all
# only keep -- discard all but matching
# only discard --  keep all but matching
# both -- allow 'keep' matches, then discard all matching, then allow remaining
def check_filtered(args: argparse.Namespace, path: str) -> bool:
    if len(args.filters_keep) == 0 and len(args.filters_discard) == 0:
        return False

    # Always do the 'keep' first, if they exist, since if there's a match, we
    # don't care after that.
    if len(args.filters_keep) > 0:
        for filter in args.filters_keep:
            # r = regex_cache(filter)
            # if r and r.search(path):
            #     return False

            # print(f"check filter {filter} vs {path}")
            # if path.startswith(filter):
            if filter in path:
                return False

    if len(args.filters_discard):
        for filter in args.filters_discard:
            # r = regex_cache(filter)
            # if r and r.search(path):
            #     return True

            # if path.startswith(filter):
            if filter in path:
                return True

    # If we're here, we didn't match anything, so check which of the
    # combinations of above exists
    if len(args.filters_keep) > 0 and len(args.filters_discard) > 0:
        # We survived both filters, keep it
        return False

    if len(args.filters_keep) > 0:
        # we only wanted to keep some, so get rid of the rest
        return True

    # otherwise, we were discard-only, so don't filter anything remaining
    return False


# Given a path, check to see if it's one we want to normally elide (because
# it's geometry-related and thus probably really long and spammy with minimal
# value).
#
# FIXME: It'd be great if we didn't have to maintain the regex list by hand.
geom_path_re = re.compile(
    r"/(model|skin|chunk_data)/(bones|polys|indices|vertices|normals|tex_coords|bspnodes|vertex_colors|node_face_indices)/\d+$")

def check_geometrypath(path: str) -> bool:
    if geom_path_re.search(path):
        return True

    # else
    return False



# regex based filtering, WIP:
# There's probably a way better way to do this.
# filter_regex_cache = { }
# def regex_cache(re_str):
#     if not re_str.startswith("/") or not re_str.endswith("/"):
#         return None

#     if re_str in filter_regex_cache:
#         return filter_regex_cache[re_str]

#     re_compiled = re.compile(re_str, re.IGNORECASE)
#     filter_regex_cache[re_str] = re_compiled
#     return re_compiled
