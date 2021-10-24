# simplifier to display coordinates as (x,y) or similar
import logging

def simplify_xyz(d, _parent, _cachecon, args) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using xyz simplifier")

    x = round(d.x, args.precision)
    y = round(d.y, args.precision)
    z = round(d.z, args.precision)
    return f"xyz({x}, {y}, {z})"


def simplify_wxyz(d, _parent, _cachecon, args) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using wxyz simplifier")

    w = round(d.w, args.precision)
    x = round(d.x, args.precision)
    y = round(d.y, args.precision)
    z = round(d.z, args.precision)
    return f"wxyz({w}, {x}, {y}, {z})"


def simplify_xy(d, _parent, _cachecon, args) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using xy simplifier")

    x = round(d.x, args.precision)
    y = round(d.y, args.precision)
    return f"xy({x}, {y})"


def simplify_nested_xy(d, _parent, _cachecon, _args) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using nested xy simplifier")

    x = d.x.value
    y = d.y.value
    return f"xy({x}, {y})"


# regexes for simplify_xy
emitter_sizes_re = r"^/model/particle_emitters/\d+/old/p/sizes/values/values/\d+$"
verts_wmo_textcoords_re = r"/chunks/\d+/chunk_data/(tex_coords)/\d+$"
verts_texcoords_re = r"^/model/vertices/\d+/tex_coords/\d+$"


# regexes for simplify_xyz
attachment_pos_re = r"/attachments/\d+/position$"
bone_pivot_re = r"/bones/\d+/pivot$"
bone_xlate_re = r"/bones/\d+/translation/values/values/\d+/values/\d+$"
bone_scale_re = r"/bones/\d+/scale/values/values/\d+/values/\d+$"
skin_pos_re = r"/submeshes/\d+/(sort_)?center_position$"
camera_pos_re = r"/cameras/\d+/(target_)?position_base$"
collision_pos_re = r"/collision_(face_normals|positions)/\d+$"
bbox_re = r"/(bounding_box|collision_box)/(min|max)$"
events_pos_re = r"^/model/events/\d+/position$"
emitter_rot_scale_xlate_re = r"^/model/particle_emitters/\d+/old/p/(rot\d|scales|trans)$"
emitter_position_re = r"^/model/particle_emitters/\d+/old/position$"
seq_bbox_re = r"/sequences/\d+/bounds/extent/(min|max)$"
verts_vec_re = r"^/model/vertices/\d+/(normal|pos)$"
verts_wmo_re = r"/chunks/\d+/chunk_data/(vertices|normals)/\d+$"


# regexes for simplify_wxyz
bone_rot_re = r"/bones/\d+/rotation/values/values/\d+/values/\d+$"


# regexes for simplify_nested_xy
# FIXME: Can we make these behave better straight out of kaitai?
nested_xy_re = r"^/model/particle_emitters/\d+/multi_texture_param\d/\d+$"





simplifiers = [
    (emitter_sizes_re, simplify_xy),
    (verts_wmo_textcoords_re, simplify_xy),
    (verts_texcoords_re, simplify_xy),

    (attachment_pos_re, simplify_xyz),
    (bone_pivot_re, simplify_xyz),
    (bone_xlate_re, simplify_xyz),
    (bone_scale_re, simplify_xyz),
    (skin_pos_re, simplify_xyz),
    (camera_pos_re, simplify_xyz),
    (collision_pos_re, simplify_xyz),
    (bbox_re, simplify_xyz),
    (events_pos_re, simplify_xyz),
    (emitter_rot_scale_xlate_re, simplify_xyz),
    (emitter_position_re, simplify_xyz),
    (seq_bbox_re, simplify_xyz),
    (verts_vec_re, simplify_xyz),
    (verts_wmo_re, simplify_xyz),

    (bone_rot_re, simplify_wxyz),

    (nested_xy_re, simplify_nested_xy),
]
