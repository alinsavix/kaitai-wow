types:
    chunk_moba:
        doc: "Map Object Render Batches"
        doc-ref: https://wowdev.wiki/WMO#MOBA_chunk

        seq:
            - id: batches
              type: batch_list
              repeat: eos


    batch_list_flags:
        seq:
            - id: unknown1
              type: b1  # 0x01
            - id: use_material_id_large
              type: b1  # 0x02
            - id: unused1
              type: b6


    batch_list:  # FIXME: originally SMOBatch
        seq:
            - id: unknown1
              type: u1
              repeat: expr
              repeat-expr: 10
            - id: material_id_large
              type: u2
              doc: "used if use_material_id_large is set"
            - id: start_index
              type: u4
              doc: "index of first face index used in MOVI"
            - id: count
              type: u2
              doc: "number of MOVI indices used"
            - id: min_index
              type: u2
              doc: "index of the first vertex used in MOVT"
            - id: max_index
              type: u2
              doc: "index of the last vertex used (batch includes this one)"
            - id: flags
              type: batch_list_flags
            - id: material_id
              type: u1
