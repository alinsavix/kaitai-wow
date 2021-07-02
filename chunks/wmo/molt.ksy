enums:
    wmo_light_types:
        0: omni
        1: spot
        2: direct
        3: ambient

types:
    chunk_molt:
        doc: "Map Object Lighting Information"
        doc-ref: https://wowdev.wiki/WMO#MOLT_chunk

        seq:
            - id: lights
              type: light_list
              repeat: eos

    light_list:  # FIXME: originally SMOLight
        seq:
            - id: type
              type: u1
              enum: wmo_light_types
            - id: use_attenuation
              type: u1
            - id: unknown1
              type: u2
            - id: color
              type: cimvector
            - id: position
              type: c3vector
            - id: intensity
              type: f4
            - id: unknown2
              type: f4
              repeat: expr
              repeat-expr: 4
            - id: attenuation_start
              type: f4
            - id: attenuation_end
              type: f4
