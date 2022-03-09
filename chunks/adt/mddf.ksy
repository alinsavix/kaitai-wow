types:
    chunk_mddf:
        doc: "Map Doodad Definitions - Documentation is extensive, please see URL"
        doc-ref: https://wowdev.wiki/ADT/v18#MMDF_chunk

        seq:
            - id: map_doodad_defs_list
              type: map_doodad_def
              repeat: eos
              doc: "Map doodad definitions"


    mddf_flags:
        seq:
            - id: biodome
              type: b1  # 0x01
            - id: shrubbery
              type: b1  # 0x02
            - id: unknown1
              type: b1  # 0x04
            - id: unknown2
              type: b1  # 0x08
            - id: unused1
              type: b1  # 0x10
              simplifier: simplify_remove
            - id: liquid_known
              type: b1  # 0x20
            - id: entry_is_fdid
              type: b1  # 0x40
              doc: "name_id is a fdid to load instead of MMID reference"
            - id: unused2
              type: b1  # 0x80
              simplifier: simplify_remove
            - id: unknown3
              type: b1  # 0x0100

    map_doodad_def:
        seq:
            - id: model_fdid
              type: u4
              doc: "FDID of doodad model (unless `mddf_entry_is_fddid` is unset, which should no longer be the case)"
              simplifier: simplify_fileid
            - id: unique_id
              type: u4
              doc: "Unique identifier for ADT"
            - id: position
              type: c3vector
              doc: "Relative to a corner of the map. Subtract 17066 from the non-veritical values and you should start to see something that makes sense. You'll then probably have to negate one of the non-veritical values in whatever coordinate system"
            - id: rotation
              type: c3vector
              doc: "in degrees. This is not the same coordinate system orientation as the ADT itself!"
            - id: scale_raw
              type: u2
              doc: "default scale is 1024 == 1.0f"
            - id: flags
              type: mddf_flags
              size: 2

        instances:
            scale:
                value: scale_raw / 1024.0
