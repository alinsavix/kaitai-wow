types:
    m2texturetransform:
        seq:
            - id: translation
              type: m2track(m2track_types::c3vector)
            - id: rotation
              type: m2track(m2track_types::c4quaternion)
            - id: scaling
              type: m2track(m2track_types::c3vector)
