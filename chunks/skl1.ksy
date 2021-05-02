
types:
    chunk_skl1:
        doc: "Skeleton Data"
        doc-ref: https://wowdev.wiki/M2/.skel#SKL1
        seq:
            - id: flags
              type: u4
              doc: "Flags unknown, possibly always 0x100 currently"
            - id: name
              type: m2array_str
            - id: unknown1
              type: u1
              repeat: expr
              repeat-expr: 4
              doc: "Possibly Unused"
