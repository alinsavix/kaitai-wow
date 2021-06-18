types:
    chunk_afid:
        doc: "Animation File IDs"
        doc-ref: https://wowdev.wiki/M2#AFID
        seq:
            - id: anim_file_ids
              type: anim_file_id
              repeat: eos

    anim_file_id:
        seq:
            - id: anim_id
              type: u2
              enum: anim_names
            - id: sub_anim_id
              type: u2
            - id: file_data_id
              type: u4
              doc: "Might be 0 for 'none'"
