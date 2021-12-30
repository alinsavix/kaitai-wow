types:
    c2vector:
        simplifier: simplify_xy
        seq:
            - id: x
              type: f4
            - id: y
              type: f4

    c2ivector:
        seq:
            - id: x
              type: s4  # FIXME: check type ("int" in docs)
            - id: y
              type: s4

    c3vector:
        simplifier: simplify_xyz
        seq:
            - id: x
              type: f4
            - id: y
              type: f4
            - id: z
              type: f4

    c3ivector:
        seq:
            - id: x
              type: s4
            - id: y
              type: s4
            - id: z
              type: s4

    c4vector:
        simplifier: simplify_wxyz
        seq:
            - id: x
              type: f4
            - id: y
              type: f4
            - id: z
              type: f4
            - id: w
              type: f4

    c4ivector:
        seq:
            - id: x
              type: s4
            - id: y
              type: s4
            - id: z
              type: s4
            - id: w
              type: s4

    # For the matrix types, wowdev.wiki isn't sure if these are row- or column- first
    c33matrix:
        seq:
            - id: columns
              type: c3vector
              repeat: expr
              repeat-expr: 3

    c34matrix:
        seq:
            - id: columns
              type: c3vector
              repeat: expr
              repeat-expr: 4

    # wowdev.wiki says "todo: verify"
    c4plane:
        seq:
            - id: normal
              type: c3vector
            - id: distance
              type: f4

    c4quaternion:
        seq:
            - id: x
              type: f4
            - id: y
              type: f4
            - id: z
              type: f4
            - id: w
              type: f4
              doc: "Unlike Quaternions elsewhere, scalar part w is last instead of first"

    # "three component vector of shorts"
    c3svector:
        seq:
            - id: x
              type: s2
            - id: y
              type: s2
            - id: z
              type: s2

    c3segment:
        seq:
            - id: start
              type: c3vector
            - id: end
              type: c3vector

    cfacet:
        seq:
            - id: plane
              type: c4plane
            - id: vertices
              type: c3vector
              repeat: expr
              repeat-expr: 3

    c3ray:
        seq:
            - id: origin
              type: c3vector
            - id: dir
              type: c3vector

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

    fp_6_9:
        seq:
            # FIXME: Make sure this is the right number of bytes
            # FIXME: This is actually a "fixed point" structure which
            # needs further decoding
            - id: value
              type: u2

    vector_2fp_6_9:
        seq:
            - id: x
              type: fp_6_9
            - id: y
              type: fp_6_9
