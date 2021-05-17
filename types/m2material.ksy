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
    m2material_flags:
        seq:
            - id: unlit
              type: b1 # 0x01
            - id: unfogged
              type: b1 # 0x02
            - id: twosided
              type: b1 # 0x04
              doc: "two-sided, no backface culling"
            - id: depthtest
              type: b1 # 0x08
            - id: depthwrite
              type: b1 # 0x10
            - id: unused1
              type: b1 # 0x20
            - id: shadowbatch1
              type: b1 # 0x40
            - id: shadowbatch2
              type: b1 # 0x80
            - id: unused2
              type: b1 # 0x100
            - id: unused3
              type: b1 # 0x200
            - id: unknown1 # "seen in WoD"
              type: b1 # 0x400
            - id: preventalpha
              type: b1 # 0x800
              doc: "prevent alpha for custom elements; use fully opaque or transparent"

    m2material:
        seq:
            - id: flags
              size: 2
              type: m2material_flags
            - id: blending_mode
              type: u2
              enum: m2material_blendmodes
