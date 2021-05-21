# FIXME: Pretty sure the flags are fucked up in one way or another
types:
    md20_global_flags:
        seq:
            - id: tilt_x
              type: b1  # 0x01
            - id: tilt_y
              type: b1  # 0x02
            - id: unk_0x04
              type: b1  # 0x04
            - id: use_texture_combiner_combos
              type: b1  # 0x08

            - id: unk_0x10
              type: b1  # 0x10
            - id: load_phys_data
              type: b1  # 0x20
            - id: unk_0x40
              type: b1  # 0x40
            - id: unk_0x80
              type: b1  # 0x80

            - id: camera_related
              type: b1  # 0x0100
            - id: new_particle_record
              type: b1  # 0x0200
            - id: unk_0x400
              type: b1  # 0x0400
            - id: texture_transforms_use_bone_sequences
              type: b1  # 0x0800

            - id: unk_0x1000
              type: b1  # 0x1000
            - id: unk_0x2000
              type: b1  # 0x2000
            - id: unk_0x4000
              type: b1  # 0x4000
            - id: unk_0x8000
              type: b1  # 0x8000

            - id: unk_0x10000
              type: b1  # 0x010000
            - id: unk_0x20000
              type: b1  # 0x020000
            - id: unk_0x40000
              type: b1  # 0x040000
            - id: unk_0x80000
              type: b1  # 0x080000

            - id: unk_0x100000
              type: b1  # 0x100000
            - id: unk_0x200000
              type: b1  # 0x200000
            - id: unused_0x400000
              type: b1  # 0x400000
            - id: unused_0x800000
              type: b1  # 0x800000

            - id: unused_0x01000000
              type: b1  # 0x01000000
            - id: unused_0x02000000
              type: b1  # 0x02000000
            - id: unused_0x04000000
              type: b1  # 0x04000000
            - id: unused_0x08000000
              type: b1  # 0x08000000

            - id: unused_0x10000000
              type: b1  # 0x10000000
            - id: unused_0x20000000
              type: b1  # 0x20000000
            - id: unused_0x40000000
              type: b1  # 0x40000000
            - id: unused_0x80000000
              type: b1  # 0x80000000


    chunk_md20:
        seq:
            - id: magic2
              contents: "MD20"
            - id: version
              type: u4
              enum: wow_versions
            - id: name
              type: m2array<str>
              doc: "should be globally unique"
            - id: flags
              type: md20_global_flags
              size: 4
            # - id: global_loops
            #   type: m2array(m2array_types::m2loop)
            - id: global_loops
              type: m2array<m2loop>

            # - id: sequences
            #   type: m2array(m2array_types::m2sequence)
            # - id: sequence_idx_hash_by_id
            #   type: m2array(m2array_types::uint16)
            - id: sequences
              type: m2array<m2sequence>
            - id: sequence_idx_hash_by_id
              type: m2array<u2>

            - id: bones
              type: m2array<m2compbone>
            - id: bone_indices_by_id   # FIXME: maybe 'boneFileDataIDs'?
              type: m2array<u2>

            - id: vertices
              type: m2array<m2vertex>

            # used in .skin file, supposedly
            - id: num_skin_profiles
              type: u4

            - id: colors
              type: m2array<m2color>
              doc: "Color and alpha animations definitions"
            - id: textures
              type: m2array<m2texture>
            - id: texture_weights
              type: m2array<m2textureweight>
              doc: "Transparency of textures"
            - id: texture_transforms
              type: m2array<m2texturetransform>

            # alternate name "texture_indices_by_id"
            - id: texture_replaceable_lookup
              type: m2array<u2>

            # blending modes / render flags
            - id: materials
              type: m2array<m2material>

            # alternate name "bone_lookup_table"
            - id: bone_lookup
              type: m2array<u2>

            # alternate name "texture_lookup_table"
            - id: texture_lookup
              type: m2array<u2>

            # alternate name "texture_transform_bone_map"
            - id: texture_unit_lookup  # FIXME: verify
              type: m2array<u2>

            # alternate name "texture_weight_combos"
            - id: texture_transparency_lookup  # FIXME: verify
              type: m2array<u2>

            # alternate name "texture_transform_combos"
            - id: uvanimlookup
              type: m2array<u2>

            # FIXME: wow.tools also has angle & length -- wherefrom?
            - id: bounding_box
              type: caabox
            - id: bounding_sphere_radius
              type: f4
            - id: collision_box
              type: caabox
            - id: collision_sphere_radius
              type: f4
            - id: collision_indices  # FIXME: verify with wow.tools and in general
              type: m2array<u2>
            - id: collision_positions  # FIXME: verify with wow.tools and in general
              type: m2array<c3vector>
            - id: collision_face_normals  # FIXME: verify with wow.tools and in general
              type: m2array<c3vector>
            - id: attachments
              type: m2array<m2attachment>
            - id: attachment_lookup
              type: m2array<u2>
            - id: events
              type: m2array<m2event>
            - id: lights
              type: m2array<m2light>
            - id: cameras
              type: m2array<m2camera>
            - id: camera_lookup  # FIXME: verify with wow.tools
              type: m2array<u2>
            - id: ribbon_emitters
              type: m2array<m2ribbon>
            - id: particle_emitters
              type: m2array<m2particle>
            - id: texture_combiner_combos
              type: m2array<u2>
              if: flags.use_texture_combiner_combos
