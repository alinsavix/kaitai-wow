# simplifiers for enum values
import logging

def simplify_enum(d, _parent, _args):
    logger = logging.getLogger("simplify")
    logger.debug("using enum simplifier")

    # If a field is an enum, but a value for the specific integer doesn't
    # exist, kaitai just returns an int, rather than an enum value without
    # an enum name.
    if isinstance(d, int):
        return f"{d}"

    return f"{d.value}  # {d.name}"


anim_id_re = r"/chunks/\d+/chunk_data/anim_file_ids/\d+/anim_id$"
blp_re = r"^/(color_encoding|preferred_format)$"
interpolation_type_re = r"(interpolation_type|m2track_type)$"
material_blending_re = r"^/model/materials/\d+/blending_mode$"
particle_old_blending_re = r"/model/particle_emitters/\d+/old/(blending|emitter)_type$"
sequence_id_re = r"/sequences/\d+/id$"
texture_type_re = r"^/model/textures/\d+/type$"
version_re = r"^/model/version$"


simplifiers = [
    (anim_id_re, simplify_enum),
    (blp_re, simplify_enum),
    (interpolation_type_re, simplify_enum),
    (material_blending_re, simplify_enum),
    (particle_old_blending_re, simplify_enum),
    (sequence_id_re, simplify_enum),
    (texture_type_re, simplify_enum),
    (version_re, simplify_enum),
]
