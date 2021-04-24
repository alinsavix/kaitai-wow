types:
    m2camera:
        seq:
            - id: type
              type: u4
              doc: "0 portait, 1 characterinfo, -1 otherwise"
            - id: far_clip
              type: f4
            - id: near_clip
              type: f4
            - id: positions
              type: m2track(m2track_types::todo) # FIXME: M2Track<M2SplineKey<C3Vector>>
            - id: position_base
              type: c3vector
            - id: target_position
              type: m2track(m2track_types::todo) # FIXME: M2Track<M2SplineKey<C3Vector>>
            - id: target_position_base
              type: c3vector
            - id: roll
              type: m2track(m2track_types::todo) # FIXME: M2Track<M2SplineKey<float>>
              doc: "0 to 2*pi"
            - id: fov
              type: m2track(m2track_types::todo) # FIXME: M2Track<M2SplineKey<float>>
              doc: "diagonal FoV in radians"
