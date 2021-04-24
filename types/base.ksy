types:
    # FIXME: Figure out if we implemented this right
    fixed16:
        seq:
            - id: value_raw
              type: s2
        instances:
            value:
                value: value_raw / 32767.0

    ubyte4:
        seq:
            - id: value
              type: u1
              repeat: expr
              repeat-expr: 4
