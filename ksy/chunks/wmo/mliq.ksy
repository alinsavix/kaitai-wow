types:
    chunk_mliq:
        doc: "Map Liquid Information"
        doc-ref: https://wowdev.wiki/WMO#MLIQ_chunk

        seq:
            - id: liquid_verts
              type: c2ivector
              doc: "number of vertices (x,y)"
            - id: liquid_tiles
              type: c2ivector
              doc: "number of tiles (ntiles = nverts - 1)"
            - id: lquid_corner
              type: c3vector
              doc: "base coordinates for X and Y"
            - id: liquid_material_id
              type: u2
              doc: "material ID (index into MOMT)"
            - id: vertex_list
              type: mliq_vertex
              repeat: expr
              repeat-expr: liquid_verts.x * liquid_verts.y
            - id: tile_list
              type: mliq_tile
              repeat: expr
              repeat-expr: liquid_tiles.x * liquid_tiles.y


    # FIXME: also has a 'magma' version as union
    mliq_vertex:
        seq:
            - id: flow1
              type: u1
            - id: flow2
              type: u1
            - id: flow1pct
              type: u1
            - id: filler
              type: u1
            - id: height
              type: f4

    mliq_tile:
        seq:
            - id: liquid
              type: b6
            - id: fishable
              type: b1
            - id: shared
              type: b1
