enums:
    bspnode_flags:
        0: yz_plane
        1: xz_plane
        2: xy_plane
        3: axismask
        4: leaf
        -1: nochild

types:
    chunk_mobn:
        doc: "Map Object BSP Nodes"
        doc-ref: https://wowdev.wiki/WMO#MOBN_chunk

        seq:
            - id: bspnodes
              type: bspnode
              repeat: eos

    bspnode:  # FIXME: originally CAaBspNode
        seq:
            - id: flags
              type: u2
              enum: bspnode_flags
              simplifier: simplify_enum
            - id: neg_child
              type: s2
              doc: "index of bsp child node (right in this array)"
            - id: pos_child
              type: s2
            - id: num_faces
              type: u2
              doc: "num of triangle faces in MOBR"
            - id: face_start
              type: u4
              doc: "index of the first triangle index (in MOBR)"
            - id: plane_dist
              type: f4
