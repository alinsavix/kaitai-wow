types:
    mogp_group_flags:
        seq:
            - id: has_bsp_tree
              type: b1  # 0x01
            - id: has_light_map
              type: b1  # 0x02
              doc: "subtract mohd.color in mocv fixing"
            - id: has_vertex_colors
              type: b1  # 0x04
              doc: "has MOCV chunk"
            - id: exterior
              type: b1  # 0x08
            - id: unused1
              type: b1  # 0x10
            - id: unused2
              type: b1  # 0x20
            - id: exterior_lit
              type: b1  # 0x40
            - id: unreachable
              type: b1  # 0x80

            - id: show_exterior_skybox
              type: b1  # 0x0100
            - id: has_lights
              type: b1  # 0x0200
              doc: "has MOLR chunk"
            - id: l_o_d
              type: b1  # 0x0400
              doc: "Also load for LoD != 0 (_lod* groups)"
            - id: has_doodads
              type: b1  # 0x0800
              doc: "Has doodads (MODR chunk)"
            - id: liquidsurface
              type: b1  # 0x1000
              doc: "Has water (MLIQ chunk)"
            - id: interior
              type: b1  # 0x2000
              doc: "Indoors"
            - id: unused3
              type: b1  # 0x4000
            - id: unused4
              type: b1  # 0x8000

            - id: alwaysdraw
              type: b1  # 0x00010000
              doc: "wowdev.wiki: clear 0x08 after CMapObjGroup::Create() in MOGP and MOGI"
            - id: has_mori
              type: b1  # 0x00020000
              doc: "Has MORI and MORB chunks"
            - id: show_skybox
              type: b1  # 0x00040000
              doc: "Automatically unset if MOSB not present"
            - id: water_is_ocean
              type: b1  # 0x00080000
              doc: "LiquidType related, see MLIQ"
            - id: unknown1
              type: b1  # 0x00100000
            - id: is_mount_allowed  # FIXME: should this be "mount_is_allowed"?
              type: b1  # 0x00200000
            - id: unused5
              type: b1  # 0x00400000
            - id: unused6
              type: b1  # 0x00800000

            - id: cverts2
              type: b1  # 0x01000000
              doc: "Has two MOCV chunks - don't run FixColorVertexAlpha on these!"
            - id: tverts2
              type: b1  # 0x02000000
              doc: "Has two MOTV chunks"
            - id: antiportal
              type: b1  # 0x04000000
              doc: "Antiportal; requires intBatchCount == 0, extBatchCount == 0, UNREACHABLE"
            - id: unknown3
              type: b1  # 0x08000000
              doc: "maybe don't render batches, but still render doodads?"
            - id: unused7
              type: b1  # 0x10000000
            - id: exterior_cull
              type: b1  # 0x20000000
            - id: tverts3
              type: b1  # 0x40000000
              doc: "has three MOTV chunks"
            - id: unknown4
              type: b1  # 0x80000000
              doc: "unknown, seen in world/wmo/kultiras/human/8hu_warfronts_armory_v2_000.wmo"


    mogp_group_flags2:
        seq:
            - id: can_cut_terrain
              type: b1  # 0x01
            - id: unused1
              type: b31


    # FIXME: This will always be the chunk that starts non-root wmo files,
    # can we make it any less painful to work with, nesting-wise?
    chunk_mogp:
        doc: "Map Object Group Definition"
        doc-ref: https://wowdev.wiki/WMO#MOGP_chunk

        seq:
            - id: group_name
              type: u4
              doc: "Offset into MOGN"
            - id: descriptive_group_name
              type: u4
              doc: "Offset into MOGN"
            - id: flags
              type: mogp_group_flags
            - id: bounding_box
              type: caabox
              doc: "Same as corresponding MOGI entry"
            - id: portal_start
              type: u2
              doc: "Offset into MOPR"
            - id: portal_count
              type: u2
              doc: "number of MOPR items used after portalStart"
            - id: trans_batch_count
              type: u2
            - id: int_batch_count
              type: u2
            - id: ext_batch_count
              type: u2
            - id: other_batch_count
              type: u2
              doc: "Possibly padding, possibly data"
            - id: fog_ids
              type: u1
              repeat: expr
              repeat-expr: 4
              doc: "IDs in MFOG chunk"
            - id: group_liquid
              type: u4
              doc: "See MLIQ chunk"
            - id: foreign_key  # FIXME: still gotta figure this out  # name: wmo_group_id?
              type: u4
            - id: flags2
              type: mogp_group_flags2
            - id: unused1
              type: u4

            # This will use the chunk definition from the wmo filetype
            - id: chunks
              type: wmo_chunk
              repeat: until
              repeat-until: _io.eof
