# unimplemented -- nothing known about this type
types:
    chunk_maoi:
        doc: "Height map indexes"
        doc-ref: https://wowdev.wiki/WDT#MAOI

        seq:
            - id: maois
              type: maoi_entry
              repeat: eos


    maoi_entry:
        seq:
            - id: tile_x
              type: u2
              doc: "MAOH entries are per ADT tile"
            - id: tile_y
              type: u2
            - id: offset
              type: u4
              doc: "offset in MAOH"
            - id: size
              type: u4
              doc: "always (17*17+16*16)*2"
