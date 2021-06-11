types:
    chunk_pvpd:
        doc: "Map Particle Volume PD"
        doc-ref: https://wowdev.wiki/WDT#PVPD

        seq:
            - id: particle_volume_pds
              type: particle_volume_pd
              repeat: eos

    particle_volume_pd:
        seq:
            - id: unknown1
              type: c2vector
            - id: unknown2
              type: f4
            - id: unknown3
              type: f4
