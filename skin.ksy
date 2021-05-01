meta:
    id: skin
    endian: le
    bit-endian: le
    encoding: UTF-8

    # include is read by merge-yaml.py and then removed. It isn't legal
    # in normal kaitai-struct configurations
    include:
        - enums
        - types

seq:
    # FIXME: Will .skin files ever have more than one chunk?
    - id: magic
      contents: "SKIN"
    - id: vertices
      type: m2array(m2array_types::uint16)
    - id: indices
      type: m2array(m2array_types::uint16)
    - id: bones
      type: m2array(m2array_types::ubyte4)
    - id: submeshes
      type: m2array(m2array_types::m2skinsection)
    - id: batches
      type: m2array(m2array_types::m2batch)
    - id: bone_count_max
      type: u4
    - id: shadow_batches
      type: m2array(m2array_types::m2shadowbatch)
