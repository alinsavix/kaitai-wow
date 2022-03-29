types:
    chunk_pvbd:
        doc: "Map Particle Volume BD"
        doc-ref: https://wowdev.wiki/WDT#PVBD

        seq:
            - id: particle_volume_bds
              type: particle_volume_bd
              repeat: eos

    particle_volume_bd:
        seq:
            - id: unknown1
              type: u4
            - id: unknown2
              type: caabox
              doc: "bounds/extents"
            - id: unknown3
              type: u4
              doc: "indices into PVPD"
              repeat: expr
              repeat-expr: 8
            - id: unknown4
              type: u4
              doc: "true if this entry is complete, false and this entry will be joined with next"
