types:
    m2vertex:
        seq:
            - id: pos
              type: c3vector
            - id: bone_weights
              type: u1
              repeat: expr
              repeat-expr: 4
              simplifier: simplify_fourbone
            - id: bone_indices
              type: u1
              repeat: expr
              repeat-expr: 4
              simplifier: simplify_fourbone
            - id: normal
              type: c3vector
            - id: tex_coords
              type: c2vector
              repeat: expr
              repeat-expr: 2
