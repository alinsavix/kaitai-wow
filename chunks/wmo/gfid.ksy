types:
    chunk_gfid:
        doc: "Map Object Group File Data IDs"
        doc-ref: https://wowdev.wiki/WMO#GFID_chunk

        seq:
            - id: group_fdids
              type: u4
              repeat: eos
              simplifier_each: simplify_fileid
