meta:
    id: wmo
    endian: le
    bit-endian: le
    encoding: UTF-8

    xref:
        doc-ref: https://wowdev.wiki/WMO

    # include is read by merge-yaml.py and then removed. It isn't legal
    # in normal kaitai-struct configurations
    include:
        - enums
        - types
        - chunks/wmo


seq:
    # This shooooould always be first
    - id: mvermagic
      contents: "REVM" # MVER backwards
    - id: chunksize  # We know the size, no need to store it
      type: u4

    - id: ver
      type: u4

    # CHUNKEH
    - id: chunks
      type: wmo_chunk
      repeat: eos



types:
    noop: {}

    wmo_chunk:
        seq:
            - id: chunk_type_raw
              type: str
              size: 4
              encoding: UTF-8
            - id: chunk_size
              type: u4
            - id: chunk_data
              size: chunk_size
              type:
                  switch-on: chunk_type_raw.reverse
                  cases:
                    '"MOHD"': chunk_mohd
                    '"MOMT"': chunk_momt
                    '"MOGN"': chunk_mogn
                    '"MOGI"': chunk_mogi
                    '"MOPV"': chunk_mopv
                    '"MOPT"': chunk_mopt
                    '"MOPR"': chunk_mopr
                    '"MOLT"': chunk_molt
                    '"MODS"': chunk_mods
                    '"MODI"': chunk_modi
                    '"MODD"': chunk_modd
                    '"MFOG"': chunk_mfog
                    '"GFID"': chunk_gfid
                    '"MOGP"': chunk_mogp
                    '"MOPY"': chunk_mopy
                    '"MOVI"': chunk_movi
                    '"MOVT"': chunk_movt
                    '"MONR"': chunk_monr
                    '"MOTV"': chunk_motv
                    '"MOBA"': chunk_moba
                    '"MOBS"': chunk_mobs
                    '"MODR"': chunk_modr
                    '"MOBN"': chunk_mobn
                    '"MOBR"': chunk_mobr
                    '"MOCV"': chunk_mocv
                    '"MDAL"': chunk_mdal

                    _: noop

        instances:
            chunk_type:
                value: chunk_type_raw.reverse
