types:
    chunk_mopr:
        doc: "Map Object Portal References"
        doc-ref: https://wowdev.wiki/WMO#MOPR_chunk

        seq:
            - id: portal_references
              type: portal_reference_list
              repeat: eos

    portal_reference_list:  # FIXME: originally SMOPortalRef
        seq:
            - id: portal_index  # index into MOPT
              type: u2
            - id: group_index
              type: u2
            - id: side  # positive or negative
              type: s2
            - id: unused1  # "filler"
              type: u2
              simplifier: simplify_remove
