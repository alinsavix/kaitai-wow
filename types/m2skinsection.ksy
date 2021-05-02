types:
    # Not sure why they don't call this struct "submeshes"
    m2skinsection:
        doc: "Submesh information"
        doc-ref: https://wowdev.wiki/M2/.skin#Submeshes
        seq:
            - id: skin_section_id
              type: u2
            - id: level
              type: u2
              doc: "`(level << 16)` is added to start_triangle to avoid needing to make those fields larger"
            - id: vertex_start
              type: u2
              doc: "Starting vertex number"
            - id: vertex_count
              type: u2
            - id: index_start
              type: u2
              doc: "Starting triangle index (3x number of triangles drawn so far)"
            - id: index_count
              type: u2
            - id: bone_count
              type: u2
              doc: "Number of elements in bone lookup table, always > 0"
            - id: bone_combo_index
              type: u2
              doc: "Starting index in bone lookup table"
            - id: bone_influences
              type: u2
              doc: "Highest number of bones referenced by a vertex of this submesh, always <= 4 "
            - id: center_bone_index
              type: u2
            - id: center_position
              type: c3vector
              doc: "Average position of all the verts in the submesh"
            - id: sort_center_position
              type: c3vector
              doc: "Center of the box when an axis-aligned box is built around the verts of the submesh"
            - id: sort_radius
              type: f4
              doc: "Distance of the vertex farthest from CenterBoundingBox"
