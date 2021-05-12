meta:
    id: skin
    endian: le
    bit-endian: le
    encoding: UTF-8

    # include is read by merge-yaml.py and then removed. It isn't legal
    # in normal kaitai-struct configurations
    include:
        - enums
        - types

seq:
    # FIXME: Will .skin files ever have more than one chunk?
    - id: magic
      contents: "SKIN"
    - id: vertices
      type: m2array<u2>
      doc: "Indexes into global (presumably 'global for this model') vertex list"
    - id: indices
      type: m2array<u2>
      doc: |
          Index into `vertices`; Can be used as an index buffer for draw calls. A
          set of 3 indices form a triangle. Triangles are right-handed, swap
          second and third index for left-handed."
    - id: bones
      type: m2array<ubyte4>
      doc: "Indexes into global (presumably 'global for this model') bone list. Standard 4-bone rig."
    - id: submeshes
      type: m2array<m2skinsection>
      doc: "Submeshes (subsets of full model)"
    - id: batches
      type: m2array<m2batch>
      doc: "Texture units/batches"
    - id: bone_count_max
      type: u4
      doc: |
          WoW takes this and divides it by the number of bones in each
          submesh, then stores the biggest one. Maximum number of bones per
          draw call for each view. Related to (old) GPU numbers of registers.
          Values seen: 256, 64, 53, 21
    - id: shadow_batches
      type: m2array<m2shadowbatch>
