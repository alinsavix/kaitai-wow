meta:
    id: m2
    endian: le
    bit-endian: le
    encoding: UTF-8

    xref:
        doc-ref: https://wowdev.wiki/M2

    # include is read by merge-yaml.py and then removed. It isn't legal
    # in normal kaitai-struct configurations
    include:
        - enums
        - types
        - chunks

seq:
    # FIXME: Not 100% certain we'll always see the MD21/MD20 pair
    - id: md21magic
      contents: "MD21"
    - id: headersize
      type: u4
    - id: model
      type: chunk_md20
      size: headersize
    - id: chunks
      type: chunk
      repeat: until
      repeat-until: _io.eof

types:
    noop: {}

    chunk:
        seq:
            - id: chunk_type
              type: str
              size: 4
              encoding: UTF-8
            - id: chunk_size
              type: u4
            - id: chunk_data
              size: chunk_size
              type:
                  switch-on: chunk_type
                  cases:
                      #   '"MD21"': chunk_md21
                      '"LDV1"': chunk_ldv1
                      '"TXID"': chunk_txid
                      '"TXAC"': chunk_txac
                      '"EXP2"': chunk_exp2
                      '"PGD1"': chunk_pgd1
                      '"DETL"': chunk_detl
                      '"SFID"': chunk_sfid
                      '"AFID"': chunk_afid
                      _: noop
