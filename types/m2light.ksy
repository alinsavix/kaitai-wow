types:
    m2light:
        seq:
            - id: type
              type: u2 # FIXME: actually an enum
            - id: bone
              type: s2
              doc: "-1 if not attached to a bone"
            - id: position
              type: c3vector
              doc: "relative to bone"
            - id: ambient_color
              type: m2track(m2track_types::c3vector)
            - id: ambient_intensity
              type: m2track(m2track_types::float)
              doc: "defaults to 1.0"
            - id: diffuse_color
              type: m2track(m2track_types::c3vector)
            - id: diffuse_intensity
              type: m2track(m2track_types::float)
              doc: "defaults to 1.0"
            - id: attenuation_start
              type: m2track(m2track_types::float)
            - id: attenuation_end
              type: m2track(m2track_types::float)
            - id: visibility
              type: m2track(m2track_types::uint8)
