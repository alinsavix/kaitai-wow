types:
    chunk_mobs:
        doc: "Map Object Shadow Batches"
        doc-ref: https://wowdev.wiki/WMO#MOBS_chunk

        seq:
            - id: shadow_batches
              type: shadow_batch_list
              repeat: eos

    shadow_batch_list:
        seq:
            - id: unknown1
              type: u1
              repeat: expr
              repeat-expr: 10
            - id: material_id_big
              type: u2
              doc: "Index into MOMT"
            - id: field2
              type: u4
            - id: field6
              type: u2
            - id: unknown2
              type: u1
              repeat: expr
              repeat-expr: 4
            - id: flag_thing
              type: u1
            - id: material_id_small
              type: u1
              doc: "Index into MOMT"
