types:
    chunk_mhid:
        doc: "Map Height Texture IDs"
        doc-ref: https://wowdev.wiki/ADT/v18#MHID
        seq:
            - id: map_height_fdids
              type: u4
              repeat: eos
              simplifier_each: simplify_fileid
