types:
    m2color:
        seq:
            - id: color
              # FIXME: this ends up simplifying as xyz instead of rgb
              type: m2track(m2track_types::c3vector)
            - id: alpha
              type: m2track(m2track_types::fixed16)
