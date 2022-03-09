types:
    mcnk_flags:
        seq:
            - id: has_mcsh
              type: b1
            - id: impass
              type: b1
            - id: lq_river
              type: b1
            - id: lq_ocean
              type: b1
            - id: lq_magma
              type: b1
            - id: lq_slime
              type: b1
            - id: has_mccv
              type: b1
            - id: unknown1
              type: b1
            - id: unused1
              type: b7
            - id: do_not_fix_alpha_map
              type: b1
              doc: "fix alpha maps in MCAL and MCSH (4 bit alpha maps are 63*63 instead of 64*64"
            - id: high_res_holes
              type: b1
              doc: "Since ~5.3 WoW uses full 64-bit to store holes for each tile if this flag is set"
            - id: unused2
              type: b15

    chunk_mcnk:
        doc: "Map Tile Chunks. Always come in 256 individual chunks. Each chunk has 9x9 verts, with 8x8 additional verts in-between, plus several texture layers, normal vectors, shadow map, etc. Offsets to sub-chunks are relative to beginning of MCNK chunk, not MCNK chunk data."
        doc-ref: https://wowdev.wiki/ADT/v18#MCNK_chunk

        seq:
            - id: flags
              type: mcnk_flags
              size: 4
            - id: index_x
              type: u4
            - id: index_y
              type: u4
            - id: num_layers
              type: u4
              valid:
                  max: 4
            - id: num_doodad_refs
              type: u4
            - id: holes_high_res
              type: u8
              doc: "only used if flags.high_res_holes"

            - id: ofs_layer
              type: u4
            - id: ofs_refs
              type: u4
            - id: ofs_alpha
              type: u4
            - id: size_alpha
              type: u4
            - id: ofs_shadow
              type: u4
              doc: "only used if flags.has_mcsh"
            - id: size_shadow
              type: u4
            - id: area_id
              type: u4
              doc: "in alpha: both zone id and sub zone id, as uint16s"
            - id: num_map_obj_refs
              type: u4
            - id: holes_low_res
              type: u2
            - id: unknown1
              type: u2

            - id: really_low_quality_texturing_map
              type: b2
              repeat: expr
              repeat-expr: 8 * 8
              doc: "determines which detail doodads to show. Values are an array of two bit unsigned integers, identifying the layer."
            - id: no_effect_doodad
              type: b1
              repeat: expr
              repeat-expr: 8 * 8
              doc: "doodads disabled if set"
            - id: ofs_sound_emitters
              type: u4
            - id: num_sound_emitters
              type: u4
              doc: "set to 0 in client if ofs_sound_emitters not pointing to MCSE"
            - id: ofs_liquids
              type: u4
            - id: size_liquids
              type: u4
              doc: "8 when not used; only read if >8"
            - id: position
              type: c3vector
            - id: ofs_mccv
              type: u4
              doc: "only with flags.has_mccv"
            - id: ofs_mclv
              type: u4
            - id: unused1
              type: u4
# FIXME: Still needs a lot of sub-chunks and such
