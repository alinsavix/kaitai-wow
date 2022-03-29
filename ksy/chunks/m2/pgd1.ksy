types:
    chunk_pgd1:
        doc: |
            Particle Geoset Data - Sets geoset for each Particle emitter.
            And with this value Particle Emitter start to obey same geoset
            rules as in M2SkinSection
        doc-ref: https://wowdev.wiki/M2#PGD1
        seq:
            - id: p_g_d_v1
              type: m2array<pgd1_entry>
