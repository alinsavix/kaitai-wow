# Parse a BLS ("blizzard shader") file. Note that the decompression step
# isn't done, so if you want the actual shader, you'll need to do that
# part yourself, at least for now (each compressed chunk is zlib compressed)
#
# Note that the primary structure here differs slightly from what is currently
# documented on wowdev.wiki
meta:
    id: bls
    endian: le
    bit-endian: le
    encoding: UTF-8

    xref:
        doc: |
            BLS is the container format that stores the GPU shaders used to render
            the world. In WoD, there are now four different shader types under the
            Shaders\* directory.

            Vertex (versions: arbvp1, vp40, glvs_150, ps_2_0, ps_3_0, ps_4_0, ps_5_0)

            Fragment (versions: arbfp1, fp40, glfs_150, ps_2_0, ps_3_0, ps_4_0, ps_5_0)

            Geometry (versions: glgs_150, gs_4_0, gs_5_0)

            Hull/Domain (versions: ds_5_0/hs_50)

            Hull/Domain is equivalent to Tessellation in OpenGL, except WoW currently only has these shaders for DX

        doc-ref: https://wowdev.wiki/BLS

    # include is read by merge-yaml.py and then removed. It isn't legal
    # in normal kaitai-struct configurations
    include:
        - enums
        - types

seq:
    # All shader files are GXSH now, so just check for it rather than
    # doing FOURCC-style dispatching
    - id: magic
      contents: "HSXG"  # reversed from acctual chunk name, because... reasons?
    - id: unknown1
      type: u4
    - id: version
      type: u4
    - id: num_shaders
      type: u4
    - id: ofs_compressed_chunks
      type: u4
    - id: num_compressed_chunks
      type: u4
    - id: ofs_compressed_data
      type: u4
    - id: ofs_shader_blocks
      type: u4
      repeat: expr
      repeat-expr: num_shaders + 1
    - id: shader_offsets
      type: u4
      repeat: expr
      repeat-expr: num_compressed_chunks + 1

# Pull out the individual data chunks, via a bunch of gymnastics.
# FIXME: Is there better naming that can be used here? Everything here
# just seems awful.
instances:
    compressed_chunks:
        type: compressed_chunk(_index)
        repeat: expr
        repeat-expr: num_compressed_chunks

types:
    compressed_chunk:
        params:
            - id: i
              type: u4
        instances:
            chunk_pos:
                value: _parent.ofs_compressed_data + _parent.shader_offsets[i]
            chunk_size:
                value: _parent.shader_offsets[i + 1] - _parent.shader_offsets[i]
            chunk:
                pos: chunk_pos
                size: chunk_size
