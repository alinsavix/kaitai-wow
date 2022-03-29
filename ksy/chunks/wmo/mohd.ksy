types:
    mohd_flags:
        seq:
            - id: no_attenuate_portal_dist
              type: b1 # 0x01
            - id: unified_render_path
              type: b1 # 0x02
              doc: |
                  In 3.3.5a this flag switches between classic render path (MOHD color is
                  baked into MOCV values, all three batch types have their own rendering
                  logic) and unified (MOHD color is added to lighting at runtime, int. and
                  ext. batches share the same rendering logic). See https://wowdev.wiki/WMO/Rendering for more details
            - id: liquid_type_from_dbc
              type: b1 # 0x04
              doc: "use real liquid type ID from DBCs instead of local one. See MLIQ for further reference"
            - id: no_fix_vertex_color_alpha
              type: b1 # 0x08
              doc: |
                  In 3.3.5.a (and probably before) it prevents CMapObjGroup::FixColorVertexAlpha function to be executed. Alternatively, for the wotlk version of it, the function can be called with MOCV.a being set to 64, which will produce the same effect for easier implementation. For wotlk+ rendering, it alters the behavior of the said function instead. See https://wowdev.wiki/WMO/Rendering for more details.
            - id: lod
              type: b1 # 0x10
            - id: default_max_lod
              type: b1 # 0x20
              doc: "Usually maxLodLevel = -1 but with this flag, numLod. Entries at this level are defaulted"
            - id: unused1
              type: b10 # 0x40 to 0x8000

    chunk_mohd:
        doc: "Map Object Header"
        doc-ref: https://wowdev.wiki/WMO#MOHD_chunk
        seq:
            - id: num_textures
              type: u4
            - id: num_groups
              type: u4
            - id: num_portals
              type: u4
            - id: num_lights
              type: u4
              doc: "Blizzard seems to add one to the MOLT entry count when there are MOLP chunks in the groups (and maybe for MOLS too)"
            - id: num_doodad_names
              type: u4
            - id: num_doodad_defs
              type: u4
            - id: num_doodad_sets
              type: u4

            - id: amb_color
              type: cargb
            - id: foreign_key
              type: u4 # FIXME: Is there more to this? def on wowdev is weird

            - id: bounding_box
              type: caabox
            - id: flags
              type: mohd_flags
            - id: num_lod
              type: u2
