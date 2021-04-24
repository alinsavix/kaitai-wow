enums:
    m2track_types:
        0: todo

        1: uint8
        4: fixed16
        5: float

        21: c3vector
        22: c4quaternion
        23: m2compquat

types:
    m2track:
        params:
            - id: m2track_type
              type: s4
              enum: m2track_types
        seq:
            - id: interpolation_type
              type: u2
            - id: global_sequence
              type: u2
            - id: timestamps
              type: m2array(m2array_types::m2array_uint32)
            - id: values
              type:
                  switch-on: m2track_type
                  cases:
                      m2track_types::todo: m2array(m2array_types::todo)
                      m2track_types::c3vector: m2array(m2array_types::m2array_c3vector)
                      m2track_types::c4quaternion: m2array(m2array_types::m2array_c4quaternion)
                      m2track_types::fixed16: m2array(m2array_types::m2array_fixed16)
                      m2track_types::float: m2array(m2array_types::m2array_float)
                      m2track_types::uint8: m2array(m2array_types::m2array_uint8)
                      m2track_types::m2compquat: m2array(m2array_types::m2array_m2compquat)

    m2trackbase:
        seq:
            - id: interpolation_type
              type: u2
            - id: global_sequence
              type: u2
            - id: timestamps
              type: m2array(m2array_types::m2array_uint32)
