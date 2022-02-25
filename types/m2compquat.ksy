types:
    m2compquat:
        simplifier: simplify_wxyz
        seq:
            - id: raw_x
              type: s2
            - id: raw_y
              type: s2
            - id: raw_z
              type: s2
            - id: raw_w
              type: s2
        instances:
            x:
                value: '(raw_x < 0 ? raw_x + 32768 : raw_x - 32767) / 32767.0'
            y:
                value: '(raw_y < 0 ? raw_y + 32768 : raw_y - 32767) / 32767.0'
            z:
                value: '(raw_z < 0 ? raw_z + 32768 : raw_z - 32767) / 32767.0'
            w:
                value: '(raw_w < 0 ? raw_w + 32768 : raw_w - 32767) / 32767.0'
