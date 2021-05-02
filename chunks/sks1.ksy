
types:
    chunk_sks1:
        doc: "Skeleton Sequence Data"
        doc-ref: https://wowdev.wiki/M2/.skel#SKS1
        seq:
            - id: global_loops
              type: m2array(m2array_types::m2loop)
            - id: sequences
              type: m2array(m2array_types::m2sequence)
            - id: sequence_lookups
              type: m2array(m2array_types::int16)
            - id: unknown1
              type: u1
              repeat: expr
              repeat-expr: 8
              doc: "May not be used"
