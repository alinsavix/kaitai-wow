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
        - chunks/skin.ksy

seq:
    # FIXME: Will .skin files ever have more than one chunk?
    - id: chunks
      type: chunk_skin
