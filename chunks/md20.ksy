# FIXME: Pretty sure the flags are fucked up in one way or another
types:
    md20_global_flags:
        seq:
            - id: flag_tilt_x
              type: b1
            - id: flag_tilt_y
              type: b1
            - id: flag_unk_0x04
              type: b1
            - id: flag_use_texture_combiner_combos
              type: b1
            - id: flag_unk_0x10
              type: b1
            - id: flag_load_phys_data
              type: b1
            - id: flag_unk_0x40
              type: b1
            - id: flag_unk_0x80
              type: b1
            - id: flag_camera_related
              type: b1
            - id: flag_new_particle_record
              type: b1
            - id: flag_unk_0x400
              type: b1
            - id: flag_texture_transforms_use_bone_sequences
              type: b1
            - id: flag_unk_0x1000
              type: b1
            - id: flag_unk_0x2000
              type: b1
            - id: flag_unk_0x4000
              type: b1
            - id: flag_unk_0x8000
              type: b1
            - id: flag_unk_0x10000
              type: b1
            - id: flag_unk_0x20000
              type: b1
            - id: flag_unk_0x40000
              type: b1
            - id: flag_unk_0x80000
              type: b1
            - id: flag_unk_0x100000
              type: b1
            - id: flag_unk_0x200000
              type: b1

    chunk_md20:
        seq:
            - id: magic2
              contents: "MD20"
            - id: version
              type: u4
              enum: wow_versions
            - id: name
              type: m2array_str
              doc: "should be globally unique"
            - id: global_flags
              type: md20_global_flags
              size: 4 # FIXME: Is this right?
            - id: global_loops
              type: m2array(m2array_types::m2loop)

            - id: sequences
              type: m2array(m2array_types::m2sequence)
            - id: sequence_idx_hash_by_id
              type: m2array(m2array_types::uint16)

            - id: bones
              type: m2array(m2array_types::m2compbone)
            - id: bone_indices_by_id
              type: m2array(m2array_types::uint16)

            - id: vertices
              type: m2array(m2array_types::m2vertex)

            # used in .skin file, supposedly
            - id: num_skin_profiles
              type: u4

            - id: colors
              type: m2array(m2array_types::m2color)
              doc: "Color and alpha animations definitions"
            - id: textures
              type: m2array(m2array_types::m2texture)
            - id: texture_weights
              type: m2array(m2array_types::m2textureweight)
              doc: "Transparency of textures"
            - id: texture_transforms
              type: m2array(m2array_types::m2texturetransform)

            # alternate name "replaceable_texture_lookup"
            - id: texture_indices_by_id
              type: m2array(m2array_types::uint16)

            # blending modes / render flags
            - id: materials
              type: m2array(m2array_types::m2material)

            # alternate name "bone_lookup_table"
            - id: bone_combos
              type: m2array(m2array_types::uint16)

            # alternate name "texture_lookup_table"
            - id: texture_combos
              type: m2array(m2array_types::uint16)

            # alternate name "tex_unit_lookup_table"
            - id: texture_transform_bone_map
              type: m2array(m2array_types::uint16)

            # alternate name "transparency_lookup_table"
            - id: texture_weight_combos
              type: m2array(m2array_types::uint16)

            # alternate name "texture_transforms_lookup_table"
            - id: texture_transform_combos
              type: m2array(m2array_types::uint16)

            - id: bounding_box
              type: caabox
            - id: bounding_sphere_radius
              type: f4
            - id: collision_box
              type: caabox
            - id: collision_sphere_radius
              type: f4
            - id: collision_indices
              type: m2array(m2array_types::uint16)
            - id: collision_positions
              type: m2array(m2array_types::c3vector)
            - id: collision_face_normals
              type: m2array(m2array_types::c3vector)
            - id: attachments
              type: m2array(m2array_types::m2attachment)
            - id: attachment_indices_by_id
              type: m2array(m2array_types::uint16)
            - id: events
              type: m2array(m2array_types::m2event)
            - id: lights
              type: m2array(m2array_types::m2light)
            - id: cameras
              type: m2array(m2array_types::m2camera)
            - id: camera_indices_by_id
              type: m2array(m2array_types::uint16)
            - id: ribbon_emitters
              type: m2array(m2array_types::m2ribbon)
            - id: particle_emitters
              type: m2array(m2array_types::m2particle)
            - id: texture_combiner_combos
              type: m2array(m2array_types::uint16)
              if: global_flags.flag_use_texture_combiner_combos
