# type: ignore
import re
from pathlib import Path
# from kaitaistruct import KaitaiStruct, KaitaiStructError
from typing import Optional

# from . import filetypes
# from . import csvcache
# from . import reports
# from .filetypes import load_wowfile, get_supported
from . import csvcache, filetypes
from .dumputil import get_contenthash
from .simplifiers.color import simplify_irgba_short
# from .simplifiers import check_simplify
from .simplifiers.coordinates import simplify_wxyz, simplify_xyz
from .simplifiers.enum import simplify_enum
from .simplifiers.fileid import simplify_fileid, simplify_fileid_short
from .simplifiers.flags import simplify_flags
from .simplifiers.shaderid_wmo import simplify_shaderid_wmo

# import logging
# from ppretty import ppretty



wmo_chunknames = {
    # Root
    "MOHD": "WMO Header",
    "MOTX": "Texture Definitions (unused in >= 8.1)",
    "MOMT": "Material Definitions",
    "MOUV": "Map Object UV Translation Speeds",
    "MOGN": "Group Names List",
    "MOGI": "Group Information",
    "MOSB": "Skybox Name",
    "MOSI": "Skybox FDID",
    "MOPV": "Portal Vertex List",
    "MOPT": "Portal List",
    "MOPR": "Portal Reference List",
    "MOVV": "Visible Block Vertices",
    "MOVB": "Visible Block List",
    "MOLT": "Light List",
    "MODS": "Doodad Set List",
    "MODN": "Doodad Name List",
    "MODI": "Doodad FDID List",
    "MODD": "Doodad Definition List",
    "MFOG": "Fog List",
    "MCVP": "Convex Volume Planes",
    "GFID": "Group FDID List",
    "MDDI": "[Something Doodad Related]",
    "MPVD": "Particulate Volume List",
    "MAVG": "Global Ambient Volume Definitions",  # see info at https://wowdev.wiki/WMO#MAVG
    "MAVD": "Ambient Volume Definitions",
    "MBVD": "Ambient Box Volume Definitions",
    "MFED": "Fox Extra Data",
    "MGI2": "Group Information v2",  # used in 9.1 or newer
    "MNLD": "New Dynamic Light Definitions",  # used in 9.1 or newer (e.g. Castle Nathria raid)
    "MDDL": "[Something Doodad Related]",  # used in 9.1 or newer

    # shared
    "MOLV": "Light Vertex Definitions",  # used in 9.1  e.g. fdid 3623016

    # Non-root
    "MOPY": "Map Object Polygon List",
    "MOVI": "Map Object Vertex Indexes",
    "MOVX": "[Something Vertex Related, Maybe?]",
    "MOVT": "Map Object Vertex Chunk",
    "MONR": "Map Object Normals",
    "MOTV": "Map Object Texture Coords",
    "MOBA": "Map Object Render Batches",
    "MOLR": "Map Object Light References",
    "MODR": "Map Object Doodad References",
    "MOBN": "Map Object BSP Nodes",
    "MOBR": "Map Object BSP Face References",
    "MOCV": "Map Object Vertex Colors",
    "MLIQ": "Map Object Liquids",
    # "MORI": "",  # Triangle strip indices?
    "MORB": "[something triangle strip related]",
    "MOTA": "Map Object Tangent Array",
    "MOBS": "Map Object Shadow Batches",
    "MDAL": "[Something Header Color Related]",
    "MOPL": "[Something with Terrain Cutting Planes]",
    "MOPB": "Map Object Prepass Batches",
    "MOLS": "Map Object Spot Lights",
    "MOLP": "Map Object Point Lights",
    "MLSS": "Map Object Lightset Spotlights",
    "MLSP": "Map Object Lightset Point Lights",
    "MLSO": "Map Object Spotlight Animsets",
    "MLSK": "Map Object Point Light Animsets",
    "MOS2": "Map Object Spotlight Anims",
    "MOP2": "Map Object Point Light Anims",
    "MPVR": "Map Object Particulate Volume Refs",
    "MAVR": "Map Object Ambient Volume Refs",
    "MBVR": "Map Object Box Volume Refs",
    "MFVR": "Map Object Fog Volume Refs",
    "MNLR": "Map Object New Light Refs",
    "MOLM": "May Object Lightmap List",  # Prerelease only
    "MOLD": "Map Object Lightmap Texture List",  # Prerelease only
}


def get_chunkmap(target):
    chunkmap = {}

    for chunk in target.chunks:
        chunktype = chunk.chunk_type
        if chunktype not in chunkmap:
            chunkmap[chunktype] = chunk.chunk_data
        else:
            if type(chunkmap[chunktype]) == list:
                chunkmap[chunktype].append(chunk.chunk_data)
            else:
                tmp = chunkmap[chunktype]
                chunkmap[chunktype] = [tmp, chunk.chunk_data]

    return chunkmap


def get_wmo_root(file):
    m = re.match(r"(.*)_\d{3}.wmo", file)
    if not m:
        raise ValueError(f"can't find root WMO name for {file}")

    rootfile = Path(m.group(1) + ".wmo")
    if not rootfile.exists():
        raise ValueError(f"can't find root WMO {rootfile}")

    # FIXME: verify load_wowfile has sane error handling
    root = filetypes.load_wowfile(rootfile)
    return get_chunkmap(root)


def wmo(args, file, out) -> None:
    args.precision = 4
    csvcache.init("listfile", args.listfile)

    target = filetypes.load_wowfile(file)
    chunkmap = get_chunkmap(target)

    if "MOGP" in chunkmap:
        out.write(f"{file}    type: WMO GROUP")
        mogp = chunkmap["MOGP"]
        chunkmap = get_chunkmap(chunkmap["MOGP"])
        is_root = False
    else:
        out.write(f"{file}    type: ROOT WMO")
        mogp = None
        is_root = True

    contenthash = get_contenthash(file)
    out.write(f"contenthash: {contenthash}")
    out.write("")

    out.write("Chunks present:")
    left = []
    right = []
    for i, c in enumerate(chunkmap.keys()):
        if c in wmo_chunknames:
            cn = wmo_chunknames[c]
        else:
            cn = "[Unknown Chunk Description]"

        if (i % 2) == 0:
            left.append(f"  {c}    {cn}")
        else:
            right.append(f"  {c}    {cn}")

    for i, j in zip(left, right):
        out.write(f"{i:<36s}{j}")

    # We might have one extra on the left
    if len(left) != len(right):
        out.write(f"{left[-1]:<36s}")

    if is_root:
        wmo_root(args, chunkmap, out)
    else:
        root = get_wmo_root(file)
        wmo_nonroot(args, mogp, chunkmap, root, out)




def wmo_root(args, chunkmap, out) -> None:
    out.write("")
    mohd = chunkmap["MOHD"]
    out.write(f"wmoID: {mohd.foreign_key} (needs db2?)")  # FIXME: probably needs DB2 lookup
    flags = simplify_flags(mohd.flags, None, args)
    out.write(f"flags: {flags}")
    out.write(f"doodad definitions: {mohd.num_doodad_defs} in {mohd.num_doodad_sets} set(s)")
    out.write(f"groups: {mohd.num_groups}    textures: {mohd.num_textures}    lights: {mohd.num_lights}    portals: {mohd.num_portals}    LODs: {mohd.num_lod}")

    ambient = simplify_irgba_short(mohd.amb_color, None, args)
    out.write(f"Ambient color: {ambient}")

    wmo_report_groupinfo(args, chunkmap["MOGI"], chunkmap["MOGN"], chunkmap["GFID"], out)
    wmo_report_materials(args, chunkmap["MOMT"], out)
    # wmo_report_doodad_sets(args, chunkmap["MODS"], chunkmap["MODI"], chunkmap["MODD"], out)


from dataclasses import dataclass


@dataclass
class MaterialInfo:
    terrain: Optional[int] = None
    flags: Optional[int] = None
    flags2: Optional[int] = None
    blend: Optional[int] = None
    shader: Optional[int] = None
    diff_color: Optional[int] = None
    sidn_color: Optional[int] = None
    color2: Optional[int] = None
    tex1: Optional[int] = None
    tex2: Optional[int] = None
    tex3: Optional[int] = None


def wmo_get_material_info(args, momt):
    mats = []
    for i, mat in enumerate(momt.materials):
        m = MaterialInfo()
        m.terrain = mat.foreign_key
        m.flags = simplify_flags(mat.flags, None, args)
        m.flags2 = mat.flags2  # FIXME: simplifier?
        m.blend = simplify_enum(mat.blend_mode, None, args)
        m.shader = simplify_shaderid_wmo(mat.shader_id, None, args)
        m.diff_color = simplify_irgba_short(mat.diff_color, None, args)
        m.sidn_color = simplify_irgba_short(mat.sidn_color, None, args)
        m.color2 = mat.color2  # diffuse?
        m.tex1 = simplify_fileid_short(mat.texture1_fdid, None, args)

        if mat.texture2_fdid > 0:
            m.tex2 = simplify_fileid_short(mat.texture2_fdid, None, args)

        if mat.texture3_fdid > 0:
            m.tex3 = simplify_fileid_short(mat.texture3_fdid, None, args)

        mats.append(m)

    return mats


def wmo_print_material_info(mats, index, out, indent=""):
    mat = mats[index]
    out.write(f"{indent}  MATERIAL index {index}     terrain: {mat.terrain} (needs db2?)")
    out.write(f"{indent}    flags: {mat.flags}")
    out.write(f"{indent}    blend mode: {mat.blend}")
    out.write(f"{indent}    shader: {mat.shader}")
    out.write(f"{indent}    diffuse: {mat.diff_color}    sidn: {mat.sidn_color}")
    out.write(f"{indent}    color2 (diffuse?): {mat.color2}    flags2: {mat.flags2}")
    out.write(f"{indent}    texture 1: {mat.tex1}")

    if mat.tex2 is not None:
        out.write(f"{indent}    texture 2: {mat.tex2}")

    if mat.tex3 is not None:
        out.write(f"{indent}    texture 3: {mat.tex3}")


def wmo_report_materials(args, momt, out):
    mats = wmo_get_material_info(args, momt)

    out.write("")
    out.write("Material Information:")
    for i, mat in enumerate(mats):
        wmo_print_material_info(mats, i, out)
        # out.write(f"  {i}    {mat}")
        # out.write(f"  MATERIAL index {i}     terrain: {mat.terrain} (needs db2?)")
        # out.write(f"    flags: {mat.flags}")
        # out.write(f"    blend mode: {mat.blend}    shader: {mat.shader}")
        # out.write(f"    diffuse: {mat.diff_color}    sidn: {mat.sidn_color}")
        # out.write(f"    color2 (diffuse?): {mat.color2}    flags2: {mat.flags2}")
        # out.write(f"    texture 1: {mat.tex1}")

        # if mat.tex2 is not None:
        #     out.write(f"    texture 2: {mat.tex2}")

        # if mat.tex3 is not None:
        #     out.write(f"    texture 3: {mat.tex3}")


def get_blob_indexed_name(blob, index):
    if index < 0:
        return "unnamed"

    strend = blob.index(b"\x00", index)
    if strend == index:
        return "unnamed"

    return blob[index:strend].decode("utf-8")


def get_group_names(mogi, mogn):
    group_names = []
    for i, group in enumerate(mogi.group_info):
        n = get_blob_indexed_name(mogn.group_names_blob, group.name_offset)
        group_names.append(n)

    return group_names


def get_group_name(mogn, index):
    return get_blob_indexed_name(mogn.group_names_blob, index)


def wmo_report_groupinfo(args, mogi, mogn, gfid, out):
    group_names = get_group_names(mogi, mogn)

    out.write("")
    out.write("Group Information:")
    for i, group in enumerate(mogi.group_info):
        out.write(f"  GROUP {i} ({group_names[i]})")
        flags = simplify_flags(group.flags, None, args)
        out.write(f"    flags: {flags}")
        fdid = simplify_fileid_short(gfid.group_fdids[i], None, args)
        out.write(f"    fdid (lod0): {fdid}")


def wmo_report_doodad_sets(args, mods, modi, modd, out):
    # sets = []
    # for i, dset in mods.doodad_sets:
    #     ds = {
    #         "dcount": dset.count,
    #         "dname": dset.name,
    #         "dstart": dset.start_index,
    #     }

    fdids = []
    for i, fdid in enumerate(modi.doodad_fdids):
        fdids.append(simplify_fileid(fdid, None, args))

    print("Doodad Information:")
    for i, dset in enumerate(mods.doodad_sets):
        print(f"  DOODAD SET {i} ({dset.name})")

        for dnum in range(dset.start_index, dset.count):
            ddef = modd.doodad_defs[dnum]
            print(f"    DOODAD {dnum}")
            flags = simplify_flags(ddef.flags, None, args)
            print(f"      flags: {flags}")
            print(f"      model: {fdids[ddef.name_index]}")

            pos = simplify_xyz(ddef.position, None, args)
            orient = simplify_wxyz(ddef.orientation, None, args)
            print(f"      pos: {pos}    scale: {ddef.scale:.4f}")
            print(f"      orientation: {orient}")

            color = simplify_irgba_short(ddef.color, None, args)
            print(f"      override color: {color}")


    # for i, ddef in enumerate(modd.doodad_defs):
    #     print(f"  DOODAD{i}")

    # print(len(modd.doodad_defs))


def wmo_nonroot(args, mogp, chunkmap, root, out):
    materials = wmo_get_material_info(args, root["MOMT"])
    # group_names = get_group_names(root["mogi"], root["mogn"])

    out.write("")
    # FIXME: probably needs DB2 lookup
    out.write(f"wmo group ID: {mogp.foreign_key} (needs db2?)")

    if "MDAL" in chunkmap:
        c = simplify_irgba_short(chunkmap["MDAL"].header_color_replacement, None, args)
        out.write(f"header color replacement: {c}")

    gn = get_group_name(root["MOGN"], mogp.group_name)
    gn_desc = get_group_name(root["MOGN"], mogp.descriptive_group_name)
    out.write(f"group name: {gn}    descriptive: {gn_desc}")

    flags = simplify_flags(mogp.flags, None, args)
    out.write(f"flags: {flags}")

    flags = simplify_flags(mogp.flags2, None, args)
    out.write(f"flags2: {flags}")

    out.write("")
    out.write(f"portal start index: {mogp.portal_start}    portal count: {mogp.portal_count}")

    b_trans = mogp.trans_batch_count
    b_intern = mogp.int_batch_count
    b_extern = mogp.ext_batch_count
    b_other = mogp.other_batch_count
    out.write(
        f"Batch coutns:  {b_trans} trans    {b_intern} internal    {b_extern} external    {b_other} other")

    fogs = ",".join([str(f) for f in mogp.fog_ids])
    out.write(f"Fog IDs: {fogs}    groupLiquid: {mogp.group_liquid} (??)")


    wmo_report_batches(args, materials, chunkmap["MOBA"], out)
    wmo_report_shadow_batches(args, materials, chunkmap["MOBS"], out)
    # wmo_report_doodads(args, chunkmap["MODR"], out)
    # wmo_report_bsp()    # FIXME: do we need this? Maybe?


    # mohd = chunkmap["MOHD"]
    # out.write(f"wmoID: {mohd.foreign_key} (needs db2?)")  # FIXME: probably needs DB2 lookup
    # flags = simplify_flags(mohd.flags, None, args)
    # out.write(f"flags: {flags}")
    # out.write(f"doodad definitions: {mohd.num_doodad_defs} in {mohd.num_doodad_sets} set(s)")
    # out.write(f"groups: {mohd.num_groups}    textures: {mohd.num_textures}    lights: {mohd.num_lights}    portals: {mohd.num_portals}    LODs: {mohd.num_lod}")

    # ambient = simplify_irgba_short(mohd.amb_color, None, args)
    # out.write(f"Ambient color: {ambient}")


    # wmo_report_groupinfo(args, chunkmap["MOGI"], chunkmap["MOGN"], chunkmap["GFID"], out)
    # wmo_report_materials(args, chunkmap["MOMT"], out)
    # wmo_report_doodad_sets(args, chunkmap["MODS"], chunkmap["MODI"], chunkmap["MODD"], out)


def wmo_report_batches(args, mats, moba, out):
    out.write("")
    out.write("Batch Information:")
    for i, bat in enumerate(moba.batches):
        # out.write(f"  {i}    {mat}")
        # from MOMT in root
        if bat.flags.use_material_id_large:
            material_id = bat.material_id_large
        else:
            material_id = bat.material_id

        out.write(f"  BATCH index {i}     material id: {material_id}")
        flags = simplify_flags(bat.flags, None, args)
        out.write(f"    flags: {flags}")

        # are first face and tris related? How do MOVI and MOVT relate?
        tri_count = int(bat.count / 3)
        vert_chunks = bat.max_index - bat.min_index + 1
        out.write(
            f"    first face: {bat.start_index}    vert chunks: {vert_chunks}    vert chunk start: {bat.min_index}    tris: {tri_count}")
        wmo_print_material_info(mats, material_id, out, "  ")


def wmo_report_shadow_batches(args, mats, mobs, out):
    out.write("")
    out.write("Shadow Batch Information:")

    for i, bat in enumerate(mobs.shadow_batches):
        # out.write(f"  {i}    {mat}")
        # from MOMT in root
        if bat.flags.use_material_id_large:
            material_id = bat.material_id_large
        else:
            material_id = bat.material_id
        out.write(f"  SHADOW BATCH index {i}     material id: {material_id}")
        flags = simplify_flags(bat.flags, None, args)
        out.write(f"    flags: {flags}")
        wmo_print_material_info(mats, material_id, out, "  ")


# FIXME: needs root wmo
def wmo_report_doodads(args, modr, out):
    out.write("")
    out.write("Doodad Information:    (FIXME: needs root)")

    for i, doodad in enumerate(modr.doodad_refs):
        out.write(f"  {doodad}")
