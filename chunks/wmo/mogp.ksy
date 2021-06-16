types:
    mogp_group_flags:
        seq:
            - id: has_bsp_tree
              type: b1  # 0x01
            - id: has_light_map
              type: b1  # 0x02
            - id: has_vertex_colors
              type: b1  # 0x04
            - id: smogroup_exterior
              type: b1  # 0x08
            - id: unused1
              type: b1  # 0x10
            - id: unused2
              type: b1  # 0x20
            - id: smogroup_exterior_lit
              type: b1  # 0x40
            - id: smogroup_unreachable
              type: b1  # 0x80

            - id: show_exterior_sky
              type: b1  # 0x0100
            - id: has_lights
              type: b1  # 0x0200
            - id: unknown_shadow
              type: b1  # 0x0400
            - id: has_doodads
              type: b1  # 0x0800
            - id: smogroup_liquidsurface
              type: b1  # 0x1000
            - id: smogroup_interior
              type: b1  # 0x2000
            - id: unused3
              type: b1  # 0x4000
            - id: query_mount_allowed
              type: b1  # 0x8000

            - id: smogroup_alwaysdraw
              type: b1  # 0x00010000
            - id: unused4
              type: b1  # 0x00020000
            - id: show_skybox
              type: b1  # 0x00040000
            - id: water_is_ocean
              type: b1  # 0x00080000
            - id: unknown1
              type: b1  # 0x00100000
            - id: is_mount_allowed  # FIXME: should this be "mount_is_allowed"?
              type: b1  # 0x00200000
            - id: unused5
              type: b1  # 0x00400000
            - id: unknown2
              type: b1  # 0x00800000

            - id: smogroup_cverts2
              type: b1  # 0x01000000
            - id: smogroup_tverts2
              type: b1  # 0x02000000
            - id: smogroup_antiportal
              type: b1  # 0x04000000
            - id: unknown3
              type: b1  # 0x08000000
            - id: unused6
              type: b1  # 0x10000000
            - id: smogroup_exterior_cull
              type: b1  # 0x20000000
            - id: smogroup_tverts3
              type: b1  # 0x40000000
            - id: unknown4
              type: b1  # 0x80000000


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
            - id: unknown1
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
            - id: foreign_key  # FIXME: still gotta figure this out
              type: u4
            - id: flags2
              type: u4
            - id: unused1
              type: u4

            # This will use the chunk definition from the wmo filetype
            - id: chunks
              type: wmo_chunk
              repeat: until
              repeat-until: _io.eof
