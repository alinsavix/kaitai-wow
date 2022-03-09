types:
    chunk_mmid:
        doc: "Map M2 Model Filename Offsets"
        doc-ref: https://wowdev.wiki/ADT/v18#MMID_chunk
        seq:
            - id: map_model_name_offset
              type: u4
              repeat: eos
              doc: "Name offset inside MMDX chunk"
