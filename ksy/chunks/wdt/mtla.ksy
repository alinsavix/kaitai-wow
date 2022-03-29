types:
    chunk_mlta:
        doc: "Map Data Unknown"
        doc-ref: https://wowdev.wiki/WDT#MLTA

        seq:
            - id: map_ltas
              type: map_lta
              repeat: eos

    map_lta:
        seq:
            - id: unknown1
              type: f4
            - id: unknown2
              type: f4
            - id: unknown3
              type: u4
              doc: "Always 1 or 2?"
