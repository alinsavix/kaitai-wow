types:
    m2ribbon:
        seq:
            - id: ribbon_id
              type: u4
            - id: bone_index
              type: u4
            - id: position
              type: c3vector
            - id: texture_indices
              type: m2array(m2array_types::uint16)
            - id: material_indices
              type: m2array(m2array_types::uint16)
            - id: color_track
              type: m2track(m2track_types::c3vector)
            - id: alpha_track
              type: m2track(m2track_types::fixed16)
            - id: height_above_track
              type: m2track(m2track_types::float)
            - id: height_below_track
              type: m2track(m2track_types::float)
            - id: edges_per_second
              type: f4
            - id: edge_lifetime
              type: f4
            - id: gravity
              type: f4
            - id: texture_rows
              type: u2
            - id: texture_cols
              type: u2
            - id: tex_slot_track
              type: m2track(m2track_types::uint16)
            - id: visibility_track
              type: m2track(m2track_types::uint8)
            - id: priority_plane
              type: s2
            - id: padding
              type: u2
