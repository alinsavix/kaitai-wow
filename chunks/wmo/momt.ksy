enums:
    momt_shaders:
        0:
            id: diffuse
        1:
            id: specular
        2:
            id: metal
        3:
            id: env
        4:
            id: opaque
        5:
            id: env_metal
        6:
            id: two_layer_diffuse
        7:
            id: two_layer_env_metal
        8:
            id: two_layer_terrain
            doc: "automatically adds _s in the filename of second texture"
        9:
            id: diffuse_emissive
        10:
            id: water_window
            doc: "FFX instead of normal material. SH_WATERWINDOW automatically generates MOTA"
        11:
            id: masked_env_metal
        12:
            id: env_metal_emissive
        13:
            id: two_layer_diffuse_opaque
        14:
            id: submarine_window
            doc: "FFX instead of normal material. SH_SUBMARINEWINDOW automatically generates MOTA"
        15:
            id: two_layer_diffuse_emissive
        16:
            id: diffuse_terrain
            doc: "SH_DIFFUSE_TERRAIN -- blend material -- used for blending WMO with terrain (dynamic blend batches)"
        17:
            id: additive_masked_env_metal
        18:
            id: two_layer_diffuse_mod_2x
        19:
            id: two_layer_diffuse_mod2x_n_a
        20:
            id: two_layer_diffuse_alpha
        21:
            id: lod
        22:
            id: parallax
            doc: "SH_PARALLAX_ICE"


    momt_blend_modes:
        0:
            id: opaque
        1:
            id: alpha_key
        2:
            id: alpha
        3:
            id: add
        4:
            id: mod
        5:
            id: mod2x
        6:
            id: mod_add
        7:
            id: inv_src_alpha_add
        8:
            id: inv_src_alpha_opaque
        9:
            id: src_alpha_opaque
        10:
            id: no_alpha_add
        11:
            id: constant_alpha
        12:
            id: screen
        13:
            id: blend_add

types:
    momt_flags:
        seq:
            - id: unlit
              type: b1  # 0x01
              doc: "disable lighting logic (can still use vertex colors)"
            - id: unfogged
              type: b1  # 0x02
              doc: "disable fog shading (rarely used)"
            - id: unculled
              type: b1  # 0x04
              doc: "two sided"
            - id: extlight
              type: b1  # 0x08
              doc: "darkened (internal faces of windows are flagged)"
            - id: sidn
              type: b1  # 0x10
              doc: "self-illuminated day/night (bright at night, unshaded)"
            - id: window
              type: b1  # 0x20
              doc: "(something lighting related)"
            - id: clamp_s
              type: b1  # 0x40
              doc: "texture clamp S"
            - id: clamp_t
              type: b1  # 0x80
              doc: "texture clamp T"
            - id: flag_0x100
              type: b1  # 0x0100
            - id: unused1
              type: b23  # 0x0100 to 0x80000000
              simplifier: simplify_remove


    chunk_momt:
        doc: "Map Object Materials"
        doc-ref: https://wowdev.wiki/WMO#MOMT_chunk
        seq:
            - id: materials
              type: material_list
              repeat: eos

    # FIXME: import tables for shader types
    material_list:
        seq:
            - id: flags
              type: momt_flags
            - id: shader_id
              type: u4
              enum: momt_shaders
              simplifier: simplify_shaderid_wmo
            - id: blend_mode
              type: u4
              enum: momt_blend_modes
              simplifier: simplify_enum
            - id: texture1_fdid
              type: u4
            - id: sidn_color
              type: cimvector
              doc: "Self-illuminated day/night"
            - id: frame_sidn_color
              type: cimvector
              doc: "set at runtime"

            - id: texture2_fdid
              type: u4
            - id: diff_color
              type: cargb
            - id: foreign_key
              type: u4  # FIXME: Is this right?

            - id: texture3_fdid
              type: u4
            - id: color2
              type: u4
            - id: flags2
              type: u4  # FIXME: should this use the flag type above?
            - id: runtime_data
              type: u4
              repeat: expr
              repeat-expr: 4
              simplifier: simplify_remove
