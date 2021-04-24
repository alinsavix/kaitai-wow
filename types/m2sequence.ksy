types:
    m2sequence:
        seq:
            - id: id
              type: u2
            - id: variation_index
              type: u2
            - id: duration
              type: u4
            - id: movespeed
              type: f4
            - id: flags
              type: u4
            - id: frequency
              type: s2
            - id: padding
              type: u2
            - id: replay
              type: m2range
            - id: blend_time_in
              type: u2
            - id: blend_time_out
              type: u2
            - id: bounds
              type: m2bounds
            - id: variation_next
              -orig-id: variationNext
              type: s2
            - id: alias_next
              -orig-id: aliasNext
              type: u2
