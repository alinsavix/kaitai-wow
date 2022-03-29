types:
    chunk_mobr:
        doc: "Map Object Node Face Indexes"
        doc-ref: https://wowdev.wiki/WMO#MOBR_chunk

        seq:
            - id: node_face_indices
              type: u2
              repeat: eos
              doc: "Face indices for MOBN. Triangle indices (in MOVI which define triangles) to describe polygon planes defined by MOBN nodes."
