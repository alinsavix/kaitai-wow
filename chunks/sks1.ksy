types:
    chunk_sks1:
        doc: "Skeleton Sequence Data"
        doc-ref: https://wowdev.wiki/M2/.skel#SKS1
        seq:
            - id: global_loops
              type: m2array<m2loop>
            - id: sequences
              type: m2array<m2sequence>
            - id: sequence_lookups
              type: m2array<s2>
            - id: unknown1
              type: u1
              repeat: expr
              repeat-expr: 8
              doc: "May not be used"
