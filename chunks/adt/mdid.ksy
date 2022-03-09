types:
    chunk_mdid:
        doc: "Map Diffuse Texture IDs"
        doc-ref: https://wowdev.wiki/ADT/v18#MDID
        seq:
            - id: map_diffuse_fdids
              type: u4
              repeat: eos
              simplifier_each: simplify_fileid
