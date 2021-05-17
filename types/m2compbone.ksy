types:
    m2compbone_flags:
        meta:
            xref:
                doc-ref: https://wowdev.wiki/M2#Bones

        seq:
            - id: ignore_parent_translate
              type: b1 # 0x01
            - id: ignore_parent_scale
              type: b1 # 0x02
            - id: ignore_parent_rotation
              type: b1 # 0x04
            - id: spherical_billboard
              type: b1 # 0x08
            - id: cyl_billboard_lock_x
              type: b1 # 0x10
            - id: cyl_billboard_lock_y
              type: b1 # 0x20
            - id: cyl_billboard_lock_z
              type: b1 # 0x40
            - id: unused1
              type: b1 # 0x80
            - id: unused2
              type: b1 # 0x100
            - id: transformed
              type: b1 # 0x200
            - id: kinematic_bone
              type: b1 # 0x400
              doc: "allow physics to influence this bone (MoP+)"
            - id: unused3
              type: b1 # 0x800
            - id: helmet_anim_scaled
              type: b1 # 0x1000
              doc: "set blend_modificator to helmetAnimScalingRec.m_amount"
            - id: something_sequence_id
              type: b1 # 0x2000
              doc: "parent_bone + submesh_id are a sequence id instead (BfA+)"

    m2compbone:
        seq:
            - id: key_bone_id
              type: s4
              doc: "back-reference to key bone lookup table. -1 if this is no key bone"
            - id: flags
              size: 4
              type: m2compbone_flags
            - id: parent_bone
              type: s2
              doc: "Parent bone ID or -1 if there is none"
            - id: submesh_id
              type: u2
              doc: "Mesh part ID or uDistToParent"
            # FIXME: this is also a union with CompressData
            - id: bone_name_crc
              type: u4
              doc: "for debugging only, bone names match those in key bone lookup"
            - id: translation
              type: m2track(m2track_types::c3vector)
            - id: rotation
              type: m2track(m2track_types::m2compquat)
              doc: "compressed values, default is (32767,32767,32767,65535) == (0,0,0,1) == identity"
            - id: scale
              type: m2track(m2track_types::c3vector)
            - id: pivot
              type: c3vector
              doc: "pivot point of that bone"
