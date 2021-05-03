# WARNING WARNING WARNING
# The naming of most things in this file are subject to change. Right now,
# many of the values match the names in WMV, rather than the wowdev.wiki
# names. That will be corrected at some point. You have been warned.
#
# No, seriously, you have been warned. Twice now, even.

enums:
    emitter_types:
        1: plane
        2: sphere
        3: spline
        4: bone

    blendmodes:
        0: opaque
        1: src_color_one
        2: src_alpha_one_minus_src_alpha
        3: opaque_alphaclip
        4: src_alpha_one

types:
    m2particles_flags:
        meta:
            xref:
                doc-ref: https://wowdev.wiki/M2#Particle_Flags

        seq:
            - id: lit
              type: b1
              doc: "0x01"
            - id: unknown1
              type: b1
              doc: "0x02"
            - id: unknown2
              type: b1
              doc: "0x04"
            - id: worldspace
              type: b1
              doc: "0x08"
            - id: notrail
              type: b1
              doc: "0x10"
            - id: unlightning
              type: b1
              doc: "0x20"
            - id: burst_multiplier
              type: b1
              doc: "0x40"
            - id: modelspace
              type: b1
              doc: "0x80 - Causes animation of particle emitter to carry over to particles"


            - id: unknown3
              type: b1
              doc: "0x0100"
            - id: randomspawn
              type: b1
              doc: "0x0200 - Spawn position randomized in some way?"
            - id: pinned
              type: b1
              doc: "0x0400 - Style: Pinned Particles - their quad enlarges from their creation position to where they expand"
            - id: unknown4
              type: b1
              doc: "0x0800"
            - id: nobillboard
              type: b1
              doc: "0x1000 - XYQuad Particles, align to XY axis facing Z axis"
            - id: groundclamp
              type: b1
              doc: "0x2000"
            - id: unknown5
              type: b1
              doc: "0x4000"
            - id: unknown6
              type: b1
              doc: "0x8000"


            - id: random_texture
              type: b1
              doc: "0x010000"
            - id: outward
              type: b1
              doc: |
                0x020000 - Style: Outward - particles move away from origin.
                When not set, particles start at `origin+(speed * life)`
                and move towards the origin"
            - id: inward_maybe
              type: b1
              doc: |
                0x040000 - Style: Unknown - In a large proportion of particles
                this seems to be simply the opposite of the above flag, but in
                some (e.g. voidgod.m2 or wingedlionmount.m2) both flags are true.
            - id: scale_vary_separately
              type: b1
              doc: |
                0x080000 - If set, scale_vary affects x and y separately,
                otherwise scale_vary.x is used and scale_vary.y is ignored
            - id: unknown7
              type: b1
              doc: "0x100000"
            - id: random_flipbookstart
              type: b1
              doc: "0x200000"
            - id: no_throttle_distance
              type: b1
              doc: "0x400000"
            - id: compressed_gravity
              type: b1
              doc: "0x800000 - gravity values are compressed vectors instead of Z-axis values"


            - id: bone_generator
              type: b1
              doc: "0x01000000 - bone generator = bone, not joint"
            - id: unknown8
              type: b1
              doc: "0x02000000"
            - id: no_throttle_distance2
              type: b1
              doc: "0x04000000 - see no_throttle_distance, unclear if this is 0x400000 or 0x4000000"
            - id: unknown9
              type: b1
              doc: "0x08000000"

            - id: multi_texture
              type: b1
              doc: "0x10000000 - uses multi-texturing"
            - id: unknown10
              type: b1
              doc: "0x20000000"
            - id: unknown11
              type: b1
              doc: "0x40000000"
            - id: unknown12
              type: b1
              doc: "0x80000000"


    m2particle:
        meta:
            xref:
                doc-ref: https://wowdev.wiki/M2#M2Particle_.28Cata.2B.29

        seq:
            - id: old
              type: m2particle_old
            - id: multi_texture_param0
              type: vector_2fp_6_9
              repeat: expr
              repeat-expr: 2
            - id: multi_texture_param1
              type: vector_2fp_6_9
              repeat: expr
              repeat-expr: 2


    # This struct is based off of a number of different sources, some intuition,
    # and a couple of animal sacrifices. It *seems* to be correct now, but it's
    # quite possible we're wrong on that.
    m2particle_old:
        meta:
            xref:
                doc-ref: https://wowdev.wiki/M2#M2ParticleOld

        seq:
            - id: particle_id
              type: s4

            - id: flags
              type: m2particles_flags
            - id: position
              type: c3vector
              doc: "Position of particle, relative to `bone` field"
            - id: bone
              type: u2

            # FIXME: Call this out as actually being a union. I think we want
            # the packed version of this (used here), though we should verify
            # we have the textures in the right order.
            - id: texture_0
              type: b5
            - id: texture_1
              type: b5
            - id: texture_2
              type: b5

            # These may always be empty strings
            - id: geometry_model_filename
              type: m2array_str
            - id: recursion_model_filename
              type: m2array_str

            - id: blending_type
              type: u1
              enum: blendmodes
            - id: emitter_type
              type: u1
              enum: emitter_types
            - id: particle_color_index
              type: u2

            # FIXME: these are actually a fixed_point type (fp_2_5)
            - id: multi_texture_param_x
              type: u1
            - id: multi_texture_param_y
              type: u1

            - id: texture_tile_rotation
              type: s2
            - id: texture_dimensions_rows
              type: u2
            - id: texture_dimensions_columns
              type: u2

            - id: emission_speed
              type: m2track(m2track_types::float)
            - id: speed_variation
              type: m2track(m2track_types::float)
            - id: vertical_range
              type: m2track(m2track_types::float)
            - id: horizontal_range
              type: m2track(m2track_types::float)
            - id: gravity
              type: m2track(m2track_types::float)
            - id: lifespan
              type: m2track(m2track_types::float)

            # WMV says "unknown"
            - id: lifespan_vary
              type: f4

            - id: emission_rate
              type: m2track(m2track_types::float)

            # WMV says "unknown"
            - id: emission_rate_vary
              type: f4

            - id: emission_area_length
              type: m2track(m2track_types::float)
            - id: emission_area_width
              type: m2track(m2track_types::float)
            - id: z_source
              type: m2track(m2track_types::float)

            # WMV then has `ModelParticleParams p`
            - id: p
              type: model_particle_params

            - id: enabled_in
              type: m2track(m2track_types::uint16)


    # Named to match up with WMV structs, while figuring this out
    model_particle_params:
        seq:
            - id: colors
              type: fblock(m2array_types::frgb)
            - id: opacity
              type: fblock(m2array_types::uint16)
            - id: sizes
              type: fblock(m2array_types::c2vector)
            - id: d
              type: u4
              repeat: expr
              repeat-expr: 2
            - id: intensity
              type: fblock(m2array_types::uint16)
            - id: unk2
              type: fblock(m2array_types::uint16)
            - id: unk
              type: f4
              repeat: expr
              repeat-expr: 3
            - id: scales
              type: c3vector
            - id: slowdown
              type: f4
            - id: unknown1
              type: f4
              repeat: expr
              repeat-expr: 2
            - id: rotation
              type: f4
            - id: unknown2
              type: f4
              repeat: expr
              repeat-expr: 2
            - id: rot1
              type: c3vector
            - id: rot2
              type: c3vector
            - id: trans
              type: c3vector
            - id: f2
              type: f4
              repeat: expr
              repeat-expr: 4
            - id: unknown_reference
              type: m2array(m2array_types::todo)


    # FIXME: Is this best defined here? Or somewhere else?
    m2extended_particle:
        seq:
            - id: z_source
              type: f4
            - id: unknown1
              type: u4
            - id: unknown2
              type: u4
            - id: unknown3
              type: m2parttrack(m2array_types::fixed16)
