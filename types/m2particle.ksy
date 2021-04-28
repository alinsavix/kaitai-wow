# WARNING WARNING WARNING
# The naming of most things in this file are subject to change. Right now,
# many of the values match the names in WMV, rather than the wowdev.wiki
# names. That will be corrected at some point. You have been warned.
#
# No, seriously, you have been warned. Twice now, even.

types:
    m2particle:
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

    # The wiki says "this is partially wrong as hell". We stole a lot of this
    # from WMV, which can actually do particle system stuff ok(ish). Probably
    # still needs a lot of validation.
    m2particle_old:
        seq:
            - id: particle_id
              type: s4
            - id: flags
              type: u4  # FIXME: parse flags
            - id: position
              type: c3vector
            - id: bone
              type: u2
            # FIXME: Call this out as actually being a union
            - id: texture
              type: u2

            # These may always be empty strings
            - id: geometry_model_filename
              type: m2array_str
            - id: recursion_model_filename
              type: m2array_str

            - id: blending_type
              type: u1
            - id: emitter_type
              type: u1
            - id: particle_color_index
              type: u2

            # FIXME: this is actually a fixed_point type (fp_2_5)
            # FIXME: Not sure if this is X[2], or X+Y
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
