# simplifier for shader ids for WMO objects
import logging

# FIXME: deal with out-of-range values
def simplify_shaderid_wmo(d, _parent, _cachecon, _args):
    logger = logging.getLogger("simplify")
    logger.debug("using shaderid (wmo) simplifier")

    id = d.value
    pixel = wmo_shader_table[id][2]
    vertex = wmo_shader_table[id][1]
    name = wmo_shader_table[id][0]

    # simplifier to just remove stuff
    return f"{id}  # {pixel}, {vertex}   (\"{name}\")"


# in the format of (name, vertex shader, pixel shader)
wmo_shader_table = [
    ("Diffuse", "MapObjDiffuse_T1", "MapObjDiffuse"),
    ("Specular", "MapObjSpecular_T1", "MapObjSpecular"),
    ("Metal", "MapObjSpecular_T1", "MapObjMetal"),
    ("Env", "MapObjDiffuse_T1_Refl", "MapObjEnv"),
    ("Opaque", "MapObjDiffuse_T1", "MapObjOpaque"),
    ("EnvMetal", "MapObjDiffuse_T1_Refl", "MapObjEnvMetal"),
    ("TwoLayerDiffuse", "MapObjDiffuse_Comp", "MapObjTwoLayerDiffuse"),
    ("TwoLayerEnvMetal", "MapObjDiffuse_T1", "MapObjTwoLayerEnvMetal"),
    ("TwoLayerTerrain", "MapObjDiffuse_Comp_Terrain", "MapObjTwoLayerTerrain"),
    ("DiffuseEmissive", "MapObjDiffuse_Comp", "MapObjDiffuseEmissive"),
    ("waterWindow", "FFXWaterWindow", "FFXWaterWindow"),
    ("MaskedEnvMetal", "MapObjDiffuse_T1_Env_T2", "MapObjMaskedEnvMetal"),
    ("EnvMetalEmissive", "MapObjDiffuse_T1_Env_T2", "MapObjEnvMetalEmissive"),
    ("TwoLayerDiffuseOpaque", "MapObjDiffuse_Comp", "MapObjTwoLayerDiffuseOpaque"),
    ("submarineWindow", "FFXSubmarineWindow", "FFXSubmarineWindow"),
    ("TwoLayerDiffuseEmissive", "MapObjDiffuse_Comp",
     "MapObjTwoLayerDiffuseEmissive"),
    ("DiffuseTerrain", "MapObjDiffuse_T1", "MapObjDiffuse"),
    ("AdditiveMaskedEnvMetal", "MapObjDiffuse_T1_Env_T2",
     "MapObjAdditiveMaskedEnvMetal"),
    ("TwoLayerDiffuseMod2x", "MapObjDiffuse_CompAlpha", "MapObjTwoLayerDiffuseMod2x"),
    ("TwoLayerDiffuseMod2xNA", "MapObjDiffuse_Comp", "MapObjTwoLayerDiffuseMod2xNA"),
    ("TwoLayerDiffuseAlpha", "MapObjDiffuse_CompAlpha", "MapObjTwoLayerDiffuseAlpha"),
    ("Lod", "MapObjDiffuse_T1", "MapObjLod"),
    ("Parallax", "MapObjParallax", "MapObjParallax"),
]


# FIXME: this could be way, way better
shader_wmo_re = r"^/chunks/\d+/chunk_data/materials/\d+/shader_id$"


simplifiers = [
    (shader_wmo_re, simplify_shaderid_wmo),
]
