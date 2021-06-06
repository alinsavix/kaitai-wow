enums:
    # FIXME: is this even used?
    modd_efogs:
        0: fog
        1: uwfog
        2: num_fogs

types:
    chunk_mfog:
        doc: "Map Object Fog Information"
        doc-ref: https://wowdev.wiki/WMO#MFOG_chunk

        seq:
            - id: fogs
              type: fogs_info
              repeat: eos

    fog_info_flags:
        seq:
            - id: infinite_radius
              type: b1
            - id: unused1  # unused as of 7.0.1.20994
              type: b3
            - id: unk_0x10
              type: b1
            - id: unused2  # unused as of 7.0.1.20994
              type: b27

    fogs_info:  # FIXME: originally SMOFog
        seq:
            - id: flags
              type: fog_info_flags
            - id: pos
              type: c3vector
            - id: smaller_radius
              type: f4
            - id: larger_radius
              type: f4
            - id: fogs
              type: fog_info
              repeat: expr
              repeat-expr: 2

    fog_info:
        seq:
            - id: end
              type: f4
            - id: start_scalar
              type: f4
            - id: color
              type: cimvector
