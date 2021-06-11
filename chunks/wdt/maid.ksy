
types:
    chunk_maid:
        doc: "Map fileid table. Needs to contain 64x64 (4096) entries"
        doc-ref: https://wowdev.wiki/WDT#MAID_chunk

        seq:
            - id: map_fileids
              type: map_file_data_id_set
              repeat: eos


    # FIXME: originally MapFileDataIDs
    # FIXME: find a file we can actually test this with
    map_file_data_id_set:
        seq:
            - id: root_adt_file_data_id
              type: u4
              doc: "reference to mapname_xx_yy.adt"
            - id: obj_0_adt_file_data_id
              type: u4
              doc: "reference to mapname_xx_yy_obj0.adt"
            - id: obj_1_adt_file_data_id
              type: u4
              doc: "reference to mapname_xx_yy_obj1.adt"
            - id: tex_0_adt_file_data_id
              type: u4
              doc: "reference to mapname_xx_yy_tex0.adt"
            - id: lod_adt_file_data_id
              type: u4
              doc: "reference to mapname_xx_yy_lod.adt"
            - id: map_texture_file_data_id
              type: u4
              doc: "reference to mapname_xx_yy.blp"
            - id: map_texture_n_file_data_id
              type: u4
              doc: "reference to mapname_xx_yy_n.blp"
            - id: minimap_texture_file_data_id
              type: u4
              doc: "reference to mapxx_yy.blp"
