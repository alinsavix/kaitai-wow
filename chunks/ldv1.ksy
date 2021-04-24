types:
    chunk_ldv1:
        seq:
            - id: unk0
              type: u2
            - id: lod_count
              type: u2
            - id: unk2_f
              type: f4
            - id: particle_bone_lod
              type: u1
              repeat: expr
              repeat-expr: 4
