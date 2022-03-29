types:
    m2bounds:
        seq:
            - id: extent
              type: caabox
            - id: radius
              type: f4

    m2range:
        seq:
            - id: minimum
              type: u4
            - id: maximum
              type: u4

    m2box:
        seq:
            - id: model_rotation_speed_min
              type: c3vector
            - id: model_rotation_speed_max
              type: c3vector
