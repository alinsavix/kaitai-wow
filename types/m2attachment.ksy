types:
    m2attachment:
        seq:
            - id: id
              type: u4
            - id: bone
              type: u2
            - id: unknown1
              type: u2
            - id: position
              type: c3vector
            - id: animate_attached
              type: m2track(m2track_types::uint8)
