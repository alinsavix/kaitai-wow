types:
    crange:
        seq:
            - id: min
              type: f4
            - id: max
              type: f4

    cirange:
        seq:
            - id: min
              type: s4 # FIXME: verify these are 4 bytes
            - id: max
              type: s4

    # Axis-aligned box
    caabox:
        seq:
            - id: min
              type: c3vector
            - id: max
              type: c3vector

    # Axis-aligned sphere
    caasphere:
        seq:
            - id: position
              type: c3vector
            - id: radius
              type: f4

    cargb:
        seq:
            - id: r
              type: u1
            - id: g
              type: u1
            - id: b
              type: u1
            - id: a
              type: u1

    cimvector:
        seq:
            - id: b
              type: u1
            - id: g
              type: u1
            - id: r
              type: u1
            - id: a
              type: u1

    crect:
        seq:
            - id: top
              type: f4
            - id: miny
              type: f4
            - id: left
              type: f4
            - id: minx
              type: f4
            - id: bottom
              type: f4
            - id: maxy
              type: f4
            - id: right
              type: f4
            - id: maxx
              type: f4

    cirect:
        seq:
            - id: top
              type: s4
            - id: miny
              type: s4
            - id: left
              type: s4
            - id: minx
              type: s4
            - id: bottom
              type: s4
            - id: maxy
              type: s4
            - id: right
              type: s4
            - id: maxx
              type: s4

    frgb:
        seq:
            - id: r
              type: f4
            - id: g
              type: f4
            - id: b
              type: f4
