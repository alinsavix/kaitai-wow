types:
    chunk_modd:
        doc: "Map Object Doodad Definition - Documentation is extensive, please see URL"
        doc-ref: https://wowdev.wiki/WMO#MODD_chunk

        seq:
            - id: doodad_defs
              type: doodad_definition_list
              repeat: eos

    modd_flags:
        seq:
            - id: accept_projected
              type: b1  # 0x01
              doc: "can have textures projected onto it (e.g. npc selection circle)"
            - id: wmo_interior_lighting
              type: b1  # 0x02
              doc: "when enabled use wmo interior lighting, otherwise exterior lighting"
            - id: unknown_0x04
              type: b1  # 0x04
            - id: unknown_0x08
              type: b1  # 0x08
            - id: unused1
              type: b4  # 0x10 to 0x80

    doodad_definition_list:
        seq:
            # FIXME: can we do the bitfields less... stupid?
            - id: name_index
              type: b24
            - id: flags
              type: modd_flags
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
              doc: |
                overrides sun color. Should only be applied to opaque submeshes of m2;
                if A != 0xff && A < 255, A is a MOLT index that is used instead of RGB here, taking distance and intensity into account;
                if A > MOLT count, then MOLT[0] is used;
                if A == 255, the shading direction vector is based on center of the group rather than sun direction vector; the look-at vector from group bounds center to doodad position
