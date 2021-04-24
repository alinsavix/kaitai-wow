types:
    m2compbone:
        seq:
            - id: key_bone_id
              type: s4
            - id: flags # FIXME
              type: u4
            - id: parent_bone
              type: s2
            - id: submesh_id
              type: u2
            - id: bone_name_crc
              -orig-id: boneNameCRC
              type: u4
            - id: translation
              type: m2track(m2track_types::c3vector)
            - id: rotation
              type: m2track(m2track_types::m2compquat)
            - id: scale
              type: m2track(m2track_types::c3vector)
            - id: pivot
              type: c3vector
