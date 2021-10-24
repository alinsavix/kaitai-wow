types:
    mphd_flags:
        # FIXME: there are some combine flags we should see about:
        #  mask_vertex_buffer_format             = adt_has_mccv | adt_has_mclv,                    // CMap::LoadWdt
        #  mask_render_chunk_something           = adt_has_height_texturing | adt_has_big_alpha,   // CMapArea::PrepareRenderChunk, CMapChunk::ProcessIffChunks
        seq:
            - id: wdt_uses_global_map_obj
              type: b1 # 0x01
              doc: "Use global map object definition"
            - id: adt_has_mccv
              type: b1 # 0x02
              doc: "adds color: ADT.MCNK.MCCV. With this flag every ADT in the map -must- have a MCCV chunk at least with default values, else only the base texture layer is rendered on such ADTs"
            - id: adt_has_big_alpha
              type: b1 # 0x04
              doc: "shader = 2. Decides whether to use _env terrain shaders or not: funky and if MCAL has 4096 instead of 2048(?)  [better desc needed]"
            - id: adt_has_doodadrefs_sorted_by_size_cat
              type: b1 # 0x08
              doc: "if enabled, the ADT MCRF(m2 only)/MCRD chunks need to be sorted by size category"
            - id: lighting_vertices
              type: b1 # 0x10
              doc: "adds second color: ADT.MCNK.MCLV -- appears to be deprecated"
            - id: adt_has_upside_down_ground
              type: b1 # 0x20
              doc: "Flips the ground display upside down to create a ceiling"
            - id: unknown1
              type: b1 # 0x40
              doc: "Only found in firelands2.wdt (but only MoP <= ver < Legion"
            - id: adt_has_height_texturing
              type: b1 # 0x80
              doc: "shader = 6. Decides whether to influence alpha maps by _h.MTXP. Also changes MCAL size to 4096 for uncompressed entries"

            - id: unknown2
              type: b1 # 0x0100
              doc: "implicitly sets 0x8000"
            - id: wdt_has_maid
              type: b1 # 0x0200
              doc: "client will load ADT using FileDataId instead of filename formatted with '%s\\%s_%d_%d.adt'"
            - id: unknown3
              type: b1 # 0x0400
            - id: unknown4
              type: b1 # 0x0800
            - id: unknown5
              type: b1 # 0x1000
            - id: unknown6
              type: b1 # 0x2000
            - id: unknown7
              type: b1 # 0x4000
            - id: unknown8
              type: b1 # 0x8000
              doc: "Implicitly set for map ids 0, 1, 571, 870, 1116 (continents). Affects the rendering of _lod.adt. If set, or implicitly set by 0x0100, maptextures and LOD are required, otherwise textures further than -533 yards will not render"

    chunk_mphd:
        doc: "Map Header"
        doc-ref: https://wowdev.wiki/WDT#MPHD_chunk

        # FIXME: Original name SMMapHeader
        seq:
            - id: flags
              type: mphd_flags
              size: 4
            - id: lgt_file_data_id
              type: u4
            - id: occ_file_data_id
              type: u4
            - id: fogs_file_data_id
              type: u4
            - id: mpv_file_data_id
              type: u4
            - id: tex_file_data_id
              type: u4
            - id: wdl_file_data_id
              type: u4
            - id: pd4_file_data_id
              type: u4
