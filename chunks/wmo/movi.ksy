types:
    chunk_movi:
        doc: "Map Object Vertex Indices - Group's vertex indices from the group's vertex list (MOVT, MONR, MOTV) to form triangles"
        doc-ref: https://wowdev.wiki/WMO#MOVI_chunk

        seq:
            - id: indices
              type: u2
              repeat: eos
