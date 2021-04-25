enums:
    m2material_blendmodes:
        0: m2blend_opaque
        1: m2blend_alpha_key
        2: m2blend_alpha
        3: m2blend_no_alpha_add
        4: m2blend_add
        5: m2blend_mod
        6: m2blend_mod2x
        7: m2blend_blendadd

types:
    m2material:
        seq:
            # "flags" field, uint16
            - id: flags_unlit
              type: b1  # 0x01
            - id: flags_unfogged
              type: b1  # 0x02
            - id: flags_twosided
              type: b1  # 0x04
              doc: "two-sided, no backface culling"
            - id: flags_depthtest
              type: b1  # 0x08
            - id: flags_depthwrite
              type: b1  # 0x10
            - id: flags_unused1
              type: b1  # 0x20
            - id: flags_shadowbatch1
              type: b1  # 0x40
            - id: flags_shadowbatch2
              type: b1  # 0x80
            - id: flags_unused2
              type: b1  # 0x100
            - id: flags_unused3
              type: b1  # 0x200
            - id: flags_unknown1  # "seen in WoD"
              type: b1  # 0x400
            - id: flags_preventalpha
              type: b1  # 0x800
              doc: "prevent alpha for custom elements; use fully opaque or transparent"

            - id: blending_mode
              type: u2
              enum: m2material_blendmodes
