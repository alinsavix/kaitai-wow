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
      contents: "REVM"  # MVER backwards
    - id: chunksize  # We know the size, no need to store it
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
                    '"DHPM"': chunk_mphd
                    '"NIAM"': chunk_main
                    '"DIAM"': chunk_maid
                    '"3LPM"': chunk_mpl3
                    '"TLSM"': chunk_mslt
                    '"ATLM"': chunk_mlta
                    '"IMVP"': chunk_pvmi
                    '"DBVP"': chunk_pvbd
                    '"DPVP"': chunk_pvpd
                    '"IOAM"': chunk_maoi
                    '"HOAM"': chunk_maoh
                    # '"NGOM"': chunk_mogn
                    # '"IGOM"': chunk_mogi
                    # '"VPOM"': chunk_mopv
                    # '"TPOM"': chunk_mopt
                    # '"RPOM"': chunk_mopr
                    # '"TLOM"': chunk_molt
                    # '"SDOM"': chunk_mods
                    # '"IDOM"': chunk_modi
                    # '"DDOM"': chunk_modd
                    # '"GOFM"': chunk_mfog
                    # '"DIFG"': chunk_gfid
                    # '"PGOM"': chunk_mogp
                    # '"YPOM"': chunk_mopy
                    # '"IVOM"': chunk_movi
                    # '"TVOM"': chunk_movt
                    # '"RNOM"': chunk_monr
                    # '"VTOM"': chunk_motv
                    # '"ABOM"': chunk_moba
                    # '"SBOM"': chunk_mobs
                    # '"RDOM"': chunk_modr
                    # '"NBOM"': chunk_mobn
                    # '"RBOM"': chunk_mobr
                    # '"VCOM"': chunk_mocv
                    # '"LADM"': chunk_mdal

                    _: noop
