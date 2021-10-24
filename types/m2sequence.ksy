types:
    m2sequence_flags:
        seq:
            - id: set_0x80
              type: b1  # 0x01
              doc: "sets 0x80 flag when loaded"
            - id: unknown1
              type: b1  # 0x02
            - id: unknown2
              type: b1  # 0x04
            - id: unknown3
              type: b1  # 0x08
            - id: runtime1
              type: b1  # 0x10
              doc: "apaprently set during runtime for all entries of a loaded sequence (including aliases)"
            - id: is_primary
              type: b1  # 0x20
              doc: "if set, animation data is in .m2 file, else in .anim file"
            - id: is_alias
              type: b1  # 0x40
              doc: "to find data, client skips these by following aliasNext until an animation without this flag is found"
            - id: is_blended
              type: b1  # 0x80
              doc: "if either side of a transition has this flag, lerp between end->start states, unless end==start by comparing bone values"

            - id: sequence_stored_in_model
              type: b1  # 0x0100
              doc: "sequence stored in model(?)"
            - id: blendtime_range
              type: b1  # 0x0200
              doc: "signals that blendTime field is really blendTimeIn and blendTimeOut"
            - id: unknown4
              type: b1  # 0x0400
            - id: unknown5
              type: b1  # 0x0800
              doc: "seen in Legion 24500 models"
            - id: unused1
              type: b1  # 0x1000
            - id: unused2
              type: b1  # 0x2000
            - id: unused3
              type: b1  # 0x4000
            - id: unused4
              type: b1  # 0x8000


    m2sequence:
        seq:
            - id: id
              type: u2
              enum: anim_names
            - id: variation_index
              type: u2
            - id: duration
              type: u4
            - id: movespeed
              type: f4
            - id: flags
              type: m2sequence_flags
              size: 4
            - id: frequency
              type: s2
            - id: padding
              type: u2
            - id: replay
              type: m2range
            - id: blend_time_in
              type: u2
            - id: blend_time_out
              type: u2
            - id: bounds
              type: m2bounds
            - id: variation_next
              -orig-id: variationNext
              type: s2
            - id: alias_next
              -orig-id: aliasNext
              type: u2
