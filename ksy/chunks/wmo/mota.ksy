types:
    chunk_mota:
        doc: "Map Object Tangent Array"
        doc-ref: https://wowdev.wiki/WMO#MOTA

        seq: []
        # - id: first_index
        #   type: u2
        #   repeat: expr
        #   repeat-expr: moba_count
        #   doc: "either -1 or first index of batch.count indices into tangents[]. If auto-generated, only has entries for batches with material[batch.material].shader == 10 or 14"
        # - id: tangents
        #   type: c4vector
        #   repeat: expr
        #   repeat-expr: accumulated_num_indices
        #   doc: "sum (batches[i].count | material[batches[i].material].shader == 10 or 14)"

        instances:
            note:
                value: '"not implemented"'
