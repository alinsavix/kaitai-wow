types:
    chunk_txac:
        doc: "Particle-texture Releated"
        doc-ref: https://wowdev.wiki/M2#TXAC
        seq:
            # FIXME: These could also be a union of two bytes
            - id: txac_mesh
              type: u2
              repeat: expr
              repeat-expr: _root.header.num_materials
            - id: txac_m_particle
              type: u2
              repeat: expr
              repeat-expr: _root.header.num_particle_emitters
