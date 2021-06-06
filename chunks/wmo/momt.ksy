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
            - id: shader
              type: u4
            - id: blend_mode
              type: u4
            - id: texture_1  # FIXME: Is this still an appropriate name?
              type: u4
            - id: sidn_color
              type: cimvector
            - id: frame_sidn_color
              type: cimvector

            - id: texture_2
              type: u4
            - id: diff_color
              type: cargb
            - id: foreign_key
              type: u4  # FIXME: Is this right?

            - id: texture_3
              type: u4
            - id: color_2
              type: u4
            - id: flags_2
              type: u4  # FIXME: should this use the flag type above?
            - id: runtime_data
              type: u4
              repeat: expr
              repeat-expr: 4
