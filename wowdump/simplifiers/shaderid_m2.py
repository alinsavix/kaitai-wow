# simplifier to simplify shaderids for m2 models
import logging

def simplify_shaderid_m2(d, parent, _args):
    logger = logging.getLogger("simplify")
    logger.debug("using shaderid (m2) simplifier")

    pixel = get_m2_pixel_shader(d, parent.texture_count)
    vertex = get_m2_vertex_shader(d, parent.texture_count)

    return f"{d}  # {pixel}, {vertex}"


# shader lookup bits, stolen directly from WoWbject Importer
m2_shader_table = (
    ("PS_Combiners_Opaque_Mod2xNA_Alpha",
     "VS_Diffuse_T1_Env", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Opaque_AddAlpha", "VS_Diffuse_T1_Env", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Opaque_AddAlpha_Alpha",
     "VS_Diffuse_T1_Env", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Opaque_Mod2xNA_Alpha_Add",
     "VS_Diffuse_T1_Env_T1", "HS_T1_T2_T3", "DS_T1_T2_T3", 3),
    ("PS_Combiners_Mod_AddAlpha", "VS_Diffuse_T1_Env", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Opaque_AddAlpha", "VS_Diffuse_T1_T1", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Mod_AddAlpha", "VS_Diffuse_T1_T1", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Mod_AddAlpha_Alpha",
     "VS_Diffuse_T1_Env", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Opaque_Alpha_Alpha",
     "VS_Diffuse_T1_Env", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Opaque_Mod2xNA_Alpha_3s",
     "VS_Diffuse_T1_Env_T1", "HS_T1_T2_T3", "DS_T1_T2_T3", 3),
    ("PS_Combiners_Opaque_AddAlpha_Wgt",
     "VS_Diffuse_T1_T1", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Mod_Add_Alpha", "VS_Diffuse_T1_Env", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Opaque_ModNA_Alpha",
     "VS_Diffuse_T1_Env", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Mod_AddAlpha_Wgt", "VS_Diffuse_T1_Env", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Mod_AddAlpha_Wgt", "VS_Diffuse_T1_T1", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Opaque_AddAlpha_Wgt",
     "VS_Diffuse_T1_T2", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Opaque_Mod_Add_Wgt",
     "VS_Diffuse_T1_Env", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Opaque_Mod2xNA_Alpha_UnshAlpha",
     "VS_Diffuse_T1_Env_T1", "HS_T1_T2_T3", "DS_T1_T2_T3", 3),
    ("PS_Combiners_Mod_Dual_Crossfade", "VS_Diffuse_T1", "HS_T1", "DS_T1", 1),
    ("PS_Combiners_Mod_Depth", "VS_Diffuse_EdgeFade_T1", "HS_T1", "DS_T1", 2),
    ("PS_Combiners_Opaque_Mod2xNA_Alpha_Alpha",
     "VS_Diffuse_T1_Env_T2", "HS_T1_T2_T3", "DS_T1_T2_T3", 3),
    ("PS_Combiners_Mod_Mod", "VS_Diffuse_EdgeFade_T1_T2", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Mod_Masked_Dual_Crossfade",
     "VS_Diffuse_T1_T2", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Opaque_Alpha", "VS_Diffuse_T1_T1", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Opaque_Mod2xNA_Alpha_UnshAlpha",
     "VS_Diffuse_T1_Env_T2", "HS_T1_T2_T3", "DS_T1_T2_T3", 3),
    ("PS_Combiners_Mod_Depth", "VS_Diffuse_EdgeFade_Env", "HS_T1", "DS_T1", 1),
    ("PS_Guild", "VS_Diffuse_T1_T2_T1", "HS_T1_T2_T3", "DS_T1_T2", 3),
    ("PS_Guild_NoBorder", "VS_Diffuse_T1_T2", "HS_T1_T2", "DS_T1_T2_T3", 2),
    ("PS_Guild_Opaque", "VS_Diffuse_T1_T2_T1", "HS_T1_T2_T3", "DS_T1_T2", 3),
    ("PS_Illum", "VS_Diffuse_T1_T1", "HS_T1_T2", "DS_T1_T2", 2),
    ("PS_Combiners_Mod_Mod_Mod_Const",
     "VS_Diffuse_T1_T2_T3", "HS_T1_T2_T3", "DS_T1_T2_T3", 3),
    ("PS_Combiners_Mod_Mod_Mod_Const",
     "VS_Color_T1_T2_T3", "HS_T1_T2_T3", "DS_T1_T2_T3", 3),
    ("PS_Combiners_Opaque", "VS_Diffuse_T1", "HS_T1", "DS_T1", 1),
    ("PS_Combiners_Mod_Mod2x", "VS_Diffuse_EdgeFade_T1_T2", "HS_T1_T2", "DS_T1_T2", 2),
)


def get_m2_pixel_shader(shaderID, op_count=2):
    if shaderID == 0:
        return "WotLK_Runtime_Selector"

    if shaderID & 0x8000:
        shaderID &= (~0x8000)
        ind = shaderID.bit_length()
        if not m2_shader_table[ind][4] == op_count:
            return m2_shader_table[ind + 1][0]
        else:
            return m2_shader_table[ind][0]
    else:
        if op_count == 1:
            if shaderID & 0x70:
                return "PS_Combiners_Mod"
            else:
                return "PS_Combiners_Opaque"
        else:
            lower = shaderID & 7

            if shaderID & 0x70:
                if lower == 0:
                    return "PS_Combiners_Mod_Opaque"
                elif lower == 3:
                    return "PS_Combiners_Mod_Add"
                elif lower == 4:
                    return "PS_Combiners_Mod_Mod2x"
                elif lower == 6:
                    return "PS_Combiners_Mod_Mod2xNA"
                elif lower == 7:
                    return "PS_Combiners_Mod_AddNA"
                else:
                    return "PS_Combiners_Mod_Mod"
            else:
                if lower == 0:
                    return "PS_Combiners_Opaque_Opaque"
                elif lower == 3:
                    return "PS_Combiners_Opaque_AddAlpha"
                elif lower == 4:
                    return "PS_Combiners_Opaque_Mod2x"
                elif lower == 6:
                    return "PS_Combiners_Opaque_Mod2xNA"
                elif lower == 7:
                    return "PS_Combiners_Opaque_AddAlpha"
                else:
                    return "PS_Combiners_Opaque_Mod"


def get_m2_vertex_shader(shader_id, op_count=2):
    if shader_id & 0x8000:
        shader_id &= (~0x8000)
        ind = shader_id.bit_length()
        return m2_shader_table[ind + 1][1]
    else:
        if op_count == 1:
            if shader_id & 0x80:
                return "VS_Diffuse_Env"
            else:
                if shader_id & 0x4000:
                    return "VS_Diffuse_T2"
                else:
                    return "VS_Diffuse_T1"
        else:
            if shader_id & 0x80:
                if shader_id & 0x8:
                    return "VS_Diffuse_Env_Env"
                else:
                    return "VS_Diffuse_Env_T1"
            else:
                if shader_id & 0x8:
                    return "VS_Diffuse_T1_Env"
                else:
                    if shader_id & 0x4000:
                        return "VS_Diffuse_T1_T2"
                    else:
                        return "VS_Diffuse_T1_T1"


shader_m2_re = r"^/skin/batches/\d+/shader_id$"


simplifiers = [
    (shader_m2_re, simplify_shaderid_m2),
]
