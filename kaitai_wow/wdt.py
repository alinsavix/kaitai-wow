# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Wdt(KaitaiStruct):

    class KeyBoneNames(Enum):
        arm_l = 0
        arm_r = 1
        shoulder_l = 2
        shoulder_r = 3
        spine_low = 4
        waist = 5
        head = 6
        jaw = 7
        index_finger_r = 8
        middle_finger_r = 9
        pinky_finger_r = 10
        ring_finger_r = 11
        thumb_r = 12
        index_finger_l = 13
        middle_finger_l = 14
        pinky_finger_l = 15
        ring_finger_l = 16
        thumb_l = 17
        dollar_b_t_h = 18
        dollar_c_s_r = 19
        dollar_c_s_l = 20
        breath = 21
        name = 22
        name_mount = 23
        dollar_c_h_d = 24
        dollar_c_c_h = 25
        root = 26
        wheel1 = 27
        wheel2 = 28
        wheel3 = 29
        wheel4 = 30
        wheel5 = 31
        wheel6 = 32
        wheel7 = 33
        wheel8 = 34
        face_attenuation = 35
        cape_parent = 36
        cape_child1 = 37
        cape_child2 = 38
        cape_child3 = 39
        cape_child4 = 40
        tabard_parent = 43
        tabard_child1 = 44
        tabard_child2 = 45
        unk_head_top = 46
        unk_head_top2 = 47
        upper_body_parent = 48
        neck_parent = 49
        neck_child1 = 50
        lower_body_parent = 51
        buckle = 52
        chest = 53
        main = 54
        leg_r = 55
        leg_l = 56
        knee_r = 57
        knee_l = 58
        foot_l = 59
        foot_r = 60
        elbow_r = 61
        elbow_l = 62
        unk_elbow_l_child = 63
        hand_r = 64
        hand_l = 65
        weapon_r = 66
        weapon_l = 67
        unk_wrist_l_child = 68
        unk_wrist_r_child = 69
        knee_r_upper_rig = 70
        knee_l_upper_rig = 71
        arm_r_2 = 72
        arm_l_2 = 73
        elbow_r_upper_rig = 74
        elbow_l_upper_rig = 75
        forearm_r = 76
        forearm_l = 77
        wrist_r_upper_rig = 78
        wrist_l_upper_rig = 79

    class M2materialBlendmodes(Enum):
        m2blend_opaque = 0
        m2blend_alpha_key = 1
        m2blend_alpha = 2
        m2blend_no_alpha_add = 3
        m2blend_add = 4
        m2blend_mod = 5
        m2blend_mod2x = 6
        m2blend_blendadd = 7

    class M2textureTypes(Enum):
        normal = 0
        component_skin = 1
        component_object_skin = 2
        component_weapon_blade = 3
        component_weapon_handle = 4
        component_environment = 5
        component_char_hair = 6
        component_char_facial_hair = 7
        component_skin_extra = 8
        component_ui_skin = 9
        component_tauren_mane = 10
        component_monster_1 = 11
        component_monster_2 = 12
        component_monster_3 = 13
        component_item_icon = 14
        guild_color_background = 15
        guild_color_emblem = 16
        guild_color_border = 17
        guild_emblem = 18
        character_eyes = 19
        character_accessory = 20
        character_skin_secondary = 21
        character_hair_secondary = 22
        character_armor_secondary = 23
        character_unknown = 24

    class Blendmodes(Enum):
        opaque = 0
        src_color_one = 1
        src_alpha_one_minus_src_alpha = 2
        opaque_alphaclip = 3
        src_alpha_one = 4

    class M2arrayTypes(Enum):
        todo = 0
        uint8 = 1
        uint16 = 2
        uint32 = 3
        fixed16 = 4
        float = 5
        ubyte4 = 6
        int8 = 7
        int16 = 8
        c2vector = 21
        c3vector = 22
        c4vector = 23
        c4quaternion = 24
        frgb = 25
        m2sequencefallback = 101
        m2compbone = 102
        m2vertex = 103
        m2color = 104
        m2texture = 105
        m2textureweight = 106
        m2texturetransform = 107
        m2material = 108
        m2attachment = 109
        m2event = 110
        m2light = 111
        m2camera = 112
        m2ribbon = 113
        m2particle = 114
        m2loop = 115
        m2sequence = 116
        m2skinsection = 117
        m2batch = 118
        m2shadowbatch = 119
        m2compquat = 120
        m2extended_particle = 121
        pgd1_entry = 122
        m2array_uint32 = 201
        m2array_m2compquat = 202
        m2array_c2vector = 203
        m2array_c3vector = 204
        m2array_c4vector = 205
        m2array_c4quaternion = 206
        m2array_fixed16 = 207
        m2array_uint8 = 208
        m2array_float = 209
        m2array_uint16 = 210

    class M2trackInterpolationTypes(Enum):
        interpolate_const = 0
        interpolate_linear = 1
        interpolate_cubic_bezier_spline = 2
        interpolate_cubic_hermite_spline = 3

    class M2trackTypes(Enum):
        todo = 0
        uint8 = 1
        uint16 = 2
        fixed16 = 4
        float = 5
        c2vector = 21
        c3vector = 22
        c4vector = 23
        c4quaternion = 24
        m2compquat = 25

    class AnimNames(Enum):
        stand = 0
        death = 1
        spell = 2
        stop = 3
        walk = 4
        run = 5
        dead = 6
        rise = 7
        stand_wound = 8
        combat_wound = 9
        combat_critical = 10
        shuffle_left = 11
        shuffle_right = 12
        walk_backwards = 13
        stun = 14
        hands_closed = 15
        attack_unarmed = 16
        attack_1h = 17
        attack_2h = 18
        attack_2h_l = 19
        parry_unarmed = 20
        parry_1h = 21
        parry_2h = 22
        parry_2h_l = 23
        shield_block = 24
        ready_unarmed = 25
        ready_1h = 26
        ready_2h = 27
        ready_2h_l = 28
        ready_bow = 29
        dodge = 30
        spell_precast = 31
        spell_cast = 32
        spell_cast_area = 33
        npc_welcome = 34
        npc_goodbye = 35
        block = 36
        jump_start = 37
        jump = 38
        jump_end = 39
        fall = 40
        swim_idle = 41
        swim = 42
        swim_left = 43
        swim_right = 44
        swim_backwards = 45
        attack_bow = 46
        fire_bow = 47
        ready_rifle = 48
        attack_rifle = 49
        loot = 50
        ready_spell_directed = 51
        ready_spell_omni = 52
        spell_cast_directed = 53
        spell_cast_omni = 54
        battle_roar = 55
        ready_ability = 56
        special_1h = 57
        special_2h = 58
        shield_bash = 59
        emote_talk = 60
        emote_eat = 61
        emote_work = 62
        emote_use_standing = 63
        emote_talk_exclamation = 64
        emote_talk_question = 65
        emote_bow = 66
        emote_wave = 67
        emote_cheer = 68
        emote_dance = 69
        emote_laugh = 70
        emote_sleep = 71
        emote_sit_ground = 72
        emote_rude = 73
        emote_roar = 74
        emote_kneel = 75
        emote_kiss = 76
        emote_cry = 77
        emote_chicken = 78
        emote_beg = 79
        emote_applaud = 80
        emote_shout = 81
        emote_flex = 82
        emote_shy = 83
        emote_point = 84
        attack_1h_pierce = 85
        attack_2h_loose_pierce = 86
        attack_off = 87
        attack_off_pierce = 88
        sheath = 89
        hip_sheath = 90
        mount = 91
        run_right = 92
        run_left = 93
        mount_special = 94
        kick = 95
        sit_ground_down = 96
        sit_ground = 97
        sit_ground_up = 98
        sleep_down = 99
        sleep = 100
        sleep_up = 101
        sit_chair_low = 102
        sit_chair_med = 103
        sit_chair_high = 104
        load_bow = 105
        load_rifle = 106
        attack_thrown = 107
        ready_thrown = 108
        hold_bow = 109
        hold_rifle = 110
        hold_thrown = 111
        load_thrown = 112
        emote_salute = 113
        kneel_start = 114
        kneel_loop = 115
        kneel_end = 116
        attack_unarmed_off = 117
        special_unarmed = 118
        stealth_walk = 119
        stealth_stand = 120
        knockdown = 121
        eating_loop = 122
        use_standing_loop = 123
        channel_cast_directed = 124
        channel_cast_omni = 125
        whirlwind = 126
        birth = 127
        use_standing_start = 128
        use_standing_end = 129
        creature_special = 130
        drown = 131
        drowned = 132
        fishing_cast = 133
        fishing_loop = 134
        fly = 135
        emote_work_no_sheathe = 136
        emote_stun_no_sheathe = 137
        emote_use_standing_no_sheathe = 138
        spell_sleep_down = 139
        spell_kneel_start = 140
        spell_kneel_loop = 141
        spell_kneel_end = 142
        sprint = 143
        in_flight = 144
        spawn = 145
        close = 146
        closed = 147
        open = 148
        opened = 149
        destroy = 150
        destroyed = 151
        rebuild = 152
        custom0 = 153
        custom1 = 154
        custom2 = 155
        custom3 = 156
        despawn = 157
        hold = 158
        decay = 159
        bow_pull = 160
        bow_release = 161
        ship_start = 162
        ship_moving = 163
        ship_stop = 164
        group_arrow = 165
        arrow = 166
        corpse_arrow = 167
        guide_arrow = 168
        sway = 169
        druid_cat_pounce = 170
        druid_cat_rip = 171
        druid_cat_rake = 172
        druid_cat_ravage = 173
        druid_cat_claw = 174
        druid_cat_cower = 175
        druid_bear_swipe = 176
        druid_bear_bite = 177
        druid_bear_maul = 178
        druid_bear_bash = 179
        dragon_tail = 180
        dragon_stomp = 181
        dragon_spit = 182
        dragon_spit_hover = 183
        dragon_spit_fly = 184
        emote_yes = 185
        emote_no = 186
        jump_land_run = 187
        loot_hold = 188
        loot_up = 189
        stand_high = 190
        impact = 191
        lift_off = 192
        hover = 193
        succubus_entice = 194
        emote_train = 195
        emote_dead = 196
        emote_dance_once = 197
        deflect = 198
        emote_eat_no_sheathe = 199
        land = 200
        submerge = 201
        submerged = 202
        cannibalize = 203
        arrow_birth = 204
        group_arrow_birth = 205
        corpse_arrow_birth = 206
        guide_arrow_birth = 207
        emote_talk_no_sheathe = 208
        emote_point_no_sheathe = 209
        emote_salute_no_sheathe = 210
        emote_dance_special = 211
        mutilate = 212
        custom_spell01 = 213
        custom_spell02 = 214
        custom_spell03 = 215
        custom_spell04 = 216
        custom_spell05 = 217
        custom_spell06 = 218
        custom_spell07 = 219
        custom_spell08 = 220
        custom_spell09 = 221
        custom_spell10 = 222
        stealth_run = 223
        emerge = 224
        cower = 225
        grab = 226
        grab_closed = 227
        grab_thrown = 228
        fly_stand = 229
        fly_death = 230
        fly_spell = 231
        fly_stop = 232
        fly_walk = 233
        fly_run = 234
        fly_dead = 235
        fly_rise = 236
        fly_stand_wound = 237
        fly_combat_wound = 238
        fly_combat_critical = 239
        fly_shuffle_left = 240
        fly_shuffle_right = 241
        fly_walk_backwards = 242
        fly_stun = 243
        fly_hands_closed = 244
        fly_attack_unarmed = 245
        fly_attack_1h = 246
        fly_attack_2h = 247
        fly_attack_2h_l = 248
        fly_parry_unarmed = 249
        fly_parry_1h = 250
        fly_parry_2h = 251
        fly_parry_2h_l = 252
        fly_shield_block = 253
        fly_ready_unarmed = 254
        fly_ready_1h = 255
        fly_ready_2h = 256
        fly_ready_2h_l = 257
        fly_ready_bow = 258
        fly_dodge = 259
        fly_spell_precast = 260
        fly_spell_cast = 261
        fly_spell_cast_area = 262
        fly_npc_welcome = 263
        fly_npc_goodbye = 264
        fly_block = 265
        fly_jump_start = 266
        fly_jump = 267
        fly_jump_end = 268
        fly_fall = 269
        fly_swim_idle = 270
        fly_swim = 271
        fly_swim_left = 272
        fly_swim_right = 273
        fly_swim_backwards = 274
        fly_attack_bow = 275
        fly_fire_bow = 276
        fly_ready_rifle = 277
        fly_attack_rifle = 278
        fly_loot = 279
        fly_ready_spell_directed = 280
        fly_ready_spell_omni = 281
        fly_spell_cast_directed = 282
        fly_spell_cast_omni = 283
        fly_battle_roar = 284
        fly_ready_ability = 285
        fly_special_1h = 286
        fly_special_2h = 287
        fly_shield_bash = 288
        fly_emote_talk = 289
        fly_emote_eat = 290
        fly_emote_work = 291
        fly_emote_use_standing = 292
        fly_emote_talk_exclamation = 293
        fly_emote_talk_question = 294
        fly_emote_bow = 295
        fly_emote_wave = 296
        fly_emote_cheer = 297
        fly_emote_dance = 298
        fly_emote_laugh = 299
        fly_emote_sleep = 300
        fly_emote_sit_ground = 301
        fly_emote_rude = 302
        fly_emote_roar = 303
        fly_emote_kneel = 304
        fly_emote_kiss = 305
        fly_emote_cry = 306
        fly_emote_chicken = 307
        fly_emote_beg = 308
        fly_emote_applaud = 309
        fly_emote_shout = 310
        fly_emote_flex = 311
        fly_emote_shy = 312
        fly_emote_point = 313
        fly_attack_1h_pierce = 314
        fly_attack_2h_loose_pierce = 315
        fly_attack_off = 316
        fly_attack_off_pierce = 317
        fly_sheath = 318
        fly_hip_sheath = 319
        fly_mount = 320
        fly_run_right = 321
        fly_run_left = 322
        fly_mount_special = 323
        fly_kick = 324
        fly_sit_ground_down = 325
        fly_sit_ground = 326
        fly_sit_ground_up = 327
        fly_sleep_down = 328
        fly_sleep = 329
        fly_sleep_up = 330
        fly_sit_chair_low = 331
        fly_sit_chair_med = 332
        fly_sit_chair_high = 333
        fly_load_bow = 334
        fly_load_rifle = 335
        fly_attack_thrown = 336
        fly_ready_thrown = 337
        fly_hold_bow = 338
        fly_hold_rifle = 339
        fly_hold_thrown = 340
        fly_load_thrown = 341
        fly_emote_salute = 342
        fly_kneel_start = 343
        fly_kneel_loop = 344
        fly_kneel_end = 345
        fly_attack_unarmed_off = 346
        fly_special_unarmed = 347
        fly_stealth_walk = 348
        fly_stealth_stand = 349
        fly_knockdown = 350
        fly_eating_loop = 351
        fly_use_standing_loop = 352
        fly_channel_cast_directed = 353
        fly_channel_cast_omni = 354
        fly_whirlwind = 355
        fly_birth = 356
        fly_use_standing_start = 357
        fly_use_standing_end = 358
        fly_creature_special = 359
        fly_drown = 360
        fly_drowned = 361
        fly_fishing_cast = 362
        fly_fishing_loop = 363
        fly_fly = 364
        fly_emote_work_no_sheathe = 365
        fly_emote_stun_no_sheathe = 366
        fly_emote_use_standing_no_sheathe = 367
        fly_spell_sleep_down = 368
        fly_spell_kneel_start = 369
        fly_spell_kneel_loop = 370
        fly_spell_kneel_end = 371
        fly_sprint = 372
        fly_in_flight = 373
        fly_spawn = 374
        fly_close = 375
        fly_closed = 376
        fly_open = 377
        fly_opened = 378
        fly_destroy = 379
        fly_destroyed = 380
        fly_rebuild = 381
        fly_custom0 = 382
        fly_custom1 = 383
        fly_custom2 = 384
        fly_custom3 = 385
        fly_despawn = 386
        fly_hold = 387
        fly_decay = 388
        fly_bow_pull = 389
        fly_bow_release = 390
        fly_ship_start = 391
        fly_ship_moving = 392
        fly_ship_stop = 393
        fly_group_arrow = 394
        fly_arrow = 395
        fly_corpse_arrow = 396
        fly_guide_arrow = 397
        fly_sway = 398
        fly_druid_cat_pounce = 399
        fly_druid_cat_rip = 400
        fly_druid_cat_rake = 401
        fly_druid_cat_ravage = 402
        fly_druid_cat_claw = 403
        fly_druid_cat_cower = 404
        fly_druid_bear_swipe = 405
        fly_druid_bear_bite = 406
        fly_druid_bear_maul = 407
        fly_druid_bear_bash = 408
        fly_dragon_tail = 409
        fly_dragon_stomp = 410
        fly_dragon_spit = 411
        fly_dragon_spit_hover = 412
        fly_dragon_spit_fly = 413
        fly_emote_yes = 414
        fly_emote_no = 415
        fly_jump_land_run = 416
        fly_loot_hold = 417
        fly_loot_up = 418
        fly_stand_high = 419
        fly_impact = 420
        fly_lift_off = 421
        fly_hover = 422
        fly_succubus_entice = 423
        fly_emote_train = 424
        fly_emote_dead = 425
        fly_emote_dance_once = 426
        fly_deflect = 427
        fly_emote_eat_no_sheathe = 428
        fly_land = 429
        fly_submerge = 430
        fly_submerged = 431
        fly_cannibalize = 432
        fly_arrow_birth = 433
        fly_group_arrow_birth = 434
        fly_corpse_arrow_birth = 435
        fly_guide_arrow_birth = 436
        fly_emote_talk_no_sheathe = 437
        fly_emote_point_no_sheathe = 438
        fly_emote_salute_no_sheathe = 439
        fly_emote_dance_special = 440
        fly_mutilate = 441
        fly_custom_spell01 = 442
        fly_custom_spell02 = 443
        fly_custom_spell03 = 444
        fly_custom_spell04 = 445
        fly_custom_spell05 = 446
        fly_custom_spell06 = 447
        fly_custom_spell07 = 448
        fly_custom_spell08 = 449
        fly_custom_spell09 = 450
        fly_custom_spell10 = 451
        fly_stealth_run = 452
        fly_emerge = 453
        fly_cower = 454
        fly_grab = 455
        fly_grab_closed = 456
        fly_grab_thrown = 457
        to_fly = 458
        to_hover = 459
        to_ground = 460
        fly_to_fly = 461
        fly_to_hover = 462
        fly_to_ground = 463
        settle = 464
        fly_settle = 465
        death_start = 466
        death_loop = 467
        death_end = 468
        fly_death_start = 469
        fly_death_loop = 470
        fly_death_end = 471
        death_end_hold = 472
        fly_death_end_hold = 473
        strangulate = 474
        fly_strangulate = 475
        ready_joust = 476
        load_joust = 477
        hold_joust = 478
        fly_ready_joust = 479
        fly_load_joust = 480
        fly_hold_joust = 481
        attack_joust = 482
        fly_attack_joust = 483
        reclined_mount = 484
        fly_reclined_mount = 485
        to_altered = 486
        from_altered = 487
        fly_to_altered = 488
        fly_from_altered = 489
        in_stocks = 490
        fly_in_stocks = 491
        vehicle_grab = 492
        vehicle_throw = 493
        fly_vehicle_grab = 494
        fly_vehicle_throw = 495
        to_altered_post_swap = 496
        from_altered_post_swap = 497
        fly_to_altered_post_swap = 498
        fly_from_altered_post_swap = 499
        reclined_mount_passenger = 500
        fly_reclined_mount_passenger = 501
        carry_2h = 502
        carried_2h = 503
        fly_carry_2h = 504
        fly_carried_2h = 505
        emote_sniff = 506
        emote_fly_sniff = 507
        attack_fist_1h = 508
        fly_attack_fist_1h = 509
        attack_fist_1h_off = 510
        fly_attack_fist_1h_off = 511
        parry_fist_1h = 512
        fly_parry_fist_1h = 513
        ready_fist_1h = 514
        fly_ready_fist_1h = 515
        special_fist_1h = 516
        fly_special_fist_1h = 517
        emote_read_start = 518
        fly_emote_read_start = 519
        emote_read_loop = 520
        fly_emote_read_loop = 521
        emote_read_end = 522
        fly_emote_read_end = 523
        swim_run = 524
        fly_swim_run = 525
        swim_walk = 526
        fly_swim_walk = 527
        swim_walk_backwards = 528
        fly_swim_walk_backwards = 529
        swim_sprint = 530
        fly_swim_sprint = 531
        mount_swim_idle = 532
        fly_mount_swim_idle = 533
        mount_swim_backwards = 534
        fly_mount_swim_backwards = 535
        mount_swim_left = 536
        fly_mount_swim_left = 537
        mount_swim_right = 538
        fly_mount_swim_right = 539
        mount_swim_run = 540
        fly_mount_swim_run = 541
        mount_swim_sprint = 542
        fly_mount_swim_sprint = 543
        mount_swim_walk = 544
        fly_mount_swim_walk = 545
        mount_swim_walk_backwards = 546
        fly_mount_swim_walk_backwards = 547
        mount_flight_idle = 548
        fly_mount_flight_idle = 549
        mount_flight_backwards = 550
        fly_mount_flight_backwards = 551
        mount_flight_left = 552
        fly_mount_flight_left = 553
        mount_flight_right = 554
        fly_mount_flight_right = 555
        mount_flight_run = 556
        fly_mount_flight_run = 557
        mount_flight_sprint = 558
        fly_mount_flight_sprint = 559
        mount_flight_walk = 560
        fly_mount_flight_walk = 561
        mount_flight_walk_backwards = 562
        fly_mount_flight_walk_backwards = 563
        mount_flight_start = 564
        fly_mount_flight_start = 565
        mount_swim_start = 566
        fly_mount_swim_start = 567
        mount_swim_land = 568
        fly_mount_swim_land = 569
        mount_swim_land_run = 570
        fly_mount_swim_land_run = 571
        mount_flight_land = 572
        fly_mount_flight_land = 573
        mount_flight_land_run = 574
        fly_mount_flight_land_run = 575
        ready_blow_dart = 576
        fly_ready_blow_dart = 577
        load_blow_dart = 578
        fly_load_blow_dart = 579
        hold_blow_dart = 580
        fly_hold_blow_dart = 581
        attack_blow_dart = 582
        fly_attack_blow_dart = 583
        carriage_mount = 584
        fly_carriage_mount = 585
        carriage_passenger_mount = 586
        fly_carriage_passenger_mount = 587
        carriage_mount_attack = 588
        fly_carriage_mount_attack = 589
        bar_tend_stand = 590
        fly_bar_tend_stand = 591
        bar_server_walk = 592
        fly_bar_server_walk = 593
        bar_server_run = 594
        fly_bar_server_run = 595
        bar_server_shuffle_left = 596
        fly_bar_server_shuffle_left = 597
        bar_server_shuffle_right = 598
        fly_bar_server_shuffle_right = 599
        bar_tend_emote_talk = 600
        fly_bar_tend_emote_talk = 601
        bar_tend_emote_point = 602
        fly_bar_tend_emote_point = 603
        bar_server_stand = 604
        fly_bar_server_stand = 605
        bar_sweep_walk = 606
        fly_bar_sweep_walk = 607
        bar_sweep_run = 608
        fly_bar_sweep_run = 609
        bar_sweep_shuffle_left = 610
        fly_bar_sweep_shuffle_left = 611
        bar_sweep_shuffle_right = 612
        fly_bar_sweep_shuffle_right = 613
        bar_sweep_emote_talk = 614
        fly_bar_sweep_emote_talk = 615
        bar_patron_sit_emote_point = 616
        fly_bar_patron_sit_emote_point = 617
        mount_self_idle = 618
        fly_mount_self_idle = 619
        mount_self_walk = 620
        fly_mount_self_walk = 621
        mount_self_run = 622
        fly_mount_self_run = 623
        mount_self_sprint = 624
        fly_mount_self_sprint = 625
        mount_self_run_left = 626
        fly_mount_self_run_left = 627
        mount_self_run_right = 628
        fly_mount_self_run_right = 629
        mount_self_shuffle_left = 630
        fly_mount_self_shuffle_left = 631
        mount_self_shuffle_right = 632
        fly_mount_self_shuffle_right = 633
        mount_self_walk_backwards = 634
        fly_mount_self_walk_backwards = 635
        mount_self_special = 636
        fly_mount_self_special = 637
        mount_self_jump = 638
        fly_mount_self_jump = 639
        mount_self_jump_start = 640
        fly_mount_self_jump_start = 641
        mount_self_jump_end = 642
        fly_mount_self_jump_end = 643
        mount_self_jump_land_run = 644
        fly_mount_self_jump_land_run = 645
        mount_self_start = 646
        fly_mount_self_start = 647
        mount_self_fall = 648
        fly_mount_self_fall = 649
        stormstrike = 650
        fly_stormstrike = 651
        ready_joust_no_sheathe = 652
        fly_ready_joust_no_sheathe = 653
        slam = 654
        fly_slam = 655
        death_strike = 656
        fly_death_strike = 657
        swim_attack_unarmed = 658
        fly_swim_attack_unarmed = 659
        spinning_kick = 660
        fly_spinning_kick = 661
        round_house_kick = 662
        fly_round_house_kick = 663
        roll_start = 664
        fly_roll_start = 665
        roll = 666
        fly_roll = 667
        roll_end = 668
        fly_roll_end = 669
        palm_strike = 670
        fly_palm_strike = 671
        monk_offense_attack_unarmed = 672
        fly_monk_offense_attack_unarmed = 673
        monk_offense_attack_unarmed_off = 674
        fly_monk_offense_attack_unarmed_off = 675
        monk_offense_parry_unarmed = 676
        fly_monk_offense_parry_unarmed = 677
        monk_offense_ready_unarmed = 678
        fly_monk_offense_ready_unarmed = 679
        monk_offense_special_unarmed = 680
        fly_monk_offense_special_unarmed = 681
        monk_defense_attack_unarmed = 682
        fly_monk_defense_attack_unarmed = 683
        monk_defense_attack_unarmed_off = 684
        fly_monk_defense_attack_unarmed_off = 685
        monk_defense_parry_unarmed = 686
        fly_monk_defense_parry_unarmed = 687
        monk_defense_ready_unarmed = 688
        fly_monk_defense_ready_unarmed = 689
        monk_defense_special_unarmed = 690
        fly_monk_defense_special_unarmed = 691
        monk_heal_attack_unarmed = 692
        fly_monk_heal_attack_unarmed = 693
        monk_heal_attack_unarmed_off = 694
        fly_monk_heal_attack_unarmed_off = 695
        monk_heal_parry_unarmed = 696
        fly_monk_heal_parry_unarmed = 697
        monk_heal_ready_unarmed = 698
        fly_monk_heal_ready_unarmed = 699
        monk_heal_special_unarmed = 700
        fly_monk_heal_special_unarmed = 701
        flying_kick = 702
        fly_flying_kick = 703
        flying_kick_start = 704
        fly_flying_kick_start = 705
        flying_kick_end = 706
        fly_flying_kick_end = 707
        crane_start = 708
        fly_crane_start = 709
        crane_loop = 710
        fly_crane_loop = 711
        crane_end = 712
        fly_crane_end = 713
        despawned = 714
        fly_despawned = 715
        thousand_fists = 716
        fly_thousand_fists = 717
        monk_heal_ready_spell_directed = 718
        fly_monk_heal_ready_spell_directed = 719
        monk_heal_ready_spell_omni = 720
        fly_monk_heal_ready_spell_omni = 721
        monk_heal_spell_cast_directed = 722
        fly_monk_heal_spell_cast_directed = 723
        monk_heal_spell_cast_omni = 724
        fly_monk_heal_spell_cast_omni = 725
        monk_heal_channel_cast_directed = 726
        fly_monk_heal_channel_cast_directed = 727
        monk_heal_channel_cast_omni = 728
        fly_monk_heal_channel_cast_omni = 729
        torpedo = 730
        fly_torpedo = 731
        meditate = 732
        fly_meditate = 733
        breath_of_fire = 734
        fly_breath_of_fire = 735
        rising_sun_kick = 736
        fly_rising_sun_kick = 737
        ground_kick = 738
        fly_ground_kick = 739
        kick_back = 740
        fly_kick_back = 741
        pet_battle_stand = 742
        fly_pet_battle_stand = 743
        pet_battle_death = 744
        fly_pet_battle_death = 745
        pet_battle_run = 746
        fly_pet_battle_run = 747
        pet_battle_wound = 748
        fly_pet_battle_wound = 749
        pet_battle_attack = 750
        fly_pet_battle_attack = 751
        pet_battle_ready_spell = 752
        fly_pet_battle_ready_spell = 753
        pet_battle_spell_cast = 754
        fly_pet_battle_spell_cast = 755
        pet_battle_custom0 = 756
        fly_pet_battle_custom0 = 757
        pet_battle_custom1 = 758
        fly_pet_battle_custom1 = 759
        pet_battle_custom2 = 760
        fly_pet_battle_custom2 = 761
        pet_battle_custom3 = 762
        fly_pet_battle_custom3 = 763
        pet_battle_victory = 764
        fly_pet_battle_victory = 765
        pet_battle_loss = 766
        fly_pet_battle_loss = 767
        pet_battle_stun = 768
        fly_pet_battle_stun = 769
        pet_battle_dead = 770
        fly_pet_battle_dead = 771
        pet_battle_freeze = 772
        fly_pet_battle_freeze = 773
        monk_offense_attack_weapon = 774
        fly_monk_offense_attack_weapon = 775
        bar_tend_emote_wave = 776
        fly_bar_tend_emote_wave = 777
        bar_server_emote_talk = 778
        fly_bar_server_emote_talk = 779
        bar_server_emote_wave = 780
        fly_bar_server_emote_wave = 781
        bar_server_pour_drinks = 782
        fly_bar_server_pour_drinks = 783
        bar_server_pickup = 784
        fly_bar_server_pickup = 785
        bar_server_put_down = 786
        fly_bar_server_put_down = 787
        bar_sweep_stand = 788
        fly_bar_sweep_stand = 789
        bar_patron_sit = 790
        fly_bar_patron_sit = 791
        bar_patron_sit_emote_talk = 792
        fly_bar_patron_sit_emote_talk = 793
        bar_patron_stand = 794
        fly_bar_patron_stand = 795
        bar_patron_stand_emote_talk = 796
        fly_bar_patron_stand_emote_talk = 797
        bar_patron_stand_emote_point = 798
        fly_bar_patron_stand_emote_point = 799
        carrion_swarm = 800
        fly_carrion_swarm = 801
        wheel_loop = 802
        fly_wheel_loop = 803
        stand_character_create = 804
        fly_stand_character_create = 805
        mount_chopper = 806
        fly_mount_chopper = 807
        face_pose = 808
        fly_face_pose = 809
        combat_ablity_2h_big01 = 810
        fly_combat_ablity_2h_big01 = 811
        combat_ablity_2h_01 = 812
        fly_combat_ablity_2h_01 = 813
        combat_whirlwind = 814
        fly_combat_whirlwind = 815
        combat_charge_loop = 816
        fly_combat_charge_loop = 817
        combat_ablity_1h_01 = 818
        fly_combat_ablity_1h_01 = 819
        combat_charge_end = 820
        fly_combat_charge_end = 821
        combat_ablity_1h_02 = 822
        fly_combat_ablity_1h_02 = 823
        combat_ablity_1h_big01 = 824
        fly_combat_ablity_1h_big01 = 825
        combat_ablity_2h_02 = 826
        fly_combat_ablity_2h_02 = 827
        sha_spell_precast_both = 828
        fly_sha_spell_precast_both = 829
        sha_spell_cast_both_front = 830
        fly_sha_spell_cast_both_front = 831
        sha_spell_cast_left_front = 832
        fly_sha_spell_cast_left_front = 833
        sha_spell_cast_right_front = 834
        fly_sha_spell_cast_right_front = 835
        ready_crossbow = 836
        fly_ready_crossbow = 837
        load_crossbow = 838
        fly_load_crossbow = 839
        attack_crossbow = 840
        fly_attack_crossbow = 841
        hold_crossbow = 842
        fly_hold_crossbow = 843
        combat_ablity_2h_l01 = 844
        fly_combat_ablity_2h_l01 = 845
        combat_ablity_2h_l02 = 846
        fly_combat_ablity_2h_l02 = 847
        combat_ablity_2h_lbig01 = 848
        fly_combat_ablity_2h_lbig01 = 849
        combat_unarmed01 = 850
        fly_combat_unarmed01 = 851
        combat_stomp_left = 852
        fly_combat_stomp_left = 853
        combat_stomp_right = 854
        fly_combat_stomp_right = 855
        combat_leap_loop = 856
        fly_combat_leap_loop = 857
        combat_leap_end = 858
        fly_combat_leap_end = 859
        sha_ready_spell_cast = 860
        fly_sha_ready_spell_cast = 861
        sha_spell_precast_both_channel = 862
        fly_sha_spell_precast_both_channel = 863
        sha_spell_cast_both_up = 864
        fly_sha_spell_cast_both_up = 865
        sha_spell_cast_both_up_channel = 866
        fly_sha_spell_cast_both_up_channel = 867
        sha_spell_cast_both_front_channel = 868
        fly_sha_spell_cast_both_front_channel = 869
        sha_spell_cast_left_front_channel = 870
        fly_sha_spell_cast_left_front_channel = 871
        sha_spell_cast_right_front_channel = 872
        fly_sha_spell_cast_right_front_channel = 873
        pri_ready_spell_cast = 874
        fly_pri_ready_spell_cast = 875
        pri_spell_precast_both = 876
        fly_pri_spell_precast_both = 877
        pri_spell_precast_both_channel = 878
        fly_pri_spell_precast_both_channel = 879
        pri_spell_cast_both_up = 880
        fly_pri_spell_cast_both_up = 881
        pri_spell_cast_both_front = 882
        fly_pri_spell_cast_both_front = 883
        pri_spell_cast_left_front = 884
        fly_pri_spell_cast_left_front = 885
        pri_spell_cast_right_front = 886
        fly_pri_spell_cast_right_front = 887
        pri_spell_cast_both_up_channel = 888
        fly_pri_spell_cast_both_up_channel = 889
        pri_spell_cast_both_front_channel = 890
        fly_pri_spell_cast_both_front_channel = 891
        pri_spell_cast_left_front_channel = 892
        fly_pri_spell_cast_left_front_channel = 893
        pri_spell_cast_right_front_channel = 894
        fly_pri_spell_cast_right_front_channel = 895
        mag_ready_spell_cast = 896
        fly_mag_ready_spell_cast = 897
        mag_spell_precast_both = 898
        fly_mag_spell_precast_both = 899
        mag_spell_precast_both_channel = 900
        fly_mag_spell_precast_both_channel = 901
        mag_spell_cast_both_up = 902
        fly_mag_spell_cast_both_up = 903
        mag_spell_cast_both_front = 904
        fly_mag_spell_cast_both_front = 905
        mag_spell_cast_left_front = 906
        fly_mag_spell_cast_left_front = 907
        mag_spell_cast_right_front = 908
        fly_mag_spell_cast_right_front = 909
        mag_spell_cast_both_up_channel = 910
        fly_mag_spell_cast_both_up_channel = 911
        mag_spell_cast_both_front_channel = 912
        fly_mag_spell_cast_both_front_channel = 913
        mag_spell_cast_left_front_channel = 914
        fly_mag_spell_cast_left_front_channel = 915
        mag_spell_cast_right_front_channel = 916
        fly_mag_spell_cast_right_front_channel = 917
        loc_ready_spell_cast = 918
        fly_loc_ready_spell_cast = 919
        loc_spell_precast_both = 920
        fly_loc_spell_precast_both = 921
        loc_spell_precast_both_channel = 922
        fly_loc_spell_precast_both_channel = 923
        loc_spell_cast_both_up = 924
        fly_loc_spell_cast_both_up = 925
        loc_spell_cast_both_front = 926
        fly_loc_spell_cast_both_front = 927
        loc_spell_cast_left_front = 928
        fly_loc_spell_cast_left_front = 929
        loc_spell_cast_right_front = 930
        fly_loc_spell_cast_right_front = 931
        loc_spell_cast_both_up_channel = 932
        fly_loc_spell_cast_both_up_channel = 933
        loc_spell_cast_both_front_channel = 934
        fly_loc_spell_cast_both_front_channel = 935
        loc_spell_cast_left_front_channel = 936
        fly_loc_spell_cast_left_front_channel = 937
        loc_spell_cast_right_front_channel = 938
        fly_loc_spell_cast_right_front_channel = 939
        dru_ready_spell_cast = 940
        fly_dru_ready_spell_cast = 941
        dru_spell_precast_both = 942
        fly_dru_spell_precast_both = 943
        dru_spell_precast_both_channel = 944
        fly_dru_spell_precast_both_channel = 945
        dru_spell_cast_both_up = 946
        fly_dru_spell_cast_both_up = 947
        dru_spell_cast_both_front = 948
        fly_dru_spell_cast_both_front = 949
        dru_spell_cast_left_front = 950
        fly_dru_spell_cast_left_front = 951
        dru_spell_cast_right_front = 952
        fly_dru_spell_cast_right_front = 953
        dru_spell_cast_both_up_channel = 954
        fly_dru_spell_cast_both_up_channel = 955
        dru_spell_cast_both_front_channel = 956
        fly_dru_spell_cast_both_front_channel = 957
        dru_spell_cast_left_front_channel = 958
        fly_dru_spell_cast_left_front_channel = 959
        dru_spell_cast_right_front_channel = 960
        fly_dru_spell_cast_right_front_channel = 961
        art_main_loop = 962
        fly_art_main_loop = 963
        art_dual_loop = 964
        fly_art_dual_loop = 965
        art_fists_loop = 966
        fly_art_fists_loop = 967
        art_bow_loop = 968
        fly_art_bow_loop = 969
        combat_ablity_1h_01off = 970
        fly_combat_ablity_1h_01off = 971
        combat_ablity_1h_02off = 972
        fly_combat_ablity_1h_02off = 973
        combat_furious_strike01 = 974
        fly_combat_furious_strike01 = 975
        combat_furious_strike02 = 976
        fly_combat_furious_strike02 = 977
        combat_furious_strikes = 978
        fly_combat_furious_strikes = 979
        combat_ready_spell_cast = 980
        fly_combat_ready_spell_cast = 981
        combat_shield_throw = 982
        fly_combat_shield_throw = 983
        pal_spell_cast_1h_up = 984
        fly_pal_spell_cast_1h_up = 985
        combat_ready_post_spell_cast = 986
        fly_combat_ready_post_spell_cast = 987
        pri_ready_post_spell_cast = 988
        fly_pri_ready_post_spell_cast = 989
        dh_combat_run = 990
        fly_dh_combat_run = 991
        combat_shield_bash = 992
        fly_combat_shield_bash = 993
        combat_throw = 994
        fly_combat_throw = 995
        combat_ablity_1h_pierce = 996
        fly_combat_ablity_1h_pierce = 997
        combat_ablity_1h_off_pierce = 998
        fly_combat_ablity_1h_off_pierce = 999
        combat_mutilate = 1000
        fly_combat_mutilate = 1001
        combat_blade_storm = 1002
        fly_combat_blade_storm = 1003
        combat_finishing_move = 1004
        fly_combat_finishing_move = 1005
        combat_leap_start = 1006
        fly_combat_leap_start = 1007
        glv_throw_main = 1008
        fly_glv_throw_main = 1009
        glv_thrown_off = 1010
        fly_glv_thrown_off = 1011
        dh_combat_sprint = 1012
        fly_dh_combat_sprint = 1013
        combat_ability_glv01 = 1014
        fly_combat_ability_glv01 = 1015
        combat_ability_glv02 = 1016
        fly_combat_ability_glv02 = 1017
        combat_ability_glv_off01 = 1018
        fly_combat_ability_glv_off01 = 1019
        combat_ability_glv_off02 = 1020
        fly_combat_ability_glv_off02 = 1021
        combat_ability_glv_big01 = 1022
        fly_combat_ability_glv_big01 = 1023
        combat_ability_glv_big02 = 1024
        fly_combat_ability_glv_big02 = 1025
        ready_glv = 1026
        fly_ready_glv = 1027
        combat_ability_glv_big03 = 1028
        fly_combat_ability_glv_big03 = 1029
        double_jump_start = 1030
        fly_double_jump_start = 1031
        double_jump = 1032
        fly_double_jump = 1033
        combat_eviscerate = 1034
        fly_combat_eviscerate = 1035
        double_jump_land_run = 1036
        fly_double_jump_land_run = 1037
        back_flip_start = 1038
        fly_back_flip_start = 1039
        back_flip_loop = 1040
        fly_back_flip_loop = 1041
        fel_rush_loop = 1042
        fly_fel_rush_loop = 1043
        fel_rush_end = 1044
        fly_fel_rush_end = 1045
        dh_to_altered_start = 1046
        fly_dh_to_altered_start = 1047
        dh_to_altered_end = 1048
        fly_dh_to_altered_end = 1049
        dh_glide = 1050
        fly_dh_glide = 1051
        fan_of_knives = 1052
        fly_fan_of_knives = 1053
        single_jump_start = 1054
        fly_single_jump_start = 1055
        dh_blade_dance1 = 1056
        fly_dh_blade_dance1 = 1057
        dh_blade_dance2 = 1058
        fly_dh_blade_dance2 = 1059
        dh_blade_dance3 = 1060
        fly_dh_blade_dance3 = 1061
        dh_meteor_strike = 1062
        fly_dh_meteor_strike = 1063
        combat_execute = 1064
        fly_combat_execute = 1065
        art_loop = 1066
        fly_art_loop = 1067
        parry_glv = 1068
        fly_parry_glv = 1069
        combat_unarmed02 = 1070
        fly_combat_unarmed02 = 1071
        combat_pistol_shot = 1072
        fly_combat_pistol_shot = 1073
        combat_pistol_shot_off = 1074
        fly_combat_pistol_shot_off = 1075
        monk_2h_l_idle = 1076
        fly_monk_2h_l_idle = 1077
        art_shield_loop = 1078
        fly_art_shield_loop = 1079
        combat_ablity_2h_03 = 1080
        fly_combat_ablity_2h_03 = 1081
        combat_stomp = 1082
        fly_combat_stomp = 1083
        combat_roar = 1084
        fly_combat_roar = 1085
        pal_ready_spell_cast = 1086
        fly_pal_ready_spell_cast = 1087
        pal_spell_precast_right = 1088
        fly_pal_spell_precast_right = 1089
        pal_spell_precast_right_channel = 1090
        fly_pal_spell_precast_right_channel = 1091
        pal_spell_cast_right_front = 1092
        fly_pal_spell_cast_right_front = 1093
        sha_spell_cast_both_out = 1094
        fly_sha_spell_cast_both_out = 1095
        attack_weapon = 1096
        fly_attack_weapon = 1097
        ready_weapon = 1098
        fly_ready_weapon = 1099
        attack_weapon_off = 1100
        fly_attack_weapon_off = 1101
        special_dual = 1102
        fly_special_dual = 1103
        dk_cast_1h_front = 1104
        fly_dk_cast_1h_front = 1105
        cast_strong_right = 1106
        fly_cast_strong_right = 1107
        cast_strong_left = 1108
        fly_cast_strong_left = 1109
        cast_curse_right = 1110
        fly_cast_curse_right = 1111
        cast_curse_left = 1112
        fly_cast_curse_left = 1113
        cast_sweep_right = 1114
        fly_cast_sweep_right = 1115
        cast_sweep_left = 1116
        fly_cast_sweep_left = 1117
        cast_strong_up_left = 1118
        fly_cast_strong_up_left = 1119
        cast_twist_up_both = 1120
        fly_cast_twist_up_both = 1121
        cast_out_strong = 1122
        fly_cast_out_strong = 1123
        drum_loop = 1124
        fly_drum_loop = 1125
        parry_weapon = 1126
        fly_parry_weapon = 1127
        ready_fl = 1128
        fly_ready_fl = 1129
        attack_fl = 1130
        fly_attack_fl = 1131
        attack_floff = 1132
        fly_attack_floff = 1133
        parry_fl = 1134
        fly_parry_fl = 1135
        special_fl = 1136
        fly_special_fl = 1137
        pri_hover_forward = 1138
        fly_pri_hover_forward = 1139
        pri_hover_backward = 1140
        fly_pri_hover_backward = 1141
        pri_hover_right = 1142
        fly_pri_hover_right = 1143
        pri_hover_left = 1144
        fly_pri_hover_left = 1145
        run_backwards = 1146
        fly_run_backwards = 1147
        cast_strong_up_right = 1148
        fly_cast_strong_up_right = 1149
        wa_walk = 1150
        fly_wa_walk = 1151
        wa_run = 1152
        fly_wa_run = 1153
        wa_drunk_stand = 1154
        fly_wa_drunk_stand = 1155
        wa_drunk_shuffle_left = 1156
        fly_wa_drunk_shuffle_left = 1157
        wa_drunk_shuffle_right = 1158
        fly_wa_drunk_shuffle_right = 1159
        wa_drunk_walk = 1160
        fly_wa_drunk_walk = 1161
        wa_drunk_walk_backwards = 1162
        fly_wa_drunk_walk_backwards = 1163
        wa_drunk_wound = 1164
        fly_wa_drunk_wound = 1165
        wa_drunk_talk = 1166
        fly_wa_drunk_talk = 1167
        wa_trance01 = 1168
        fly_wa_trance01 = 1169
        wa_trance02 = 1170
        fly_wa_trance02 = 1171
        wa_chant01 = 1172
        fly_wa_chant01 = 1173
        wa_chant02 = 1174
        fly_wa_chant02 = 1175
        wa_chant03 = 1176
        fly_wa_chant03 = 1177
        wa_hang01 = 1178
        fly_wa_hang01 = 1179
        wa_hang02 = 1180
        fly_wa_hang02 = 1181
        wa_summon01 = 1182
        fly_wa_summon01 = 1183
        wa_summon02 = 1184
        fly_wa_summon02 = 1185
        wa_beggar_talk = 1186
        fly_wa_beggar_talk = 1187
        wa_beggar_stand = 1188
        fly_wa_beggar_stand = 1189
        wa_beggar_point = 1190
        fly_wa_beggar_point = 1191
        wa_beggar_beg = 1192
        fly_wa_beggar_beg = 1193
        wa_sit01 = 1194
        fly_wa_sit01 = 1195
        wa_sit02 = 1196
        fly_wa_sit02 = 1197
        wa_sit03 = 1198
        fly_wa_sit03 = 1199
        wa_crier_stand01 = 1200
        fly_wa_crier_stand01 = 1201
        wa_crier_stand02 = 1202
        fly_wa_crier_stand02 = 1203
        wa_crier_stand03 = 1204
        fly_wa_crier_stand03 = 1205
        wa_crier_talk = 1206
        fly_wa_crier_talk = 1207
        wa_crate_hold = 1208
        fly_wa_crate_hold = 1209
        wa_barrel_hold = 1210
        fly_wa_barrel_hold = 1211
        wa_sack_hold = 1212
        fly_wa_sack_hold = 1213
        wa_wheel_barrow_stand = 1214
        fly_wa_wheel_barrow_stand = 1215
        wa_wheel_barrow_walk = 1216
        fly_wa_wheel_barrow_walk = 1217
        wa_wheel_barrow_run = 1218
        fly_wa_wheel_barrow_run = 1219
        wa_hammer_loop = 1220
        fly_wa_hammer_loop = 1221
        wa_crank_loop = 1222
        fly_wa_crank_loop = 1223
        wa_pour_start = 1224
        fly_wa_pour_start = 1225
        wa_pour_loop = 1226
        fly_wa_pour_loop = 1227
        wa_pour_end = 1228
        fly_wa_pour_end = 1229
        wa_emote_pour = 1230
        fly_wa_emote_pour = 1231
        wa_rowing_stand_right = 1232
        fly_wa_rowing_stand_right = 1233
        wa_rowing_stand_left = 1234
        fly_wa_rowing_stand_left = 1235
        wa_rowing_right = 1236
        fly_wa_rowing_right = 1237
        wa_rowing_left = 1238
        fly_wa_rowing_left = 1239
        wa_guard_stand01 = 1240
        fly_wa_guard_stand01 = 1241
        wa_guard_stand02 = 1242
        fly_wa_guard_stand02 = 1243
        wa_guard_stand03 = 1244
        fly_wa_guard_stand03 = 1245
        wa_guard_stand04 = 1246
        fly_wa_guard_stand04 = 1247
        wa_freezing01 = 1248
        fly_wa_freezing01 = 1249
        wa_freezing02 = 1250
        fly_wa_freezing02 = 1251
        wa_vendor_stand01 = 1252
        fly_wa_vendor_stand01 = 1253
        wa_vendor_stand02 = 1254
        fly_wa_vendor_stand02 = 1255
        wa_vendor_stand03 = 1256
        fly_wa_vendor_stand03 = 1257
        wa_vendor_talk = 1258
        fly_wa_vendor_talk = 1259
        wa_lean01 = 1260
        fly_wa_lean01 = 1261
        wa_lean02 = 1262
        fly_wa_lean02 = 1263
        wa_lean03 = 1264
        fly_wa_lean03 = 1265
        wa_lean_talk = 1266
        fly_wa_lean_talk = 1267
        wa_boat_wheel = 1268
        fly_wa_boat_wheel = 1269
        wa_smith_loop = 1270
        fly_wa_smith_loop = 1271
        wa_scrubbing = 1272
        fly_wa_scrubbing = 1273
        wa_weapon_sharpen = 1274
        fly_wa_weapon_sharpen = 1275
        wa_stirring = 1276
        fly_wa_stirring = 1277
        wa_perch01 = 1278
        fly_wa_perch01 = 1279
        wa_perch02 = 1280
        fly_wa_perch02 = 1281
        hold_weapon = 1282
        fly_hold_weapon = 1283
        wa_barrel_walk = 1284
        fly_wa_barrel_walk = 1285
        wa_pour_hold = 1286
        fly_wa_pour_hold = 1287
        cast_strong = 1288
        fly_cast_strong = 1289
        cast_curse = 1290
        fly_cast_curse = 1291
        cast_sweep = 1292
        fly_cast_sweep = 1293
        cast_strong_up = 1294
        fly_cast_strong_up = 1295
        wa_boat_wheel_stand = 1296
        fly_wa_boat_wheel_stand = 1297
        wa_smith_stand = 1298
        fly_wa_smith_stand = 1299
        wa_crank_stand = 1300
        fly_wa_crank_stand = 1301
        wa_pour_walk = 1302
        fly_wa_pour_walk = 1303
        falconeer_start = 1304
        fly_falconeer_start = 1305
        falconeer_loop = 1306
        fly_falconeer_loop = 1307
        falconeer_end = 1308
        fly_falconeer_end = 1309
        wa_drunk_drink = 1310
        fly_wa_drunk_drink = 1311
        wa_stand_eat = 1312
        fly_wa_stand_eat = 1313
        wa_stand_drink = 1314
        fly_wa_stand_drink = 1315
        wa_bound01 = 1316
        fly_wa_bound01 = 1317
        wa_bound02 = 1318
        fly_wa_bound02 = 1319
        combat_ablity_1h_03off = 1320
        fly_combat_ablity_1h_03off = 1321
        combat_ability_dual_wield01 = 1322
        fly_combat_ability_dual_wield01 = 1323
        wa_cradle01 = 1324
        fly_wa_cradle01 = 1325
        loc_summon = 1326
        fly_loc_summon = 1327
        load_weapon = 1328
        fly_load_weapon = 1329
        art_off_loop = 1330
        fly_art_off_loop = 1331
        wa_dead01 = 1332
        fly_wa_dead01 = 1333
        wa_dead02 = 1334
        fly_wa_dead02 = 1335
        wa_dead03 = 1336
        fly_wa_dead03 = 1337
        wa_dead04 = 1338
        fly_wa_dead04 = 1339
        wa_dead05 = 1340
        fly_wa_dead05 = 1341
        wa_dead06 = 1342
        fly_wa_dead06 = 1343
        wa_dead07 = 1344
        fly_wa_dead07 = 1345
        giant_run = 1346
        fly_giant_run = 1347
        bar_tend_emote_cheer = 1348
        fly_bar_tend_emote_cheer = 1349
        bar_tend_emote_talk_question = 1350
        fly_bar_tend_emote_talk_question = 1351
        bar_tend_emote_talk_exclamation = 1352
        fly_bar_tend_emote_talk_exclamation = 1353
        bar_tend_walk = 1354
        fly_bar_tend_walk = 1355
        bartend_shuffle_left = 1356
        fly_bartend_shuffle_left = 1357
        bar_tend_shuffle_right = 1358
        fly_bar_tend_shuffle_right = 1359
        bar_tend_custom_spell01 = 1360
        fly_bar_tend_custom_spell01 = 1361
        bar_tend_custom_spell02 = 1362
        fly_bar_tend_custom_spell02 = 1363
        bar_tend_custom_spell03 = 1364
        fly_bar_tend_custom_spell03 = 1365
        bar_server_emote_cheer = 1366
        fly_bar_server_emote_cheer = 1367
        bar_server_emote_talk_question = 1368
        fly_bar_server_emote_talk_question = 1369
        bar_server_emote_talk_exclamation = 1370
        fly_bar_server_emote_talk_exclamation = 1371
        bar_server_custom_spell01 = 1372
        fly_bar_server_custom_spell01 = 1373
        bar_server_custom_spell02 = 1374
        fly_bar_server_custom_spell02 = 1375
        bar_server_custom_spell03 = 1376
        fly_bar_server_custom_spell03 = 1377
        bar_patron_emote_drink = 1378
        fly_bar_patron_emote_drink = 1379
        bar_patron_emote_cheer = 1380
        fly_bar_patron_emote_cheer = 1381
        bar_patron_custom_spell01 = 1382
        fly_bar_patron_custom_spell01 = 1383
        bar_patron_custom_spell02 = 1384
        fly_bar_patron_custom_spell02 = 1385
        bar_patron_custom_spell03 = 1386
        fly_bar_patron_custom_spell03 = 1387
        hold_dart = 1388
        fly_hold_dart = 1389
        ready_dart = 1390
        fly_ready_dart = 1391
        attack_dart = 1392
        fly_attack_dart = 1393
        load_dart = 1394
        fly_load_dart = 1395
        wa_dart_target_stand = 1396
        fly_wa_dart_target_stand = 1397
        wa_dart_target_emote_talk = 1398
        fly_wa_dart_target_emote_talk = 1399
        bar_patron_sit_emote_cheer = 1400
        fly_bar_patron_sit_emote_cheer = 1401
        bar_patron_sit_custom_spell01 = 1402
        fly_bar_patron_sit_custom_spell01 = 1403
        bar_patron_sit_custom_spell02 = 1404
        fly_bar_patron_sit_custom_spell02 = 1405
        bar_patron_sit_custom_spell03 = 1406
        fly_bar_patron_sit_custom_spell03 = 1407
        bar_piano_stand = 1408
        fly_bar_piano_stand = 1409
        bar_piano_emote_talk = 1410
        fly_bar_piano_emote_talk = 1411
        wa_hearth_sit = 1412
        fly_wa_hearth_sit = 1413
        wa_hearth_sit_emote_cry = 1414
        fly_wa_hearth_sit_emote_cry = 1415
        wa_hearth_sit_emote_cheer = 1416
        fly_wa_hearth_sit_emote_cheer = 1417
        wa_hearth_sit_custom_spell01 = 1418
        fly_wa_hearth_sit_custom_spell01 = 1419
        wa_hearth_sit_custom_spell02 = 1420
        fly_wa_hearth_sit_custom_spell02 = 1421
        wa_hearth_sit_custom_spell03 = 1422
        fly_wa_hearth_sit_custom_spell03 = 1423
        wa_hearth_stand = 1424
        fly_wa_hearth_stand = 1425
        wa_hearth_stand_emote_cheer = 1426
        fly_wa_hearth_stand_emote_cheer = 1427
        wa_hearth_stand_emote_talk = 1428
        fly_wa_hearth_stand_emote_talk = 1429
        wa_hearth_stand_custom_spell01 = 1430
        fly_wa_hearth_stand_custom_spell01 = 1431
        wa_hearth_stand_custom_spell02 = 1432
        fly_wa_hearth_stand_custom_spell02 = 1433
        wa_hearth_stand_custom_spell03 = 1434
        fly_wa_hearth_stand_custom_spell03 = 1435
        wa_scribe_start = 1436
        fly_wa_scribe_start = 1437
        wa_scribe_loop = 1438
        fly_wa_scribe_loop = 1439
        wa_scribe_end = 1440
        fly_wa_scribe_end = 1441
        wa_emote_scribe = 1442
        fly_wa_emote_scribe = 1443
        haymaker = 1444
        fly_haymaker = 1445
        haymaker_precast = 1446
        fly_haymaker_precast = 1447
        channel_cast_omni_up = 1448
        fly_channel_cast_omni_up = 1449
        dh_jump_land_run = 1450
        fly_dh_jump_land_run = 1451
        cinematic01 = 1452
        fly_cinematic01 = 1453
        cinematic02 = 1454
        fly_cinematic02 = 1455
        cinematic03 = 1456
        fly_cinematic03 = 1457
        cinematic04 = 1458
        fly_cinematic04 = 1459
        cinematic05 = 1460
        fly_cinematic05 = 1461
        cinematic06 = 1462
        fly_cinematic06 = 1463
        cinematic07 = 1464
        fly_cinematic07 = 1465
        cinematic08 = 1466
        fly_cinematic08 = 1467
        cinematic09 = 1468
        fly_cinematic09 = 1469
        cinematic10 = 1470
        fly_cinematic10 = 1471
        take_off_start = 1472
        fly_take_off_start = 1473
        take_off_finish = 1474
        fly_take_off_finish = 1475
        land_start = 1476
        fly_land_start = 1477
        land_finish = 1478
        fly_land_finish = 1479
        wa_walk_talk = 1480
        fly_wa_walk_talk = 1481
        wa_perch03 = 1482
        fly_wa_perch03 = 1483
        carriage_mount_moving = 1484
        fly_carriage_mount_moving = 1485
        take_off_finish_fly = 1486
        fly_take_off_finish_fly = 1487
        combat_ablity_2h_big02 = 1488
        fly_combat_ablity_2h_big02 = 1489
        mount_wide = 1490
        fly_mount_wide = 1491
        emote_talk_subdued = 1492
        fly_emote_talk_subdued = 1493
        wa_sit04 = 1494
        fly_wa_sit04 = 1495
        mount_summon = 1496
        fly_mount_summon = 1497
        emote_selfie = 1498
        fly_emote_selfie = 1499
        custom_spell11 = 1500
        fly_custom_spell11 = 1501
        custom_spell12 = 1502
        fly_custom_spell12 = 1503
        custom_spell13 = 1504
        fly_custom_spell13 = 1505
        custom_spell14 = 1506
        fly_custom_spell14 = 1507
        custom_spell15 = 1508
        fly_custom_spell15 = 1509
        custom_spell16 = 1510
        fly_custom_spell16 = 1511
        custom_spell17 = 1512
        fly_custom_spell17 = 1513
        custom_spell18 = 1514
        fly_custom_spell18 = 1515
        custom_spell19 = 1516
        fly_custom_spell19 = 1517
        custom_spell20 = 1518
        fly_custom_spell20 = 1519
        future_patch01 = 1520
        fly_future_patch01 = 1521
        future_patch02 = 1522
        fly_future_patch02 = 1523
        future_patch03 = 1524
        fly_future_patch03 = 1525
        future_patch04 = 1526
        fly_future_patch04 = 1527
        future_patch05 = 1528
        fly_future_patch05 = 1529
        future_patch06 = 1530
        fly_future_patch06 = 1531
        future_patch07 = 1532
        fly_future_patch07 = 1533
        future_patch08 = 1534
        fly_future_patch08 = 1535
        future_patch09 = 1536
        fly_future_patch09 = 1537
        future_patch10 = 1538
        fly_future_patch10 = 1539
        future_patch11 = 1540
        fly_future_patch11 = 1541

    class WowVersions(Enum):
        tbc = 260
        wotlk = 264
        cata = 265
        mop = 272
        wod = 273
        legion = 274

    class EmitterTypes(Enum):
        plane = 1
        sphere = 2
        spline = 3
        bone = 4
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.mvermagic = self._io.read_bytes(4)
        if not self.mvermagic == b"\x52\x45\x56\x4D":
            raise kaitaistruct.ValidationNotEqualError(b"\x52\x45\x56\x4D", self.mvermagic, self._io, u"/seq/0")
        self.chunksize = self._io.read_u4le()
        self.ver = self._io.read_u4le()
        self.chunks = []
        i = 0
        while not self._io.is_eof():
            self.chunks.append(Wdt.WdtChunk(self._io, self, self._root))
            i += 1


    class C3segment(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.start = Wdt.C3vector(self._io, self, self._root)
            self.end = Wdt.C3vector(self._io, self, self._root)


    class M2light(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = self._io.read_u2le()
            self.bone = self._io.read_s2le()
            self.position = Wdt.C3vector(self._io, self, self._root)
            self.ambient_color = Wdt.M2track(Wdt.M2trackTypes.c3vector, self._io, self, self._root)
            self.ambient_intensity = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.diffuse_color = Wdt.M2track(Wdt.M2trackTypes.c3vector, self._io, self, self._root)
            self.diffuse_intensity = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.attenuation_start = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.attenuation_end = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.visibility = Wdt.M2track(Wdt.M2trackTypes.uint8, self._io, self, self._root)


    class M2extendedParticle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.z_source = self._io.read_f4le()
            self.unknown1 = self._io.read_u4le()
            self.unknown2 = self._io.read_u4le()
            self.unknown3 = Wdt.M2parttrack(Wdt.M2arrayTypes.fixed16, self._io, self, self._root)


    class MphdFlags(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.wdt_uses_global_map_obj = self._io.read_bits_int_le(1) != 0
            self.adt_has_mccv = self._io.read_bits_int_le(1) != 0
            self.adt_has_big_alpha = self._io.read_bits_int_le(1) != 0
            self.adt_has_doodadrefs_sorted_by_size_cat = self._io.read_bits_int_le(1) != 0
            self.lighting_vertices = self._io.read_bits_int_le(1) != 0
            self.adt_has_upside_down_ground = self._io.read_bits_int_le(1) != 0
            self.unknown1 = self._io.read_bits_int_le(1) != 0
            self.adt_has_height_texturing = self._io.read_bits_int_le(1) != 0
            self.unknown2 = self._io.read_bits_int_le(1) != 0
            self.wdt_has_maid = self._io.read_bits_int_le(1) != 0
            self.unknown3 = self._io.read_bits_int_le(1) != 0
            self.unknown4 = self._io.read_bits_int_le(1) != 0
            self.unknown5 = self._io.read_bits_int_le(1) != 0
            self.unknown6 = self._io.read_bits_int_le(1) != 0
            self.unknown7 = self._io.read_bits_int_le(1) != 0
            self.unknown8 = self._io.read_bits_int_le(1) != 0


    class ChunkMaid(KaitaiStruct):
        """Map fileid table. Needs to contain 64x64 (4096) entries.
        
        .. seealso::
           Source - https://wowdev.wiki/WDT#MAID_chunk
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.map_fileids = []
            i = 0
            while not self._io.is_eof():
                self.map_fileids.append(Wdt.MapFileDataIdSet(self._io, self, self._root))
                i += 1



    class M2sequence(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = KaitaiStream.resolve_enum(Wdt.AnimNames, self._io.read_u2le())
            self.variation_index = self._io.read_u2le()
            self.duration = self._io.read_u4le()
            self.movespeed = self._io.read_f4le()
            self._raw_flags = self._io.read_bytes(4)
            _io__raw_flags = KaitaiStream(BytesIO(self._raw_flags))
            self.flags = Wdt.M2sequenceFlags(_io__raw_flags, self, self._root)
            self.frequency = self._io.read_s2le()
            self.padding = self._io.read_u2le()
            self.replay = Wdt.M2range(self._io, self, self._root)
            self.blend_time_in = self._io.read_u2le()
            self.blend_time_out = self._io.read_u2le()
            self.bounds = Wdt.M2bounds(self._io, self, self._root)
            self.variation_next = self._io.read_s2le()
            self.alias_next = self._io.read_u2le()


    class M2texturetransform(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.translation = Wdt.M2track(Wdt.M2trackTypes.c3vector, self._io, self, self._root)
            self.rotation = Wdt.M2track(Wdt.M2trackTypes.c4quaternion, self._io, self, self._root)
            self.scaling = Wdt.M2track(Wdt.M2trackTypes.c3vector, self._io, self, self._root)


    class M2batch(KaitaiStruct):
        """Texture Units.
        
        .. seealso::
           Source - https://wowdev.wiki/M2/.skin#Texture_units
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.flags = self._io.read_u1()
            self.priority_plane = self._io.read_s1()
            self.shader_id = self._io.read_u2le()
            self.skin_section_index = self._io.read_u2le()
            self.geoset_index = self._io.read_u2le()
            self.color_index = self._io.read_s2le()
            self.material_index = self._io.read_u2le()
            self.material_layer = self._io.read_u2le()
            self.texture_count = self._io.read_u2le()
            self.texture_combo_index = self._io.read_u2le()
            self.texture_coord_combo_index = self._io.read_u2le()
            self.texture_weight_combo_index = self._io.read_u2le()
            self.texture_transform_combo_index = self._io.read_u2le()


    class ChunkMslt(KaitaiStruct):
        """Map Spot Lights.
        
        .. seealso::
           Source - https://wowdev.wiki/WDT#MSLT_.28Legion.2B.29
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.spot_lights = []
            i = 0
            while not self._io.is_eof():
                self.spot_lights.append(Wdt.MapSpotLight(self._io, self, self._root))
                i += 1



    class M2particleOld(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.particle_id = self._io.read_s4le()
            self.flags = Wdt.M2particlesFlags(self._io, self, self._root)
            self.position = Wdt.C3vector(self._io, self, self._root)
            self.bone = self._io.read_u2le()
            self.texture_0 = self._io.read_bits_int_le(5)
            self.texture_1 = self._io.read_bits_int_le(5)
            self.texture_2 = self._io.read_bits_int_le(5)
            self._io.align_to_byte()
            if True:
                self.num_geometry_model_filename = self._io.read_u4le()

            if True:
                self.ofs_geometry_model_filename = self._io.read_u4le()

            if True:
                self.num_recursion_model_filename = self._io.read_u4le()

            if True:
                self.ofs_recursion_model_filename = self._io.read_u4le()

            self.blending_type = KaitaiStream.resolve_enum(Wdt.Blendmodes, self._io.read_u1())
            self.emitter_type = KaitaiStream.resolve_enum(Wdt.EmitterTypes, self._io.read_u1())
            self.particle_color_index = self._io.read_u2le()
            self.multi_texture_param_x = self._io.read_u1()
            self.multi_texture_param_y = self._io.read_u1()
            self.texture_tile_rotation = self._io.read_s2le()
            self.texture_dimensions_rows = self._io.read_u2le()
            self.texture_dimensions_columns = self._io.read_u2le()
            self.emission_speed = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.speed_variation = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.vertical_range = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.horizontal_range = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.gravity = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.lifespan = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.lifespan_vary = self._io.read_f4le()
            self.emission_rate = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.emission_rate_vary = self._io.read_f4le()
            self.emission_area_length = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.emission_area_width = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.z_source = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.p = Wdt.ModelParticleParams(self._io, self, self._root)
            self.enabled_in = Wdt.M2track(Wdt.M2trackTypes.uint16, self._io, self, self._root)

        @property
        def geometry_model_filename(self):
            if hasattr(self, '_m_geometry_model_filename'):
                return self._m_geometry_model_filename if hasattr(self, '_m_geometry_model_filename') else None

            if True:
                _pos = self._io.pos()
                self._io.seek(self.ofs_geometry_model_filename)
                self._m_geometry_model_filename = (self._io.read_bytes(self.num_geometry_model_filename)).decode(u"UTF-8")
                self._io.seek(_pos)

            return self._m_geometry_model_filename if hasattr(self, '_m_geometry_model_filename') else None

        @property
        def recursion_model_filename(self):
            if hasattr(self, '_m_recursion_model_filename'):
                return self._m_recursion_model_filename if hasattr(self, '_m_recursion_model_filename') else None

            if True:
                _pos = self._io.pos()
                self._io.seek(self.ofs_recursion_model_filename)
                self._m_recursion_model_filename = (self._io.read_bytes(self.num_recursion_model_filename)).decode(u"UTF-8")
                self._io.seek(_pos)

            return self._m_recursion_model_filename if hasattr(self, '_m_recursion_model_filename') else None


    class ParticleVolumeBd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unknown1 = self._io.read_u4le()
            self.unknown2 = Wdt.Caabox(self._io, self, self._root)
            self.unknown3 = [None] * (8)
            for i in range(8):
                self.unknown3[i] = self._io.read_u4le()

            self.unknown4 = self._io.read_u4le()


    class Cfacet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.plane = Wdt.C4plane(self._io, self, self._root)
            self.vertices = [None] * (3)
            for i in range(3):
                self.vertices[i] = Wdt.C3vector(self._io, self, self._root)



    class M2array(KaitaiStruct):
        def __init__(self, m2array_type, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.m2array_type = m2array_type
            self._read()

        def _read(self):
            self.num = self._io.read_u4le()
            self.offset = self._io.read_u4le()

        @property
        def values(self):
            if hasattr(self, '_m_values'):
                return self._m_values if hasattr(self, '_m_values') else None

            _pos = self._io.pos()
            self._io.seek(self.offset)
            self._m_values = [None] * (self.num)
            for i in range(self.num):
                _on = self.m2array_type
                if _on == Wdt.M2arrayTypes.fixed16:
                    self._m_values[i] = Wdt.Fixed16(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2ribbon:
                    self._m_values[i] = Wdt.M2ribbon(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.int16:
                    self._m_values[i] = self._io.read_s2le()
                elif _on == Wdt.M2arrayTypes.m2array_c4quaternion:
                    self._m_values[i] = Wdt.M2array(Wdt.M2arrayTypes.c4quaternion, self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2vertex:
                    self._m_values[i] = Wdt.M2vertex(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2light:
                    self._m_values[i] = Wdt.M2light(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2sequence:
                    self._m_values[i] = Wdt.M2sequence(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2array_fixed16:
                    self._m_values[i] = Wdt.M2array(Wdt.M2arrayTypes.fixed16, self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2array_c3vector:
                    self._m_values[i] = Wdt.M2array(Wdt.M2arrayTypes.c3vector, self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2loop:
                    self._m_values[i] = Wdt.M2loop(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2sequencefallback:
                    self._m_values[i] = Wdt.M2sequencefallback(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.uint8:
                    self._m_values[i] = self._io.read_u1()
                elif _on == Wdt.M2arrayTypes.uint32:
                    self._m_values[i] = self._io.read_u4le()
                elif _on == Wdt.M2arrayTypes.todo:
                    self._m_values[i] = Wdt.M2arrayTodo(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2event:
                    self._m_values[i] = Wdt.M2event(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.c4quaternion:
                    self._m_values[i] = Wdt.C4quaternion(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2texturetransform:
                    self._m_values[i] = Wdt.M2texturetransform(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.c3vector:
                    self._m_values[i] = Wdt.C3vector(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2particle:
                    self._m_values[i] = Wdt.M2particle(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2color:
                    self._m_values[i] = Wdt.M2color(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2shadowbatch:
                    self._m_values[i] = Wdt.M2shadowbatch(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.float:
                    self._m_values[i] = self._io.read_f4le()
                elif _on == Wdt.M2arrayTypes.c4vector:
                    self._m_values[i] = Wdt.C4vector(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2texture:
                    self._m_values[i] = Wdt.M2texture(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.c2vector:
                    self._m_values[i] = Wdt.C2vector(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2array_c4vector:
                    self._m_values[i] = Wdt.M2array(Wdt.M2arrayTypes.c4vector, self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2extended_particle:
                    self._m_values[i] = Wdt.M2extendedParticle(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.uint16:
                    self._m_values[i] = self._io.read_u2le()
                elif _on == Wdt.M2arrayTypes.m2array_m2compquat:
                    self._m_values[i] = Wdt.M2array(Wdt.M2arrayTypes.m2compquat, self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2attachment:
                    self._m_values[i] = Wdt.M2attachment(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.int8:
                    self._m_values[i] = self._io.read_s1()
                elif _on == Wdt.M2arrayTypes.m2array_float:
                    self._m_values[i] = Wdt.M2array(Wdt.M2arrayTypes.float, self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2array_c2vector:
                    self._m_values[i] = Wdt.M2array(Wdt.M2arrayTypes.c2vector, self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.frgb:
                    self._m_values[i] = Wdt.Frgb(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2material:
                    self._m_values[i] = Wdt.M2material(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2array_uint32:
                    self._m_values[i] = Wdt.M2array(Wdt.M2arrayTypes.uint32, self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2compquat:
                    self._m_values[i] = Wdt.M2compquat(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.ubyte4:
                    self._m_values[i] = Wdt.Ubyte4(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2camera:
                    self._m_values[i] = Wdt.M2camera(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2compbone:
                    self._m_values[i] = Wdt.M2compbone(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.pgd1_entry:
                    self._m_values[i] = Wdt.Pgd1Entry(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2array_uint16:
                    self._m_values[i] = Wdt.M2array(Wdt.M2arrayTypes.uint16, self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2batch:
                    self._m_values[i] = Wdt.M2batch(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2skinsection:
                    self._m_values[i] = Wdt.M2skinsection(self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2array_uint8:
                    self._m_values[i] = Wdt.M2array(Wdt.M2arrayTypes.uint8, self._io, self, self._root)
                elif _on == Wdt.M2arrayTypes.m2textureweight:
                    self._m_values[i] = Wdt.M2textureweight(self._io, self, self._root)

            self._io.seek(_pos)
            return self._m_values if hasattr(self, '_m_values') else None


    class ChunkMphd(KaitaiStruct):
        """Map Header.
        
        .. seealso::
           Source - https://wowdev.wiki/WDT#MPHD_chunk
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_flags = self._io.read_bytes(4)
            _io__raw_flags = KaitaiStream(BytesIO(self._raw_flags))
            self.flags = Wdt.MphdFlags(_io__raw_flags, self, self._root)
            self.lgt_file_data_id = self._io.read_u4le()
            self.occ_file_data_id = self._io.read_u4le()
            self.fogs_file_data_id = self._io.read_u4le()
            self.mpv_file_data_id = self._io.read_u4le()
            self.tex_file_data_id = self._io.read_u4le()
            self.wdl_file_data_id = self._io.read_u4le()
            self.pd4_file_data_id = self._io.read_u4le()


    class M2textureweight(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.weight = Wdt.M2track(Wdt.M2trackTypes.fixed16, self._io, self, self._root)


    class M2bounds(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.extent = Wdt.Caabox(self._io, self, self._root)
            self.radius = self._io.read_f4le()


    class M2camera(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = self._io.read_u4le()
            self.far_clip = self._io.read_f4le()
            self.near_clip = self._io.read_f4le()
            self.positions = Wdt.M2track(Wdt.M2trackTypes.todo, self._io, self, self._root)
            self.position_base = Wdt.C3vector(self._io, self, self._root)
            self.target_position = Wdt.M2track(Wdt.M2trackTypes.todo, self._io, self, self._root)
            self.target_position_base = Wdt.C3vector(self._io, self, self._root)
            self.roll = Wdt.M2track(Wdt.M2trackTypes.todo, self._io, self, self._root)
            self.fov = Wdt.M2track(Wdt.M2trackTypes.todo, self._io, self, self._root)


    class Ubyte4(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = [None] * (4)
            for i in range(4):
                self.value[i] = self._io.read_u1()



    class C34matrix(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.columns = [None] * (4)
            for i in range(4):
                self.columns[i] = Wdt.C3vector(self._io, self, self._root)



    class C3ray(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.origin = Wdt.C3vector(self._io, self, self._root)
            self.dir = Wdt.C3vector(self._io, self, self._root)


    class Cimvector(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.b = self._io.read_u1()
            self.g = self._io.read_u1()
            self.r = self._io.read_u1()
            self.a = self._io.read_u1()


    class ChunkPvbd(KaitaiStruct):
        """Map Particle Volume BD.
        
        .. seealso::
           Source - https://wowdev.wiki/WDT#PVBD
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.particle_volume_bds = []
            i = 0
            while not self._io.is_eof():
                self.particle_volume_bds.append(Wdt.ParticleVolumeBd(self._io, self, self._root))
                i += 1



    class C4plane(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.normal = Wdt.C3vector(self._io, self, self._root)
            self.distance = self._io.read_f4le()


    class MapFileDataIdSet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.root_adt_file_data_id = self._io.read_u4le()
            self.obj_0_adt_file_data_id = self._io.read_u4le()
            self.obj_1_adt_file_data_id = self._io.read_u4le()
            self.tex_0_adt_file_data_id = self._io.read_u4le()
            self.lod_adt_file_data_id = self._io.read_u4le()
            self.map_texture_file_data_id = self._io.read_u4le()
            self.map_texture_n_file_data_id = self._io.read_u4le()
            self.minimap_texture_file_data_id = self._io.read_u4le()


    class Cirect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.top = self._io.read_s4le()
            self.miny = self._io.read_s4le()
            self.left = self._io.read_s4le()
            self.minx = self._io.read_s4le()
            self.bottom = self._io.read_s4le()
            self.maxy = self._io.read_s4le()
            self.right = self._io.read_s4le()
            self.maxx = self._io.read_s4le()


    class C2ivector(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_s4le()
            self.y = self._io.read_s4le()


    class C3ivector(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_s4le()
            self.y = self._io.read_s4le()
            self.z = self._io.read_s4le()


    class U4Nested(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if True:
                self.num_timestamps = self._io.read_u4le()

            if True:
                self.ofs_timestamps = self._io.read_u4le()


        @property
        def inner(self):
            if hasattr(self, '_m_inner'):
                return self._m_inner if hasattr(self, '_m_inner') else None

            if True:
                _pos = self._io.pos()
                self._io.seek(self.ofs_timestamps)
                self._m_inner = [None] * (self.num_timestamps)
                for i in range(self.num_timestamps):
                    self._m_inner[i] = self._io.read_u4le()

                self._io.seek(_pos)

            return self._m_inner if hasattr(self, '_m_inner') else None


    class M2material(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_flags = self._io.read_bytes(2)
            _io__raw_flags = KaitaiStream(BytesIO(self._raw_flags))
            self.flags = Wdt.M2materialFlags(_io__raw_flags, self, self._root)
            self.blending_mode = KaitaiStream.resolve_enum(Wdt.M2materialBlendmodes, self._io.read_u2le())


    class ParticleVolumePd(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unknown1 = Wdt.C2vector(self._io, self, self._root)
            self.unknown2 = self._io.read_f4le()
            self.unknown3 = self._io.read_f4le()


    class M2color(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.color = Wdt.M2track(Wdt.M2trackTypes.c3vector, self._io, self, self._root)
            self.alpha = Wdt.M2track(Wdt.M2trackTypes.fixed16, self._io, self, self._root)


    class Frgb(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.r = self._io.read_f4le()
            self.g = self._io.read_f4le()
            self.b = self._io.read_f4le()


    class M2sequencefallback(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.something = self._io.read_u4le()
            self.somethingelse = self._io.read_u4le()


    class ModelParticleParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.colors = Wdt.Fblock(Wdt.M2arrayTypes.frgb, self._io, self, self._root)
            self.opacity = Wdt.Fblock(Wdt.M2arrayTypes.uint16, self._io, self, self._root)
            self.sizes = Wdt.Fblock(Wdt.M2arrayTypes.c2vector, self._io, self, self._root)
            self.d = [None] * (2)
            for i in range(2):
                self.d[i] = self._io.read_u4le()

            self.intensity = Wdt.Fblock(Wdt.M2arrayTypes.uint16, self._io, self, self._root)
            self.unk2 = Wdt.Fblock(Wdt.M2arrayTypes.uint16, self._io, self, self._root)
            self.unk = [None] * (3)
            for i in range(3):
                self.unk[i] = self._io.read_f4le()

            self.scales = Wdt.C3vector(self._io, self, self._root)
            self.slowdown = self._io.read_f4le()
            self.unknown1 = [None] * (2)
            for i in range(2):
                self.unknown1[i] = self._io.read_f4le()

            self.rotation = self._io.read_f4le()
            self.unknown2 = [None] * (2)
            for i in range(2):
                self.unknown2[i] = self._io.read_f4le()

            self.rot1 = Wdt.C3vector(self._io, self, self._root)
            self.rot2 = Wdt.C3vector(self._io, self, self._root)
            self.trans = Wdt.C3vector(self._io, self, self._root)
            self.f2 = [None] * (4)
            for i in range(4):
                self.f2[i] = self._io.read_f4le()

            self.unknown_reference = Wdt.M2array(Wdt.M2arrayTypes.todo, self._io, self, self._root)


    class M2event(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.identifier = (self._io.read_bytes(4)).decode(u"ASCII")
            self.data = self._io.read_u4le()
            self.bone = self._io.read_u4le()
            self.position = Wdt.C3vector(self._io, self, self._root)
            self.enabled = Wdt.M2trackbase(self._io, self, self._root)


    class C2vector(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()


    class M2texture(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(Wdt.M2textureTypes, self._io.read_u4le())
            self._raw_flags = self._io.read_bytes(4)
            _io__raw_flags = KaitaiStream(BytesIO(self._raw_flags))
            self.flags = Wdt.M2textureFlags(_io__raw_flags, self, self._root)
            if True:
                self.num_filename = self._io.read_u4le()

            if True:
                self.ofs_filename = self._io.read_u4le()


        @property
        def filename(self):
            if hasattr(self, '_m_filename'):
                return self._m_filename if hasattr(self, '_m_filename') else None

            if True:
                _pos = self._io.pos()
                self._io.seek(self.ofs_filename)
                self._m_filename = (self._io.read_bytes(self.num_filename)).decode(u"UTF-8")
                self._io.seek(_pos)

            return self._m_filename if hasattr(self, '_m_filename') else None


    class M2range(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.minimum = self._io.read_u4le()
            self.maximum = self._io.read_u4le()


    class C4ivector(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_s4le()
            self.y = self._io.read_s4le()
            self.z = self._io.read_s4le()
            self.w = self._io.read_s4le()


    class M2compbone(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key_bone_id = self._io.read_s4le()
            self._raw_flags = self._io.read_bytes(4)
            _io__raw_flags = KaitaiStream(BytesIO(self._raw_flags))
            self.flags = Wdt.M2compboneFlags(_io__raw_flags, self, self._root)
            self.parent_bone = self._io.read_s2le()
            self.submesh_id = self._io.read_u2le()
            self.bone_name_crc = self._io.read_u4le()
            self.translation = Wdt.M2track(Wdt.M2trackTypes.c3vector, self._io, self, self._root)
            self.rotation = Wdt.M2track(Wdt.M2trackTypes.m2compquat, self._io, self, self._root)
            self.scale = Wdt.M2track(Wdt.M2trackTypes.c3vector, self._io, self, self._root)
            self.pivot = Wdt.C3vector(self._io, self, self._root)


    class M2arrayStr(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num = self._io.read_u4le()
            self.offset = self._io.read_u4le()

        @property
        def arraydata(self):
            if hasattr(self, '_m_arraydata'):
                return self._m_arraydata if hasattr(self, '_m_arraydata') else None

            io = self._io
            _pos = io.pos()
            io.seek(self.offset)
            self._m_arraydata = (io.read_bytes(self.num)).decode(u"UTF-8")
            io.seek(_pos)
            return self._m_arraydata if hasattr(self, '_m_arraydata') else None


    class M2vertex(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pos = Wdt.C3vector(self._io, self, self._root)
            self.bone_weights = [None] * (4)
            for i in range(4):
                self.bone_weights[i] = self._io.read_u1()

            self.bone_indices = [None] * (4)
            for i in range(4):
                self.bone_indices[i] = self._io.read_u1()

            self.normal = Wdt.C3vector(self._io, self, self._root)
            self.tex_coords = [None] * (2)
            for i in range(2):
                self.tex_coords[i] = Wdt.C2vector(self._io, self, self._root)



    class ChunkMaoh(KaitaiStruct):
        """Height map.
        
        .. seealso::
           Source - https://wowdev.wiki/WDT#MAOH
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

        @property
        def note(self):
            if hasattr(self, '_m_note'):
                return self._m_note if hasattr(self, '_m_note') else None

            self._m_note = u"not implemented"
            return self._m_note if hasattr(self, '_m_note') else None


    class Fp69(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u2le()


    class UnknownChunk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

        @property
        def unknown_chunk(self):
            if hasattr(self, '_m_unknown_chunk'):
                return self._m_unknown_chunk if hasattr(self, '_m_unknown_chunk') else None

            self._m_unknown_chunk = True
            return self._m_unknown_chunk if hasattr(self, '_m_unknown_chunk') else None


    class Pgd1Entry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.geoset = self._io.read_u2le()


    class Caasphere(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.position = Wdt.C3vector(self._io, self, self._root)
            self.radius = self._io.read_f4le()


    class Fixed16(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value_raw = self._io.read_s2le()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = (self.value_raw / 32767.0)
            return self._m_value if hasattr(self, '_m_value') else None


    class Noop(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class C3vector(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.z = self._io.read_f4le()


    class ChunkMlta(KaitaiStruct):
        """Map Data Unknown.
        
        .. seealso::
           Source - https://wowdev.wiki/WDT#MLTA
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.map_ltas = []
            i = 0
            while not self._io.is_eof():
                self.map_ltas.append(Wdt.MapLta(self._io, self, self._root))
                i += 1



    class M2track(KaitaiStruct):
        def __init__(self, m2track_type, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.m2track_type = m2track_type
            self._read()

        def _read(self):
            self.interpolation_type = KaitaiStream.resolve_enum(Wdt.M2trackInterpolationTypes, self._io.read_u2le())
            self.global_sequence = self._io.read_s2le()
            if True:
                self.num_timestamps = self._io.read_u4le()

            if True:
                self.ofs_timestamps = self._io.read_u4le()

            _on = self.m2track_type
            if _on == Wdt.M2trackTypes.uint8:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.m2array_uint8, self._io, self, self._root)
            elif _on == Wdt.M2trackTypes.c2vector:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.m2array_c2vector, self._io, self, self._root)
            elif _on == Wdt.M2trackTypes.c4quaternion:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.m2array_c4quaternion, self._io, self, self._root)
            elif _on == Wdt.M2trackTypes.m2compquat:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.m2array_m2compquat, self._io, self, self._root)
            elif _on == Wdt.M2trackTypes.uint16:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.m2array_uint16, self._io, self, self._root)
            elif _on == Wdt.M2trackTypes.float:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.m2array_float, self._io, self, self._root)
            elif _on == Wdt.M2trackTypes.fixed16:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.m2array_fixed16, self._io, self, self._root)
            elif _on == Wdt.M2trackTypes.todo:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.todo, self._io, self, self._root)
            elif _on == Wdt.M2trackTypes.c3vector:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.m2array_c3vector, self._io, self, self._root)

        @property
        def timestamps(self):
            if hasattr(self, '_m_timestamps'):
                return self._m_timestamps if hasattr(self, '_m_timestamps') else None

            if True:
                _pos = self._io.pos()
                self._io.seek(self.ofs_timestamps)
                self._m_timestamps = [None] * (self.num_timestamps)
                for i in range(self.num_timestamps):
                    self._m_timestamps[i] = Wdt.U4Nested(self._io, self, self._root)

                self._io.seek(_pos)

            return self._m_timestamps if hasattr(self, '_m_timestamps') else None


    class Crange(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.min = self._io.read_f4le()
            self.max = self._io.read_f4le()


    class WdtChunk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.chunk_type_raw = (self._io.read_bytes(4)).decode(u"UTF-8")
            self.chunk_size = self._io.read_u4le()
            _on = (self.chunk_type_raw)[::-1]
            if _on == u"MSLT":
                self._raw_chunk_data = self._io.read_bytes(self.chunk_size)
                _io__raw_chunk_data = KaitaiStream(BytesIO(self._raw_chunk_data))
                self.chunk_data = Wdt.ChunkMslt(_io__raw_chunk_data, self, self._root)
            elif _on == u"MPHD":
                self._raw_chunk_data = self._io.read_bytes(self.chunk_size)
                _io__raw_chunk_data = KaitaiStream(BytesIO(self._raw_chunk_data))
                self.chunk_data = Wdt.ChunkMphd(_io__raw_chunk_data, self, self._root)
            elif _on == u"MAOH":
                self._raw_chunk_data = self._io.read_bytes(self.chunk_size)
                _io__raw_chunk_data = KaitaiStream(BytesIO(self._raw_chunk_data))
                self.chunk_data = Wdt.ChunkMaoh(_io__raw_chunk_data, self, self._root)
            elif _on == u"MPL3":
                self._raw_chunk_data = self._io.read_bytes(self.chunk_size)
                _io__raw_chunk_data = KaitaiStream(BytesIO(self._raw_chunk_data))
                self.chunk_data = Wdt.ChunkMpl3(_io__raw_chunk_data, self, self._root)
            elif _on == u"MAOI":
                self._raw_chunk_data = self._io.read_bytes(self.chunk_size)
                _io__raw_chunk_data = KaitaiStream(BytesIO(self._raw_chunk_data))
                self.chunk_data = Wdt.ChunkMaoi(_io__raw_chunk_data, self, self._root)
            elif _on == u"MAID":
                self._raw_chunk_data = self._io.read_bytes(self.chunk_size)
                _io__raw_chunk_data = KaitaiStream(BytesIO(self._raw_chunk_data))
                self.chunk_data = Wdt.ChunkMaid(_io__raw_chunk_data, self, self._root)
            elif _on == u"PVBD":
                self._raw_chunk_data = self._io.read_bytes(self.chunk_size)
                _io__raw_chunk_data = KaitaiStream(BytesIO(self._raw_chunk_data))
                self.chunk_data = Wdt.ChunkPvbd(_io__raw_chunk_data, self, self._root)
            elif _on == u"PVMI":
                self._raw_chunk_data = self._io.read_bytes(self.chunk_size)
                _io__raw_chunk_data = KaitaiStream(BytesIO(self._raw_chunk_data))
                self.chunk_data = Wdt.ChunkPvmi(_io__raw_chunk_data, self, self._root)
            elif _on == u"MAIN":
                self._raw_chunk_data = self._io.read_bytes(self.chunk_size)
                _io__raw_chunk_data = KaitaiStream(BytesIO(self._raw_chunk_data))
                self.chunk_data = Wdt.ChunkMain(_io__raw_chunk_data, self, self._root)
            elif _on == u"PVPD":
                self._raw_chunk_data = self._io.read_bytes(self.chunk_size)
                _io__raw_chunk_data = KaitaiStream(BytesIO(self._raw_chunk_data))
                self.chunk_data = Wdt.ChunkPvpd(_io__raw_chunk_data, self, self._root)
            elif _on == u"MLTA":
                self._raw_chunk_data = self._io.read_bytes(self.chunk_size)
                _io__raw_chunk_data = KaitaiStream(BytesIO(self._raw_chunk_data))
                self.chunk_data = Wdt.ChunkMlta(_io__raw_chunk_data, self, self._root)
            else:
                self._raw_chunk_data = self._io.read_bytes(self.chunk_size)
                _io__raw_chunk_data = KaitaiStream(BytesIO(self._raw_chunk_data))
                self.chunk_data = Wdt.Noop(_io__raw_chunk_data, self, self._root)

        @property
        def chunk_type(self):
            if hasattr(self, '_m_chunk_type'):
                return self._m_chunk_type if hasattr(self, '_m_chunk_type') else None

            self._m_chunk_type = (self.chunk_type_raw)[::-1]
            return self._m_chunk_type if hasattr(self, '_m_chunk_type') else None


    class ChunkPvmi(KaitaiStruct):
        """Map Particle Volume Info. If PVPD is already read, it is nulled. If PVMI comes first, PVPD may be non-null. Actual files order as PVMI PVPD PVBD.
        
        .. seealso::
           Source - https://wowdev.wiki/WDT#PVMI
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

        @property
        def note(self):
            if hasattr(self, '_m_note'):
                return self._m_note if hasattr(self, '_m_note') else None

            self._m_note = u"not implemented"
            return self._m_note if hasattr(self, '_m_note') else None


    class M2sequenceFlags(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.set_0x80 = self._io.read_bits_int_le(1) != 0
            self.unknown1 = self._io.read_bits_int_le(1) != 0
            self.unknown2 = self._io.read_bits_int_le(1) != 0
            self.unknown3 = self._io.read_bits_int_le(1) != 0
            self.runtime1 = self._io.read_bits_int_le(1) != 0
            self.is_primary = self._io.read_bits_int_le(1) != 0
            self.is_alias = self._io.read_bits_int_le(1) != 0
            self.is_blended = self._io.read_bits_int_le(1) != 0
            self.sequence_stored_in_model = self._io.read_bits_int_le(1) != 0
            self.blendtime_range = self._io.read_bits_int_le(1) != 0
            self.unknown4 = self._io.read_bits_int_le(1) != 0
            self.unknown5 = self._io.read_bits_int_le(1) != 0
            self.unused1 = self._io.read_bits_int_le(1) != 0
            self.unused2 = self._io.read_bits_int_le(1) != 0
            self.unused3 = self._io.read_bits_int_le(1) != 0
            self.unused4 = self._io.read_bits_int_le(1) != 0


    class M2parttrack(KaitaiStruct):
        def __init__(self, m2array_type, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.m2array_type = m2array_type
            self._read()

        def _read(self):
            self.times = Wdt.M2array(Wdt.M2arrayTypes.fixed16, self._io, self, self._root)
            _on = self.m2array_type
            if _on == Wdt.M2arrayTypes.fixed16:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.fixed16, self._io, self, self._root)


    class Vector2fp69(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = Wdt.Fp69(self._io, self, self._root)
            self.y = Wdt.Fp69(self._io, self, self._root)


    class MapSpotLight(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = self._io.read_u4le()
            self.color = Wdt.Cargb(self._io, self, self._root)
            self.position = Wdt.C3vector(self._io, self, self._root)
            self.range_attenuation_start = self._io.read_f4le()
            self.range_attenuiation_end = self._io.read_f4le()
            self.intensity = self._io.read_f4le()
            self.rotation = Wdt.C3vector(self._io, self, self._root)
            self.falloff_exponent = self._io.read_f4le()
            self.inner_radius = self._io.read_f4le()
            self.outer_radius = self._io.read_f4le()
            self.unknown = [None] * (2)
            for i in range(2):
                self.unknown[i] = self._io.read_s2le()



    class M2compboneFlags(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ignore_parent_translate = self._io.read_bits_int_le(1) != 0
            self.ignore_parent_scale = self._io.read_bits_int_le(1) != 0
            self.ignore_parent_rotation = self._io.read_bits_int_le(1) != 0
            self.spherical_billboard = self._io.read_bits_int_le(1) != 0
            self.cyl_billboard_lock_x = self._io.read_bits_int_le(1) != 0
            self.cyl_billboard_lock_y = self._io.read_bits_int_le(1) != 0
            self.cyl_billboard_lock_z = self._io.read_bits_int_le(1) != 0
            self.unused1 = self._io.read_bits_int_le(1) != 0
            self.unused2 = self._io.read_bits_int_le(1) != 0
            self.transformed = self._io.read_bits_int_le(1) != 0
            self.kinematic_bone = self._io.read_bits_int_le(1) != 0
            self.unused3 = self._io.read_bits_int_le(1) != 0
            self.helmet_anim_scaled = self._io.read_bits_int_le(1) != 0
            self.something_sequence_id = self._io.read_bits_int_le(1) != 0


    class MaoiEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tile_x = self._io.read_u2le()
            self.tile_y = self._io.read_u2le()
            self.offset = self._io.read_u4le()
            self.size = self._io.read_u4le()


    class M2textureFlags(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.texture_wrap_x = self._io.read_bits_int_le(1) != 0
            self.texture_wrap_y = self._io.read_bits_int_le(1) != 0


    class ChunkPvpd(KaitaiStruct):
        """Map Particle Volume PD.
        
        .. seealso::
           Source - https://wowdev.wiki/WDT#PVPD
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.particle_volume_pds = []
            i = 0
            while not self._io.is_eof():
                self.particle_volume_pds.append(Wdt.ParticleVolumePd(self._io, self, self._root))
                i += 1



    class ChunkMaoi(KaitaiStruct):
        """Height map indexes.
        
        .. seealso::
           Source - https://wowdev.wiki/WDT#MAOI
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.maois = []
            i = 0
            while not self._io.is_eof():
                self.maois.append(Wdt.MaoiEntry(self._io, self, self._root))
                i += 1



    class Cargb(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.r = self._io.read_u1()
            self.g = self._io.read_u1()
            self.b = self._io.read_u1()
            self.a = self._io.read_u1()


    class M2compquat(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_s2le()
            self.y = self._io.read_s2le()
            self.z = self._io.read_s2le()
            self.w = self._io.read_s2le()


    class M2shadowbatch(KaitaiStruct):
        """Shadow Batches
        
        Generated on the fly, conditionally:
        if !(batches[i].flags & 4) && !batches[i].texunit
           && !(renderflags[batches[i].renderFlag].flags & 0x40)
           && (renderflags[batches[i].renderFlag].blendingmode < 2u
           || renderflags[batches[i].renderFlag].flags & 0x80)
        
        .. seealso::
           Source - https://wowdev.wiki/M2/.skin#shadow_batches
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.flags = self._io.read_u1()
            self.flags2 = self._io.read_u1()
            self.unknown1 = self._io.read_u2le()
            self.submesh_id = self._io.read_u2le()
            self.texture_id = self._io.read_u2le()
            self.color_id = self._io.read_u2le()
            self.transparency_id = self._io.read_u2le()


    class M2trackbase(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.interpolation_type = KaitaiStream.resolve_enum(Wdt.M2trackInterpolationTypes, self._io.read_u2le())
            self.global_sequence = self._io.read_s2le()
            self.timestamps = Wdt.M2array(Wdt.M2arrayTypes.m2array_uint32, self._io, self, self._root)


    class C4vector(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.z = self._io.read_f4le()
            self.w = self._io.read_f4le()


    class C33matrix(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.columns = [None] * (3)
            for i in range(3):
                self.columns[i] = Wdt.C3vector(self._io, self, self._root)



    class M2particle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.old = Wdt.M2particleOld(self._io, self, self._root)
            self.multi_texture_param0 = [None] * (2)
            for i in range(2):
                self.multi_texture_param0[i] = Wdt.Vector2fp69(self._io, self, self._root)

            self.multi_texture_param1 = [None] * (2)
            for i in range(2):
                self.multi_texture_param1[i] = Wdt.Vector2fp69(self._io, self, self._root)



    class MapLta(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unknown1 = self._io.read_f4le()
            self.unknown2 = self._io.read_f4le()
            self.unknown3 = self._io.read_u4le()


    class MapAreaFlags(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.has_adt = self._io.read_bits_int_le(1) != 0
            self.all_water = self._io.read_bits_int_le(1) != 0
            self.loaded = self._io.read_bits_int_le(1) != 0


    class MapAreaInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_flags = self._io.read_bytes(4)
            _io__raw_flags = KaitaiStream(BytesIO(self._raw_flags))
            self.flags = Wdt.MapAreaFlags(_io__raw_flags, self, self._root)
            self.async_id = self._io.read_u4le()


    class ChunkMpl3(KaitaiStruct):
        """MPL3 - Nothing known about this type.
        
        .. seealso::
           Source - https://wowdev.wiki/WDT#MPL3_.28Shadowlands.2B.29
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

        @property
        def note(self):
            if hasattr(self, '_m_note'):
                return self._m_note if hasattr(self, '_m_note') else None

            self._m_note = u"not implemented"
            return self._m_note if hasattr(self, '_m_note') else None


    class Fblock(KaitaiStruct):
        def __init__(self, m2array_type, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.m2array_type = m2array_type
            self._read()

        def _read(self):
            self.timestamps = Wdt.M2array(Wdt.M2arrayTypes.uint16, self._io, self, self._root)
            _on = self.m2array_type
            if _on == Wdt.M2arrayTypes.fixed16:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.fixed16, self._io, self, self._root)
            elif _on == Wdt.M2arrayTypes.uint8:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.uint8, self._io, self, self._root)
            elif _on == Wdt.M2arrayTypes.todo:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.todo, self._io, self, self._root)
            elif _on == Wdt.M2arrayTypes.c4quaternion:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.c4quaternion, self._io, self, self._root)
            elif _on == Wdt.M2arrayTypes.c3vector:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.c3vector, self._io, self, self._root)
            elif _on == Wdt.M2arrayTypes.float:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.float, self._io, self, self._root)
            elif _on == Wdt.M2arrayTypes.c4vector:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.c4vector, self._io, self, self._root)
            elif _on == Wdt.M2arrayTypes.c2vector:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.c2vector, self._io, self, self._root)
            elif _on == Wdt.M2arrayTypes.uint16:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.uint16, self._io, self, self._root)
            elif _on == Wdt.M2arrayTypes.frgb:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.frgb, self._io, self, self._root)
            elif _on == Wdt.M2arrayTypes.m2compquat:
                self.values = Wdt.M2array(Wdt.M2arrayTypes.m2compquat, self._io, self, self._root)


    class Todo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.todo_nothing = self._io.read_u4le()


    class M2box(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.model_rotation_speed_min = Wdt.C3vector(self._io, self, self._root)
            self.model_rotation_speed_max = Wdt.C3vector(self._io, self, self._root)


    class ChunkMain(KaitaiStruct):
        """Map tile table. Needs to contain 64x64 (4096) entries.
        
        .. seealso::
           Source - https://wowdev.wiki/WDT#MAIN_chunk
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.areas = []
            i = 0
            while not self._io.is_eof():
                self.areas.append(Wdt.MapAreaInfo(self._io, self, self._root))
                i += 1



    class Caabox(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.min = Wdt.C3vector(self._io, self, self._root)
            self.max = Wdt.C3vector(self._io, self, self._root)


    class M2skinsection(KaitaiStruct):
        """Submesh information.
        
        .. seealso::
           Source - https://wowdev.wiki/M2/.skin#Submeshes
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.skin_section_id = self._io.read_u2le()
            self.level = self._io.read_u2le()
            self.vertex_start = self._io.read_u2le()
            self.vertex_count = self._io.read_u2le()
            self.index_start = self._io.read_u2le()
            self.index_count = self._io.read_u2le()
            self.bone_count = self._io.read_u2le()
            self.bone_combo_index = self._io.read_u2le()
            self.bone_influences = self._io.read_u2le()
            self.center_bone_index = self._io.read_u2le()
            self.center_position = Wdt.C3vector(self._io, self, self._root)
            self.sort_center_position = Wdt.C3vector(self._io, self, self._root)
            self.sort_radius = self._io.read_f4le()


    class M2loop(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timestamp = self._io.read_u4le()


    class M2materialFlags(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unlit = self._io.read_bits_int_le(1) != 0
            self.unfogged = self._io.read_bits_int_le(1) != 0
            self.twosided = self._io.read_bits_int_le(1) != 0
            self.depthtest = self._io.read_bits_int_le(1) != 0
            self.depthwrite = self._io.read_bits_int_le(1) != 0
            self.unused1 = self._io.read_bits_int_le(1) != 0
            self.shadowbatch1 = self._io.read_bits_int_le(1) != 0
            self.shadowbatch2 = self._io.read_bits_int_le(1) != 0
            self.unused2 = self._io.read_bits_int_le(1) != 0
            self.unused3 = self._io.read_bits_int_le(1) != 0
            self.unknown1 = self._io.read_bits_int_le(1) != 0
            self.preventalpha = self._io.read_bits_int_le(1) != 0


    class M2particlesFlags(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.lit = self._io.read_bits_int_le(1) != 0
            self.unknown1 = self._io.read_bits_int_le(1) != 0
            self.unknown2 = self._io.read_bits_int_le(1) != 0
            self.worldspace = self._io.read_bits_int_le(1) != 0
            self.notrail = self._io.read_bits_int_le(1) != 0
            self.unlightning = self._io.read_bits_int_le(1) != 0
            self.burst_multiplier = self._io.read_bits_int_le(1) != 0
            self.modelspace = self._io.read_bits_int_le(1) != 0
            self.unknown3 = self._io.read_bits_int_le(1) != 0
            self.randomspawn = self._io.read_bits_int_le(1) != 0
            self.pinned = self._io.read_bits_int_le(1) != 0
            self.unknown4 = self._io.read_bits_int_le(1) != 0
            self.nobillboard = self._io.read_bits_int_le(1) != 0
            self.groundclamp = self._io.read_bits_int_le(1) != 0
            self.unknown5 = self._io.read_bits_int_le(1) != 0
            self.unknown6 = self._io.read_bits_int_le(1) != 0
            self.random_texture = self._io.read_bits_int_le(1) != 0
            self.outward = self._io.read_bits_int_le(1) != 0
            self.inward_maybe = self._io.read_bits_int_le(1) != 0
            self.scale_vary_separately = self._io.read_bits_int_le(1) != 0
            self.unknown7 = self._io.read_bits_int_le(1) != 0
            self.random_flipbookstart = self._io.read_bits_int_le(1) != 0
            self.no_throttle_distance = self._io.read_bits_int_le(1) != 0
            self.compressed_gravity = self._io.read_bits_int_le(1) != 0
            self.bone_generator = self._io.read_bits_int_le(1) != 0
            self.unknown8 = self._io.read_bits_int_le(1) != 0
            self.no_throttle_distance2 = self._io.read_bits_int_le(1) != 0
            self.unknown9 = self._io.read_bits_int_le(1) != 0
            self.multi_texture = self._io.read_bits_int_le(1) != 0
            self.unknown10 = self._io.read_bits_int_le(1) != 0
            self.unknown11 = self._io.read_bits_int_le(1) != 0
            self.unknown12 = self._io.read_bits_int_le(1) != 0


    class M2arrayTodo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class C4quaternion(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.z = self._io.read_f4le()
            self.w = self._io.read_f4le()


    class Crect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.top = self._io.read_f4le()
            self.miny = self._io.read_f4le()
            self.left = self._io.read_f4le()
            self.minx = self._io.read_f4le()
            self.bottom = self._io.read_f4le()
            self.maxy = self._io.read_f4le()
            self.right = self._io.read_f4le()
            self.maxx = self._io.read_f4le()


    class M2attachment(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = self._io.read_u4le()
            self.bone = self._io.read_u2le()
            self.unknown1 = self._io.read_u2le()
            self.position = Wdt.C3vector(self._io, self, self._root)
            self.animate_attached = Wdt.M2track(Wdt.M2trackTypes.uint8, self._io, self, self._root)


    class M2ribbon(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ribbon_id = self._io.read_u4le()
            self.bone_index = self._io.read_u4le()
            self.position = Wdt.C3vector(self._io, self, self._root)
            if True:
                self.num_texture_indices = self._io.read_u4le()

            if True:
                self.ofs_texture_indices = self._io.read_u4le()

            if True:
                self.num_material_indices = self._io.read_u4le()

            if True:
                self.ofs_material_indices = self._io.read_u4le()

            self.color_track = Wdt.M2track(Wdt.M2trackTypes.c3vector, self._io, self, self._root)
            self.alpha_track = Wdt.M2track(Wdt.M2trackTypes.fixed16, self._io, self, self._root)
            self.height_above_track = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.height_below_track = Wdt.M2track(Wdt.M2trackTypes.float, self._io, self, self._root)
            self.edges_per_second = self._io.read_f4le()
            self.edge_lifetime = self._io.read_f4le()
            self.gravity = self._io.read_f4le()
            self.texture_rows = self._io.read_u2le()
            self.texture_cols = self._io.read_u2le()
            self.tex_slot_track = Wdt.M2track(Wdt.M2trackTypes.uint16, self._io, self, self._root)
            self.visibility_track = Wdt.M2track(Wdt.M2trackTypes.uint8, self._io, self, self._root)
            self.priority_plane = self._io.read_s2le()
            self.padding = self._io.read_u2le()

        @property
        def material_indices(self):
            if hasattr(self, '_m_material_indices'):
                return self._m_material_indices if hasattr(self, '_m_material_indices') else None

            if True:
                _pos = self._io.pos()
                self._io.seek(self.ofs_material_indices)
                self._m_material_indices = [None] * (self.num_material_indices)
                for i in range(self.num_material_indices):
                    self._m_material_indices[i] = self._io.read_u2le()

                self._io.seek(_pos)

            return self._m_material_indices if hasattr(self, '_m_material_indices') else None

        @property
        def texture_indices(self):
            if hasattr(self, '_m_texture_indices'):
                return self._m_texture_indices if hasattr(self, '_m_texture_indices') else None

            if True:
                _pos = self._io.pos()
                self._io.seek(self.ofs_texture_indices)
                self._m_texture_indices = [None] * (self.num_texture_indices)
                for i in range(self.num_texture_indices):
                    self._m_texture_indices[i] = self._io.read_u2le()

                self._io.seek(_pos)

            return self._m_texture_indices if hasattr(self, '_m_texture_indices') else None


    class C3svector(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_s2le()
            self.y = self._io.read_s2le()
            self.z = self._io.read_s2le()


    class Cirange(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.min = self._io.read_s4le()
            self.max = self._io.read_s4le()



