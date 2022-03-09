types:
    chunk_mwid:
        doc: "Map WMO Model Filename Offsets"
        doc-ref: https://wowdev.wiki/ADT/v18#MWID_chunk
        seq:
            - id: map_wmo_name_offset
              type: u4
              repeat: eos
              doc: "Name offset inside MWMO chunk"
