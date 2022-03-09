types:
    chunk_mh2o:
        doc: "Map Tile Liquids"
        doc-ref: https://wowdev.wiki/ADT/v18#MH2O_chunk_.28WotLK.2B.29

        seq:
            - id: liquid_chunks
              type: mh2o_header
              repeat: expr
              repeat-expr: 16 * 16

    mh2o_header:
        seq:
            - id: ofs_instances
              type: u4
              doc: "points to SMLiquidInstance[layer_count]"

            # FIXME: Probably need special handling
            - id: num_layers
              type: u4
              doc: "0 if the chunk has no liquids. If > 1, the offsets will point to arrays"

            # FIXME: Do we need to special-case 0?
            - id: ofs_attributes
              type: u4
              doc: "points to mh2o_chunk_attributes, can be ommitted for all-0"

        instances:
            attributes:
                type: mh2o_attributes
                pos: ofs_attributes
            instances:
                type: mh2o_instances
                pos: ofs_instances
                repeat: expr
                repeat-expr: num_layers

    mh2o_attributes:
        seq:
            - id: fishable
              type: u8
              doc: "8x8 bitmask for fishability"
            - id: deep
              type: u8
              doc: "8x8 bitmask for fatigue area"

    mh2o_instances:
        doc: |
            For RegisterLiquidObject:

            if LO < 42 || !exists(LO):
                if LM == 2:
                if LM == 1:
                    if LT != 2 && LT != 14: usePlanarMapLiquidObject
                    if LT == 17: usePlanarMapLiquidObjectNoSky
                    else: usePlanarMapLiquidObject
                if LM == 0:
                    if LM == 5 && (LT == 350 || LT == 412): usePlanarMapLiquidObjectNoSky
                    else: usePlanarMapLiquidObject

            if LO == 42 || LT == 14: oceanLiquidObject

            else: LO is in DB, take that

        seq:
            - id: foreign_key
              type: u2
              doc: "Foreign key to LiquidTypeRec dbc"
            - id: min_height_level
              type: f4
              doc: "Used as height if no heightmap given and culling"
            - id: max_height_level
              type: f4
              doc: "WoD and later ignores and assumes both are 0 for LVF=2"

            # Next four only if liquid_object_or_lvf <= 41, otherwise assumed to be (0, 0, 8, 8)
            - id: x_offset
              type: u1
              doc: "X offset of the liquid square (0-7)"
            - id: y_offset
              type: u1
              doc: "Y offset of the liquid square (0-7)"
            - id: width
              type: u1
              doc: "width of the liquid square (1-8)"
            - id: height
              type: u1
              doc: "height of the liquid square (1-8)"

            - id: ofs_exists_bitmap
              type: u4
              doc: "Not all tiles have to exist. Can be 0 for all-exst"
            - id: ofs_vertex_data
              type: u4
              doc: "Actual data format defined by LiquidMaterialRec::m_LVF via LiquidTypeRec::m_materialID. If offset=0 and liquidType=2, then LVF=2 (i.e. ocean bits)"
