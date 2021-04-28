enums:
    m2array_types:
        0: todo

        1: uint8
        2: uint16
        3: uint32
        4: fixed16
        5: float
        6: ubyte4

        21: c2vector
        22: c3vector
        23: c4vector
        24: c4quaternion
        25: frgb

        101: m2sequencefallback
        102: m2compbone
        103: m2vertex
        104: m2color
        105: m2texture
        106: m2textureweight
        107: m2texturetransform
        108: m2material
        109: m2attachment
        110: m2event
        111: m2light
        112: m2camera
        113: m2ribbon
        114: m2particle
        115: m2loop
        116: m2sequence
        117: m2skinsection
        118: m2batch
        119: m2shadowbatch
        120: m2compquat

        201: m2array_uint32
        202: m2array_m2compquat
        203: m2array_c2vector
        204: m2array_c3vector
        205: m2array_c4vector
        206: m2array_c4quaternion
        207: m2array_fixed16
        208: m2array_uint8
        209: m2array_float
        210: m2array_uint16

types:
    m2array:
        params:
            - id: m2array_type
              type: s4
              enum: m2array_types
        seq:
            - id: num
              type: u4
            - id: offset
              type: u4
        instances:
            values:
                pos: offset
                type:
                    switch-on: m2array_type
                    cases:
                        m2array_types::todo: m2array_todo
                        m2array_types::uint8: u1
                        m2array_types::uint16: u2
                        m2array_types::uint32: u4
                        m2array_types::fixed16: fixed16
                        m2array_types::float: f4
                        m2array_types::ubyte4: ubyte4
                        m2array_types::c2vector: c2vector
                        m2array_types::c3vector: c3vector
                        m2array_types::c4vector: c4vector
                        m2array_types::frgb: frgb

                        m2array_types::m2sequencefallback: m2sequencefallback
                        m2array_types::m2compbone: m2compbone
                        m2array_types::m2vertex: m2vertex
                        m2array_types::m2color: m2color
                        m2array_types::m2texture: m2texture
                        m2array_types::m2textureweight: m2textureweight
                        m2array_types::m2texturetransform: m2texturetransform
                        m2array_types::m2material: m2material
                        m2array_types::m2attachment: m2attachment
                        m2array_types::m2event: m2event
                        m2array_types::m2light: m2light
                        m2array_types::m2camera: m2camera
                        m2array_types::m2ribbon: m2ribbon
                        m2array_types::m2particle: m2particle
                        m2array_types::m2loop: m2loop
                        m2array_types::m2sequence: m2sequence
                        m2array_types::m2skinsection: m2skinsection
                        m2array_types::m2batch: m2batch
                        m2array_types::m2shadowbatch: m2shadowbatch
                        m2array_types::c4quaternion: c4quaternion
                        m2array_types::m2compquat: m2compquat

                        m2array_types::m2array_uint32: m2array(m2array_types::uint32)
                        m2array_types::m2array_c2vector: m2array(m2array_types::c2vector)
                        m2array_types::m2array_c3vector: m2array(m2array_types::c3vector)
                        m2array_types::m2array_c4vector: m2array(m2array_types::c4vector)
                        m2array_types::m2array_c4quaternion: m2array(m2array_types::c4quaternion)
                        m2array_types::m2array_fixed16: m2array(m2array_types::fixed16)
                        m2array_types::m2array_float: m2array(m2array_types::float)
                        m2array_types::m2array_uint8: m2array(m2array_types::uint8)
                        m2array_types::m2array_uint8: m2array(m2array_types::uint16)
                        m2array_types::m2array_m2compquat: m2array(m2array_types::m2compquat)

                repeat: expr
                repeat-expr: num

    # 'todo' and 'str' are kind of special cases as far as handling
    # them
    m2array_todo:
        seq: []
            # - id: num
            #   type: u4
            # - id: offset
            #   type: u4

    m2array_str:
        seq:
            - id: num
              type: u4
            - id: offset
              type: u4
        instances:
            arraydata:
                io: _io
                type: str
                encoding: UTF-8
                size: num
                pos: offset
