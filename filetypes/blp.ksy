# Parse a BLP ("blizzard picture") file. Reading the actual binary data is
# up to the user, since we don't want to use opaque types, and we don't just
# want to needlessly load large arrays of bytes or whatever. It's easy though,
# since all the structs here say where and how much, all the user need do
# is read those bytes.
meta:
    id: blp
    endian: le
    bit-endian: le
    encoding: UTF-8

    xref:
        doc: |
            Textures with precalculated mipmaps, in one of several different
            formats. RGB formats are stored using DXT compression (DXT1 for
            0-bit alpha, DXT3 for others). Formats used:

            Palettized, 0-bit alpha (P0) - Example: character skins, clothing.
            Palettized, 1-bit alpha (P1) - Example:. clothing (relatively rare).
            Palettized, 8-bit alpha (P8) - Example: clothing.

            RGB, 0-bit alpha (RGB0) - Example: Sansamroot.blp.
            RGB, 1-bit alpha (RGB1) - Example: Peaceflower.blp.
            RGB, 8-bit alpha (RGB8) - Example: Sungrass.blp.
        doc-ref: https://wowdev.wiki/BLP

    # include is read by merge-yaml.py and then removed. It isn't legal
    # in normal kaitai-struct configurations
    include:
        - enums
        - types

enums:
    blp_color_encodings:
        0: color_jpeg
        1: color_palette
        2: color_dxt
        3: color_argb8888
        4: color_argb8888_dup

    blp_pixel_format:
        0: pixel_dxt1
        1: pixel_dxt3
        2: pixel_argb8888
        3: pixel_argb1555
        4: pixel_argb4444
        5: pixel_rgb565
        6: pixel_a8
        7: pixel_dxt5
        8: pixel_unspecified
        9: pixel_argb2565
        11: pixel_bc5  # DXGI_FORMAT_BC5_UNORM

seq:
    - id: magic
      contents: "BLP2"
    - id: version
      contents: [ 0x01, 0x00, 0x00, 0x00 ]

    - id: color_encoding
      type: u1
      enum: blp_color_encodings
    - id: alpha_channel_bit_depth
      type: u1
    - id: preferred_format
      type: u1
      enum: blp_pixel_format
    - id: mipmap_level
      type: b4
    - id: flag_unknown
      type: b1
    - id: width
      type: u4
      doc: "Power of two"
    - id: height
      type: u4
      doc: "Power of two"
    - id: mip_offsets
      type: u4
      repeat: expr
      repeat-expr: 16
    - id: mip_sizes
      type: u4
      repeat: expr
      repeat-expr: 16
    - id: palette
      type: blp_pal_pixel
      repeat: expr
      repeat-expr: 256


types:
    blp_pal_pixel:
        seq:
            - id: b
              type: u1
            - id: g
              type: u1
            - id: r
              type: u1

            # FIXME: We don't have to actually assign to a variable here, right?
            - id: pad
              type: u1
