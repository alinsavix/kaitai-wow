
types:
    chunk_mods:
        doc: "Map Object Doodad Sets"
        doc-ref: https://wowdev.wiki/WMO#MODS_chunk

        seq:
            - id: doodad_sets
              type: doodad_set_list
              repeat: eos

    doodad_set_list:  # FIXME: originally SMODoodadSet
        seq:
            - id: name
              type: strz
              size: 20
            - id: start_index
              type: u4
            - id: count
              type: u4
            - id: unused1
              type: u4
