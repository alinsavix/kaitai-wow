types:
    chunk_molp:
        doc: "Map Object Point Lights"
        doc-ref: https://wowdev.wiki/WMO#MOLP_chunk

        seq:
            - id: map_object_point_lights
              type: point_light
              repeat: eos

    point_light:
        seq:
            - id: unknown1
              type: u4
            - id: color
              type: cimvector
            - id: pos
              type: c3vector
              doc: "Position of light"
            - id: intensity
              type: f4
            - id: attenuation_start
              type: f4
            - id: attenuation_end
              type: f4
            - id: unknown4
              type: f4
              doc: "possibly unused"
            - id: unknown5
              type: u4
            - id: unknown6
              type: u4
              doc: "CArgb?"
