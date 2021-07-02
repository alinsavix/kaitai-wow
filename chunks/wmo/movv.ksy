types:
    chunk_movv:
        doc: "Map Object Visible Block Vertices"
        doc-ref: https://wowdev.wiki/WMO#MOVV_chunk

        seq:
            - id: visible_block_vertices
              type: c3vector
              repeat: eos
              doc: "A list of vertices that corresponds to the visible block list."
