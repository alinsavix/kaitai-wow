types:
    chunk_txac:
        doc: "Particle-texture Releated"
        doc-ref: https://wowdev.wiki/M2#TXAC
        seq:
            # FIXME: These could also be a union of two bytes
            - id: txac_mesh
              type: u2
              repeat: expr
              repeat-expr: _root.chunks[0].data.as<chunk_md21>.data.as<chunk_md20>.materials.num
            - id: txac_m_particle
              type: u2
              repeat: expr
              repeat-expr: _root.chunks[0].data.as<chunk_md21>.data.as<chunk_md20>.particle_emitters.num
