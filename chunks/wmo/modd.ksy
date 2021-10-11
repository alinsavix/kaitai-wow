types:
    chunk_modd:
        doc: "Map Object Doodad Definition - Documentation is extensive, please see URL"
        doc-ref: https://wowdev.wiki/WMO#MODD_chunk

        seq:
            - id: doodad_defs
              type: doodad_definition_list
              repeat: eos

    doodad_definition_list:
        seq:
            # FIXME: can we do the bitfields less... stupid?
            - id: name_index
              type: b24
            - id: accept_projected
              type: b1
            - id: unknown1
              type: b1
            - id: unknown2
              type: b1
            - id: unknown3
              type: b1
            - id: unused1
              type: b4
            - id: position
              type: c3vector
              doc: "(x, Z, -Y)"
            - id: orientation
              type: c4quaternion
              doc: "(X, Y, Z, W)"
            - id: scale
              type: f4
            - id: color
              type: cimvector
              doc: "(B, G, R, A) diffuse lighting color, in place of global diffuse from DBCs"
