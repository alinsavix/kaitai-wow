types:
    chunk_mslt:
        doc: "Map Spot Lights"
        doc-ref: https://wowdev.wiki/WDT#MSLT_.28Legion.2B.29

        seq:
            - id: spot_lights
              type: map_spot_light
              repeat: eos

    map_spot_light:
        seq:
            - id: id
              type: u4
            - id: color
              type: cargb
            - id: position
              type: c3vector
            - id: range_attenuation_start
              type: f4
            - id: range_attenuiation_end
              type: f4
            - id: intensity
              type: f4
            - id: rotation
              type: c3vector
            - id: falloff_exponent
              type: f4
            - id: inner_radius
              type: f4
            - id: outer_radius
              type: f4
            - id: unknown
              type: s2
              repeat: expr
              repeat-expr: 2
