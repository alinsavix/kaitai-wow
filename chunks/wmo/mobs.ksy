types:
    chunk_mobs:
        doc: "Map Object Shadow Batches"
        doc-ref: https://wowdev.wiki/WMO#MOBS_chunk

        seq:
            - id: shadow_batches
              type: shadow_batch_list
              repeat: eos

    shadow_batch_list_flags:
        seq:
            - id: unknown1
              type: b1  # 0x01
            - id: use_material_id_large
              type: b1  # 0x02
            - id: unused1
              type: b6

    shadow_batch_list:
        seq:
            - id: unknown1
              type: u1
              repeat: expr
              repeat-expr: 10
            - id: material_id_large
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
            - id: flags
              type: shadow_batch_list_flags
            - id: material_id
              type: u1
              doc: "Index into MOMT"
