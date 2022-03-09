# not yet implemented
# see https://wowdev.wiki/ADT/v18
meta:
    id: adt
    endian: le
    bit-endian: le
    encoding: UTF-8

    xref:
        doc-ref: https://wowdev.wiki/ADT/v18

    # include is read by merge-yaml.py and then removed. It isn't legal
    # in normal kaitai-struct configurations
    include:
        - enums
        - types
        - chunks/adt

seq:
    # This shooooould always be first
    - id: mvermagic
      contents: "REVM" # MVER backwards
    - id: chunksize
      type: u4

    - id: ver
      type: u4

    - id: chunks
      type: adt_chunk
      repeat: eos

types:
    adt_chunk:
        seq:
            - id: chunk_type_raw
              type: str
              size: 4
              encoding: UTF-8
              simplifier: simplify_remove
            - id: chunk_size
              type: u4
            - id: chunk_data
              size: chunk_size
              type:
                  switch-on: chunk_type_raw.reverse
                  cases:
                      '"MDID"': chunk_mdid
                      '"MDDF"': chunk_mddf
                    #   '"MCNK"': chunk_mcnk
                      '"MH2O"': chunk_mh2o
                      '"MHDR"': chunk_mhdr
                      '"MHID"': chunk_mhid
                      '"MMDX"': chunk_mmdx
                      '"MMID"': chunk_mmid
                      '"MWID"': chunk_mwid
                      '"MWMO"': chunk_mwmo

                      _: unknown_chunk

        instances:
            chunk_type:
                value: chunk_type_raw.reverse
