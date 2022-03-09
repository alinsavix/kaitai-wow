types:
    mhdr_flags:
        seq:
            - id: has_mfbo
              type: b1  # 0x01
            - id: northrend # 0x02
              type: b1
              doc: "set for some Northrend areas"


    chunk_mhdr:
        doc: "Map Tile Header"
        doc-ref: https://wowdev.wiki/ADT/v18#MHDR_chunk

        seq:
            - id: flags
              type: mhdr_flags
              size: 4
            - id: ofs_mcin
              type: u4
            - id: ofs_mtex
              type: u4
            - id: ofs_mmdx
              type: u4
            - id: ofs_mmid
              type: u4
            - id: ofs_mwmo
              type: u4
            - id: ofs_mwid
              type: u4
            - id: ofs_mddf
              type: u4
            - id: ofs_modf
              type: u4
            - id: ofs_mfbo
              type: u4
            - id: ofs_mh2o
              type: u4
            - id: ofs_mtxf
              type: u4
            - id: mamp_value
              type: u1
            - id: padding
              type: u1
              repeat: expr
              repeat-expr: 3
            - id: unused
              type: u4
              repeat: expr
              repeat-expr: 3
