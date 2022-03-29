# not yet implemented
meta:
    id: wdt
    endian: le
    bit-endian: le
    encoding: UTF-8

    xref:
        doc-ref: https://wowdev.wiki/WDT

    # include is read by merge-yaml.py and then removed. It isn't legal
    # in normal kaitai-struct configurations
    include:
        - enums
        - types
        - chunks/wdt


seq:
    # This shooooould always be first
    - id: mvermagic
      contents: "REVM" # MVER backwards
    - id: chunksize # We know the size, no need to store it
      type: u4

    - id: ver
      type: u4

    # CHUNKEH
    - id: chunks
      type: wdt_chunk
      repeat: eos


types:
    noop: {}

    wdt_chunk:
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
                      '"MPHD"': chunk_mphd
                      '"MAIN"': chunk_main
                      '"MAID"': chunk_maid
                      '"MPL3"': chunk_mpl3
                      '"MSLT"': chunk_mslt
                      '"MLTA"': chunk_mlta
                      '"PVMI"': chunk_pvmi
                      '"PVBD"': chunk_pvbd
                      '"PVPD"': chunk_pvpd
                      '"MAOI"': chunk_maoi
                      '"MAOH"': chunk_maoh

                      _: noop

        instances:
            chunk_type:
                value: chunk_type_raw.reverse
