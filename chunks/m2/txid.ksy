types:
    chunk_txid:
        seq:
            - id: file_data_ids
              type: u4
              repeat: eos
              simplifier_each: simplify_fileid
