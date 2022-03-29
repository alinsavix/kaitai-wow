types:
    chunk_mopy:
        doc: "Map Object Poly List - Material info for triangles, two bytes per triangle"
        doc-ref: https://wowdev.wiki/WMO#MOPY_chunk

        seq:
            - id: polys
              type: poly_list
              repeat: eos

    poly_list_flags:
        seq:
            - id: unknown1
              type: b1  # 0x01
            - id: no_cam_collide
              type: b1  # 0x02
            - id: detail
              type: b1  # 0x04
            - id: collision
              type: b1  # 0x08
              doc: "No water ripples. May do more. Use for ghost material tris"
            - id: hint
              type: b1  # 0x10
            - id: render
              type: b1  # 0x20
            - id: unknown2
              type: b1  # 0x40
            - id: collide_hit
              type: b1  # 0x80

    poly_list:  # FIXME: originally SMOPoly
        seq:
            - id: flags
              type: poly_list_flags
            - id: material_id
              type: u1
              doc: "index into MOMT, 0xff for collision faces"
