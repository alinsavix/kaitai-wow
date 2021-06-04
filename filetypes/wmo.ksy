# not yet implemented
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
        - chunks


seq:
    # This shooooould always be first
    - id: mvermagic
      contents: "REVM"  # MVER backwards
    - id: chunksize  # We know the size, no need to store it
      type: u4

    # This is the only version we know right now, so assert that it's
    # also the version we're reading
    - id: ver
      contents: 0x00000011

    # CHUNKEH
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
                      '"DHOM"': chunk_mohd
                      '"TMOM"': chunk_momt
                      '"NGOM"': chunk_mogn
                      '"TLOM"': chunk_molt
                      '"SDOM"': chunk_mods
                      '"DDOM"': chunk_modd
                      '"IDOM"': chunk_modi
                      '"GOFM"': chunk_mfog
                      '"DIFG"': chunk_gfid
                      '"IDDM"': chunk_mddi
                      '"GVAM"': chunk_mavg
                      '"PGOM"': chunk_mogp
                      '"YPOM"': chunk_mopy
                      '"LADM"': chunk_madl
                      _: noop
