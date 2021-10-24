# simplifiers for color values
import logging

def simplify_irgb(d, _parent, _cachecon, _args) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using irgb simplifier")

    r = int(d.r)
    g = int(d.g)
    b = int(d.b)

    return f"rgb({r}, {g}, {b})  # {r:02x}{g:02x}{b:02x}"

def simplify_irgba(d, _parent, _cachecon, _args) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using irgba simplifier")
    r = int(d.r)
    g = int(d.g)
    b = int(d.b)
    a = int(d.a)

    return f"rgba({r}, {g}, {b}, {a})  # {r:02x}{g:02x}{b:02x}{a:02x}"


emitter_rgb_re = r"^/model/particle_emitters/\d+/old/p/colors/values/values/\d+$"
ambient_rgba_re = r"^/chunks/\d+/chunk_data/amb_color$"
wmomat_rgba_re = r"^/chunks/\d+/chunk_data/materials/\d+/(diff_color|sidn_color|frame_sidn_color)$"
wmomat_vertex_rgba_re = r"/chunks/\d+/chunk_data/vertex_colors/\d+$"
wmomat_header_rgba_re = r"/chunks/\d+/chunk_data/header_color_replacement$"


simplifiers = [
    (emitter_rgb_re, simplify_irgb),
    (ambient_rgba_re, simplify_irgba),
    (wmomat_rgba_re, simplify_irgba),
    (wmomat_vertex_rgba_re, simplify_irgba),
    (wmomat_header_rgba_re, simplify_irgba),
]
