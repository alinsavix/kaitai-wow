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
                      '"GFID"': chunk_gfid
                      '"MDAL"': chunk_mdal
                      '"MFOG"': chunk_mfog
                      '"MLIQ"': chunk_mliq
                      '"MOBA"': chunk_moba
                      '"MOBN"': chunk_mobn
                      '"MOBR"': chunk_mobr
                      '"MOBS"': chunk_mobs
                      '"MOCV"': chunk_mocv
                      '"MODD"': chunk_modd
                      '"MODI"': chunk_modi
                      '"MODR"': chunk_modr
                      '"MODS"': chunk_mods
                      '"MOGI"': chunk_mogi
                      '"MOGN"': chunk_mogn
                      '"MOGP"': chunk_mogp
                      '"MOHD"': chunk_mohd
                      '"MOLP"': chunk_molp
                      '"MOLT"': chunk_molt
                      '"MOMT"': chunk_momt
                      '"MONR"': chunk_monr
                      '"MOPR"': chunk_mopr
                      '"MOPT"': chunk_mopt
                      '"MOPV"': chunk_mopv
                      '"MOPY"': chunk_mopy
                      '"MOSB"': chunk_mosb
                      '"MOTA"': chunk_mota
                      '"MOTV"': chunk_motv
                      '"MOVI"': chunk_movi
                      '"MOVT"': chunk_movt
                      '"MOVV"': chunk_movv

                      _: unknown_chunk

        instances:
            chunk_type:
                value: chunk_type_raw.reverse
