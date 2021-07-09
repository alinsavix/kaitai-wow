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

types:
    momt_flags:
        seq:
            - id: unlit
              type: b1  # 0x01
            - id: unfogged
              type: b1  # 0x02
            - id: unculled
              type: b1  # 0x04
            - id: extlight
              type: b1  # 0x08
            - id: sidn
              type: b1  # 0x10
            - id: window
              type: b1  # 0x20
            - id: clamp_s
              type: b1  # 0x40
            - id: clamp_t
              type: b1  # 0x80
            - id: flag_0x100
              type: b1  # 0x0100
            - id: unused1
              type: b23  # 0x0100 to 0x80000000


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
            - id: blend_mode
              type: u4
            - id: texture1_file_data_id
              type: u4
            - id: sidn_color
              type: cimvector
            - id: frame_sidn_color
              type: cimvector

            - id: texture2_file_data_id
              type: u4
            - id: diff_color
              type: cargb
            - id: foreign_key
              type: u4  # FIXME: Is this right?

            - id: texture3_file_data_id
              type: u4
            - id: color2
              type: u4
            - id: flags2
              type: u4  # FIXME: should this use the flag type above?
            - id: runtime_data
              type: u4
              repeat: expr
              repeat-expr: 4
