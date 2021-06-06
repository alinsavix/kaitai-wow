types:
    chunk_mogi:
        doc: "Map Object Group Information"
        doc-ref: https://wowdev.wiki/WMO#MOGI_chunk

        seq:
            - id: group_info
              type: group_info_list
              repeat: eos

    group_info_list:
        seq:
            - id: flags
              type: u4  # FIXME: expand flags per MOGP
            - id: bounding_box
              type: caabox
            - id: name_offset
              type: s4
              doc: "Name in MOGN chunk (-1 for no name)"
