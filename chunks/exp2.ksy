types:
    chunk_exp2:
        doc: "Extended particle information, one entry per particle_emitter"
        doc-ref: https://wowdev.wiki/M2#EXP2
        seq:
            - id: content
              type: m2array(m2array_types::m2extended_particle)
