types:
    m2batch_flags:
        seq:
            # not sure of specifics of most of these
            - id: materials_invert
              type: b1  # 0x01
            - id: transform
              type: b1  # 0x02
            - id: projected_texture
              type: b1  # 0x04
            - id: unknown1
              type: b1  # 0x08
            - id: batch_compatible
              type: b1  # 0x10
            - id: projected_texture2
              type: b1  # 0x20
            - id: transparency_no_multiply
              type: b1  # 0x40
            - id: unknown2
              type: b1  # 0x80

    # FIXME: These fields could use *much* better animations
    m2batch:
        doc: "Texture Units"
        doc-ref: https://wowdev.wiki/M2/.skin#Texture_units
        seq:
            - id: flags
              type: m2batch_flags
              doc: |
                Usually 16 for static textures, and 0 for animated textures.

                &0x1: materials invert something
                &0x2: transform
                &0x4: projected texture
                &0x10: something batch compatible
                &0x20: projected texture?
                &0x40: possibly: do not multiply transparency by texture weight transparency to get final transparency value(?)

            - id: priority_plane
              type: s1
            - id: shader_id
              type: u2
              simplifier: simplify_shaderid_m2
            - id: skin_section_index
              type: u2
              doc: "Duplicate entry of a submesh (?)"
            - id: geoset_index
              type: u2
              doc: |
                    Apply to geoset index, previously. Might be a second flags field now.
                    Known possible flags:

                    0x02 - Projected texture
                    0x08 - EDGF chunk from m2 is mandatory

            - id: color_index
              type: s2
              doc: "Index color out of M2.colors"
            - id: material_index
              type: u2
              doc: "Index material out of M2.materials"
            - id: material_layer
              type: u2
            - id: texture_count
              type: u2
              doc: "Number of textures, to help determine shader"
            - id: texture_combo_index
              type: u2
              doc: "Index into texture lookup table"
            - id: texture_coord_combo_index
              type: u2
              doc: "Index into texture unit lookup table"
            - id: texture_weight_combo_index
              type: u2
              doc: "Index into transparency lookup table"
            - id: texture_transform_combo_index
              type: u2
              doc: "Index into UVAnimation lookup table"
