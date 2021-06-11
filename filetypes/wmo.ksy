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
      contents: "REVM"  # MVER backwards
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
                    '"DHOM"': chunk_mohd
                    '"TMOM"': chunk_momt
                    '"NGOM"': chunk_mogn
                    '"IGOM"': chunk_mogi
                    '"VPOM"': chunk_mopv
                    '"TPOM"': chunk_mopt
                    '"RPOM"': chunk_mopr
                    '"TLOM"': chunk_molt
                    '"SDOM"': chunk_mods
                    '"IDOM"': chunk_modi
                    '"DDOM"': chunk_modd
                    '"GOFM"': chunk_mfog
                    '"DIFG"': chunk_gfid
                    '"PGOM"': chunk_mogp
                    '"YPOM"': chunk_mopy
                    '"IVOM"': chunk_movi
                    '"TVOM"': chunk_movt
                    '"RNOM"': chunk_monr
                    '"VTOM"': chunk_motv
                    '"ABOM"': chunk_moba
                    '"SBOM"': chunk_mobs
                    '"RDOM"': chunk_modr
                    '"NBOM"': chunk_mobn
                    '"RBOM"': chunk_mobr
                    '"VCOM"': chunk_mocv
                    '"LADM"': chunk_mdal

                    _: noop
