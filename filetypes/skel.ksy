meta:
    id: skel
    endian: le
    bit-endian: le
    encoding: UTF-8

    # include is read by merge-yaml.py and then removed. It isn't legal
    # in normal kaitai-struct configurations
    include:
        - enums
        - types
        - chunks/afid.ksy
        - chunks/skel

seq:
    - id: skel
      type: skel_chunk
      repeat: until
      repeat-until: _io.eof

types:
    noop: {}

    skel_chunk:
        seq:
            - id: chunk_type
              type: str
              size: 4
              encoding: UTF-8
            - id: chunk_size
              type: u4
            - id: data
              size: chunk_size
              type:
                  switch-on: chunk_type
                  cases:
                      '"SKL1"': chunk_skl1
                      '"SKA1"': chunk_ska1
                      '"SKB1"': chunk_skb1
                      '"SKS1"': chunk_sks1
                      '"SKPD"': chunk_skpd
                      '"AFID"': chunk_afid
                      '"BFID"': chunk_bfid
                      _: noop
