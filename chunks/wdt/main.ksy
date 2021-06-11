
types:
    chunk_main:
        doc: "Map tile table. Needs to contain 64x64 (4096) entries"
        doc-ref: https://wowdev.wiki/WDT#MAIN_chunk

        seq:
            - id: areas
              type: map_area_info
              repeat: eos

    # FIXME: doublecheck these vs. existing software
    map_area_flags:
        seq:
            - id: has_adt
              type: b1
            - id: all_water
              type: b1
            - id: loaded
              type: b1

    # FIXME: Original name SMAreaInfo
    map_area_info:
        seq:
            - id: flags
              type: map_area_flags
              size: 4
            - id: async_id
              type: u4
              doc: "only set during runtime"
