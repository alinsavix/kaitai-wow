
types:
    chunk_skb1:
        doc: "Skeleton Bone Data"
        doc-ref: https://wowdev.wiki/M2/.skel#SKB1
        seq:

            - id: bones
              type: m2array(m2array_types::m2compbone)
            - id: key_bone_lookup
              type: m2array(m2array_types::int16)
