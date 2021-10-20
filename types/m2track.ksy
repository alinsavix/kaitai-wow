enums:
    m2track_types:
        0: todo

        1: uint8
        2: uint16
        4: fixed16
        5: float

        21: c2vector
        22: c3vector
        23: c4vector
        24: c4quaternion
        25: m2compquat

    m2track_interpolation_types:
        0:
            id: interpolate_const
            doc: "Change instantly at timestamp"
        1:
            id: interpolate_linear
            doc: "Linear interpolation between keyframe values (lerp for vectors/colours, nlerp for quaternions)"
        2:
            id: interpolate_cubic_bezier_spline
            doc: |
                Cubic bezier spline interpolation. Only valid for M2SplineKey tracks. The control
                points are:

                1st - first spline key value
                2nd - first spline key tanOut
                3rd - second spline key tanIn
                4th - second spline key value
        3:
            id: interpolate_cubic_hermite_spline
            doc: |
                Cubic hermite spline interpolation. Only valid for M2SplineKey tracks. The control
                points are:

                starting point - first spline key value
                starting tangent - first spline key tanOut
                ending tangent - second spline key tanIn
                ending point - second spline key value

types:
    m2track:
        params:
            - id: m2track_type
              type: s4
              enum: m2track_types
        seq:
            - id: interpolation_type
              type: u2
              enum: m2track_interpolation_types
            - id: global_sequence
              type: s2
            - id: timestamps
              type: m2array<m2array<u4>>
            - id: values
              type:
                  switch-on: m2track_type
                  cases:
                      m2track_types::todo: m2array(m2array_types::todo)

                      m2track_types::uint8: m2array(m2array_types::m2array_uint8)
                      m2track_types::uint16: m2array(m2array_types::m2array_uint16)
                      m2track_types::fixed16: m2array(m2array_types::m2array_fixed16)
                      m2track_types::float: m2array(m2array_types::m2array_float)

                      m2track_types::c2vector: m2array(m2array_types::m2array_c2vector)
                      m2track_types::c3vector: m2array(m2array_types::m2array_c3vector)
                      m2track_types::c4quaternion: m2array(m2array_types::m2array_c4quaternion)
                      m2track_types::m2compquat: m2array(m2array_types::m2array_m2compquat)

    m2trackbase:
        seq:
            - id: interpolation_type
              type: u2
              enum: m2track_interpolation_types
            - id: global_sequence
              type: s2
            - id: timestamps
              type: m2array(m2array_types::m2array_uint32)

    m2parttrack:
        params:
            - id: m2array_type
              type: s4
              enum: m2array_types
        seq:
            - id: times
              type: m2array(m2array_types::fixed16)
            - id: values
              type:
                  switch-on: m2array_type
                  cases:
                      m2array_types::fixed16: m2array(m2array_types::fixed16)

    # Could also be "M2TrackNoHeader" maybe
    # FIXME: Can we just use this as part of the normal m2track data structure?
    # # I mean, we can, but it'd be more obtuse to access. Hrrm.
    # fblock:
    #     params:
    #         - id: m2array_type
    #           type: s4
    #           enum: m2array_types

    #     seq:
    #         - id: timestamps
    #           type: m2array(m2array_types::uint16)
    #         - id: values
    #           type:
    #               switch-on: m2array_type
    #               cases:
    #                   m2array_types::todo: m2array(m2array_types::todo)

    #                   m2array_types::uint8: m2array(m2array_types::uint8)
    #                   m2array_types::fixed16: m2array(m2array_types::fixed16)
    #                   m2array_types::float: m2array(m2array_types::float)

    #                   m2array_types::c2vector: m2array(m2array_types::c2vector)
    #                   m2array_types::c3vector: m2array(m2array_types::c3vector)
    #                   m2array_types::c4vector: m2array(m2array_types::c4vector)
    #                   m2array_types::c4quaternion: m2array(m2array_types::c4quaternion)
    #                   m2array_types::m2compquat: m2array(m2array_types::m2compquat)

    fblock:
        params:
            - id: m2array_type
              type: s4
              enum: m2array_types

        seq:
            # FIXME: Doublecheck type for timestamps
            - id: timestamps
              type: m2array(m2array_types::uint16)
            - id: values
              type:
                  switch-on: m2array_type
                  cases:
                      m2array_types::todo: m2array(m2array_types::todo)

                      m2array_types::uint8: m2array(m2array_types::uint8)
                      m2array_types::uint16: m2array(m2array_types::uint16)
                      m2array_types::fixed16: m2array(m2array_types::fixed16)
                      m2array_types::float: m2array(m2array_types::float)
                      m2array_types::frgb: m2array(m2array_types::frgb)

                      m2array_types::c2vector: m2array(m2array_types::c2vector)
                      m2array_types::c3vector: m2array(m2array_types::c3vector)
                      m2array_types::c4vector: m2array(m2array_types::c4vector)
                      m2array_types::c4quaternion: m2array(m2array_types::c4quaternion)
                      m2array_types::m2compquat: m2array(m2array_types::m2compquat)
