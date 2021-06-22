# from https://github.com/marlamin/wow.tools/blob/master/mv/anims.js
# Last updated during the 9.1 PTR
# (thanks Marlamin)
enums:
    anim_names:
        0: stand  # Idle
        1: death
        2: spell
        3: stop  # Idle (no movement)
        4: walk
        5: run
        6: dead
        7: rise
        8: stand_wound  # Wound (idle)
        9: combat_wound  # Wound (combat)
        10: combat_critical  # Wound (critical)
        11: shuffle_left
        12: shuffle_right
        13: walk_backwards
        14: stun
        15: hands_closed  # Idle (no movement, hands closed)
        16: attack_unarmed
        17: attack_1h
        18: attack_2h
        19: attack_2h_l  # 2H Large
        20: parry_unarmed
        21: parry_1h
        22: parry_2h
        23: parry_2h_l
        24: shield_block
        25: ready_unarmed
        26: ready_1h
        27: ready_2h
        28: ready_2h_l  # 2H Large
        29: ready_bow
        30: dodge
        31: spell_precast
        32: spell_cast
        33: spell_cast_area
        34: npc_welcome
        35: npc_goodbye
        36: block
        37: jump_start
        38: jump
        39: jump_end
        40: fall
        41: swim_idle
        42: swim
        43: swim_left
        44: swim_right
        45: swim_backwards
        46: attack_bow
        47: fire_bow
        48: ready_rifle
        49: attack_rifle
        50: loot
        51: ready_spell_directed
        52: ready_spell_omni
        53: spell_cast_directed
        54: spell_cast_omni
        55: battle_roar
        56: ready_ability
        57: special_1h  # Critical 1H
        58: special_2h  # Critical 2H
        59: shield_bash
        60: emote_talk
        61: emote_eat
        62: emote_work
        63: emote_use_standing  # Craft
        64: emote_talk_exclamation  # Yell
        65: emote_talk_question
        66: emote_bow
        67: emote_wave
        68: emote_cheer
        69: emote_dance
        70: emote_laugh
        71: emote_sleep
        72: emote_sit_ground
        73: emote_rude
        74: emote_roar
        75: emote_kneel
        76: emote_kiss
        77: emote_cry
        78: emote_chicken
        79: emote_beg
        80: emote_applaud  # Clap
        81: emote_shout
        82: emote_flex
        83: emote_shy
        84: emote_point
        85: attack_1h_pierce  # Stab (Right)
        86: attack_2h_loose_pierce
        87: attack_off  # Attack (1H Left)
        88: attack_off_pierce  # Stab (Left)
        89: sheath  # Sheathe (Back)
        90: hip_sheath  # Sheathe (Sides)
        91: mount
        92: run_right
        93: run_left
        94: mount_special
        95: kick
        96: sit_ground_down
        97: sit_ground
        98: sit_ground_up
        99: sleep_down
        100: sleep
        101: sleep_up
        102: sit_chair_low
        103: sit_chair_med
        104: sit_chair_high
        105: load_bow
        106: load_rifle
        107: attack_thrown  # Shoot (Wand)
        108: ready_thrown  # Ready (Wand)
        109: hold_bow  # Aim (Bow)
        110: hold_rifle  # Aim (Gun/Crossbow)
        111: hold_thrown  # Ready (Thrown)
        112: load_thrown  # Ready (Thrown)
        113: emote_salute
        114: kneel_start
        115: kneel_loop
        116: kneel_end
        117: attack_unarmed_off
        118: special_unarmed  # Critical (Unarmed)
        119: stealth_walk  # Stealth (Walk)
        120: stealth_stand  # Stealth (Idle)
        121: knockdown
        122: eating_loop
        123: use_standing_loop  # Craft
        124: channel_cast_directed  # Channel 1
        125: channel_cast_omni  # Channel 2
        126: whirlwind  # Bladestorm
        127: birth  # Emerge
        128: use_standing_start  # Craft (Begin)
        129: use_standing_end  # Craft (End)
        130: creature_special
        131: drown
        132: drowned
        133: fishing_cast
        134: fishing_loop
        135: fly
        136: emote_work_no_sheathe  # Smith
        137: emote_stun_no_sheathe  # Stun
        138: emote_use_standing_no_sheathe  # Craft
        139: spell_sleep_down
        140: spell_kneel_start
        141: spell_kneel_loop
        142: spell_kneel_end
        143: sprint
        144: in_flight
        145: spawn
        146: close
        147: closed
        148: open
        149: opened
        150: destroy
        151: destroyed
        152: rebuild
        153: custom0
        154: custom1
        155: custom2
        156: custom3
        157: despawn
        158: hold
        159: decay
        160: bow_pull
        161: bow_release
        162: ship_start
        163: ship_moving
        164: ship_stop
        165: group_arrow
        166: arrow
        167: corpse_arrow
        168: guide_arrow
        169: sway
        170: druid_cat_pounce
        171: druid_cat_rip
        172: druid_cat_rake
        173: druid_cat_ravage
        174: druid_cat_claw
        175: druid_cat_cower
        176: druid_bear_swipe
        177: druid_bear_bite
        178: druid_bear_maul
        179: druid_bear_bash
        180: dragon_tail  # Tail swipe
        181: dragon_stomp  # Thunder Clap
        182: dragon_spit
        183: dragon_spit_hover
        184: dragon_spit_fly
        185: emote_yes
        186: emote_no
        187: jump_land_run  # Land & Run
        188: loot_hold
        189: loot_up
        190: stand_high
        191: impact
        192: lift_off
        193: hover  # Levitate
        194: succubus_entice
        195: emote_train
        196: emote_dead
        197: emote_dance_once
        198: deflect
        199: emote_eat_no_sheathe  # Eat/Drink
        200: land
        201: submerge
        202: submerged
        203: cannibalize
        204: arrow_birth
        205: group_arrow_birth
        206: corpse_arrow_birth
        207: guide_arrow_birth
        208: emote_talk_no_sheathe  # Talk
        209: emote_point_no_sheathe  # Point
        210: emote_salute_no_sheathe  # Salute
        211: emote_dance_special  # Dance Special (human only)
        212: mutilate  # Stab
        213: custom_spell01  # Boss Cast 1
        214: custom_spell02  # Boss Channel 1
        215: custom_spell03  # Suspended (Bolvar) (human only)
        216: custom_spell04  # Knock on Door (human only)
        217: custom_spell05  # Boss Precast
        218: custom_spell06  # Boss Channel 2
        219: custom_spell07  # Boss Channel End
        220: custom_spell08  # Boss Cast 2
        221: custom_spell09
        222: custom_spell10
        223: stealth_run
        224: emerge
        225: cower
        226: grab
        227: grab_closed
        228: grab_thrown
        229: fly_stand  # Fly (Idle)
        230: fly_death
        231: fly_spell
        232: fly_stop
        233: fly_walk
        234: fly_run
        235: fly_dead
        236: fly_rise
        237: fly_stand_wound
        238: fly_combat_wound
        239: fly_combat_critical
        240: fly_shuffle_left
        241: fly_shuffle_right
        242: fly_walk_backwards
        243: fly_stun  # Fly (Backwards)
        244: fly_hands_closed
        245: fly_attack_unarmed
        246: fly_attack_1h
        247: fly_attack_2h
        248: fly_attack_2h_l
        249: fly_parry_unarmed
        250: fly_parry_1h
        251: fly_parry_2h
        252: fly_parry_2h_l
        253: fly_shield_block
        254: fly_ready_unarmed  # Fly (Idle)
        255: fly_ready_1h
        256: fly_ready_2h
        257: fly_ready_2h_l
        258: fly_ready_bow
        259: fly_dodge
        260: fly_spell_precast
        261: fly_spell_cast
        262: fly_spell_cast_area
        263: fly_npc_welcome
        264: fly_npc_goodbye
        265: fly_block
        266: fly_jump_start
        267: fly_jump
        268: fly_jump_end
        269: fly_fall
        270: fly_swim_idle
        271: fly_swim
        272: fly_swim_left
        273: fly_swim_right
        274: fly_swim_backwards
        275: fly_attack_bow
        276: fly_fire_bow
        277: fly_ready_rifle
        278: fly_attack_rifle
        279: fly_loot
        280: fly_ready_spell_directed
        281: fly_ready_spell_omni
        282: fly_spell_cast_directed
        283: fly_spell_cast_omni
        284: fly_battle_roar
        285: fly_ready_ability
        286: fly_special_1h
        287: fly_special_2h
        288: fly_shield_bash
        289: fly_emote_talk
        290: fly_emote_eat
        291: fly_emote_work
        292: fly_emote_use_standing
        293: fly_emote_talk_exclamation
        294: fly_emote_talk_question
        295: fly_emote_bow
        296: fly_emote_wave
        297: fly_emote_cheer
        298: fly_emote_dance
        299: fly_emote_laugh
        300: fly_emote_sleep
        301: fly_emote_sit_ground
        302: fly_emote_rude
        303: fly_emote_roar
        304: fly_emote_kneel
        305: fly_emote_kiss
        306: fly_emote_cry
        307: fly_emote_chicken
        308: fly_emote_beg
        309: fly_emote_applaud
        310: fly_emote_shout
        311: fly_emote_flex
        312: fly_emote_shy
        313: fly_emote_point
        314: fly_attack_1h_pierce
        315: fly_attack_2h_loose_pierce
        316: fly_attack_off
        317: fly_attack_off_pierce
        318: fly_sheath
        319: fly_hip_sheath
        320: fly_mount
        321: fly_run_right
        322: fly_run_left
        323: fly_mount_special
        324: fly_kick
        325: fly_sit_ground_down
        326: fly_sit_ground
        327: fly_sit_ground_up
        328: fly_sleep_down
        329: fly_sleep
        330: fly_sleep_up
        331: fly_sit_chair_low
        332: fly_sit_chair_med
        333: fly_sit_chair_high
        334: fly_load_bow
        335: fly_load_rifle
        336: fly_attack_thrown
        337: fly_ready_thrown
        338: fly_hold_bow
        339: fly_hold_rifle
        340: fly_hold_thrown
        341: fly_load_thrown
        342: fly_emote_salute
        343: fly_kneel_start
        344: fly_kneel_loop
        345: fly_kneel_end
        346: fly_attack_unarmed_off
        347: fly_special_unarmed
        348: fly_stealth_walk
        349: fly_stealth_stand
        350: fly_knockdown
        351: fly_eating_loop
        352: fly_use_standing_loop
        353: fly_channel_cast_directed
        354: fly_channel_cast_omni
        355: fly_whirlwind
        356: fly_birth
        357: fly_use_standing_start
        358: fly_use_standing_end
        359: fly_creature_special
        360: fly_drown
        361: fly_drowned
        362: fly_fishing_cast
        363: fly_fishing_loop
        364: fly_fly
        365: fly_emote_work_no_sheathe
        366: fly_emote_stun_no_sheathe
        367: fly_emote_use_standing_no_sheathe
        368: fly_spell_sleep_down
        369: fly_spell_kneel_start
        370: fly_spell_kneel_loop
        371: fly_spell_kneel_end
        372: fly_sprint
        373: fly_in_flight
        374: fly_spawn
        375: fly_close
        376: fly_closed
        377: fly_open
        378: fly_opened
        379: fly_destroy
        380: fly_destroyed
        381: fly_rebuild
        382: fly_custom0
        383: fly_custom1
        384: fly_custom2
        385: fly_custom3
        386: fly_despawn
        387: fly_hold
        388: fly_decay
        389: fly_bow_pull
        390: fly_bow_release
        391: fly_ship_start
        392: fly_ship_moving
        393: fly_ship_stop
        394: fly_group_arrow
        395: fly_arrow
        396: fly_corpse_arrow
        397: fly_guide_arrow
        398: fly_sway
        399: fly_druid_cat_pounce
        400: fly_druid_cat_rip
        401: fly_druid_cat_rake
        402: fly_druid_cat_ravage
        403: fly_druid_cat_claw
        404: fly_druid_cat_cower
        405: fly_druid_bear_swipe
        406: fly_druid_bear_bite
        407: fly_druid_bear_maul
        408: fly_druid_bear_bash
        409: fly_dragon_tail
        410: fly_dragon_stomp
        411: fly_dragon_spit
        412: fly_dragon_spit_hover
        413: fly_dragon_spit_fly
        414: fly_emote_yes
        415: fly_emote_no
        416: fly_jump_land_run
        417: fly_loot_hold
        418: fly_loot_up
        419: fly_stand_high
        420: fly_impact
        421: fly_lift_off
        422: fly_hover
        423: fly_succubus_entice
        424: fly_emote_train
        425: fly_emote_dead
        426: fly_emote_dance_once
        427: fly_deflect
        428: fly_emote_eat_no_sheathe
        429: fly_land
        430: fly_submerge
        431: fly_submerged
        432: fly_cannibalize
        433: fly_arrow_birth
        434: fly_group_arrow_birth
        435: fly_corpse_arrow_birth
        436: fly_guide_arrow_birth
        437: fly_emote_talk_no_sheathe
        438: fly_emote_point_no_sheathe
        439: fly_emote_salute_no_sheathe
        440: fly_emote_dance_special
        441: fly_mutilate
        442: fly_custom_spell01
        443: fly_custom_spell02
        444: fly_custom_spell03
        445: fly_custom_spell04
        446: fly_custom_spell05
        447: fly_custom_spell06
        448: fly_custom_spell07
        449: fly_custom_spell08
        450: fly_custom_spell09
        451: fly_custom_spell10
        452: fly_stealth_run
        453: fly_emerge
        454: fly_cower
        455: fly_grab  # Fly (Critcal)
        456: fly_grab_closed
        457: fly_grab_thrown  # Fly (Attack with Hands)
        458: to_fly
        459: to_hover
        460: to_ground
        461: fly_to_fly
        462: fly_to_hover
        463: fly_to_ground
        464: settle
        465: fly_settle
        466: death_start
        467: death_loop
        468: death_end
        469: fly_death_start
        470: fly_death_loop  # Fly (Fall)
        471: fly_death_end  # Fly (Land Dead)
        472: death_end_hold
        473: fly_death_end_hold
        474: strangulate
        475: fly_strangulate
        476: ready_joust  # Joust (Idle)
        477: load_joust  # Joust (Lower Lance)
        478: hold_joust  # Joust (Lance Lowered)
        479: fly_ready_joust
        480: fly_load_joust
        481: fly_hold_joust
        482: attack_joust
        483: fly_attack_joust
        484: reclined_mount  # Mount (Car/Mech)
        485: fly_reclined_mount
        486: to_altered  # Worgen Transformation
        487: from_altered
        488: fly_to_altered
        489: fly_from_altered
        490: in_stocks
        491: fly_in_stocks
        492: vehicle_grab
        493: vehicle_throw
        494: fly_vehicle_grab
        495: fly_vehicle_throw
        496: to_altered_post_swap
        497: from_altered_post_swap
        498: fly_to_altered_post_swap
        499: fly_from_altered_post_swap
        500: reclined_mount_passenger  # Sit (Carriage Backseat)
        501: fly_reclined_mount_passenger
        502: carry_2h  # Carrying (human only)
        503: carried_2h  # Carried (human only)
        504: fly_carry_2h
        505: fly_carried_2h
        506: emote_sniff
        507: emote_fly_sniff
        508: attack_fist_1h  # Attack (Unarmed Right)
        509: fly_attack_fist_1h
        510: attack_fist_1h_off  # Attack (Unarmed Left)
        511: fly_attack_fist_1h_off  # Block (Unarmed)
        512: parry_fist_1h
        513: fly_parry_fist_1h
        514: ready_fist_1h
        515: fly_ready_fist_1h
        516: special_fist_1h  # Critcal (Unarmed)
        517: fly_special_fist_1h
        518: emote_read_start  # Map (Open)
        519: fly_emote_read_start
        520: emote_read_loop  # Map
        521: fly_emote_read_loop
        522: emote_read_end  # Map (Close)
        523: fly_emote_read_end
        524: swim_run
        525: fly_swim_run
        526: swim_walk
        527: fly_swim_walk
        528: swim_walk_backwards
        529: fly_swim_walk_backwards
        530: swim_sprint
        531: fly_swim_sprint
        532: mount_swim_idle
        533: fly_mount_swim_idle
        534: mount_swim_backwards
        535: fly_mount_swim_backwards
        536: mount_swim_left
        537: fly_mount_swim_left
        538: mount_swim_right
        539: fly_mount_swim_right
        540: mount_swim_run
        541: fly_mount_swim_run
        542: mount_swim_sprint
        543: fly_mount_swim_sprint
        544: mount_swim_walk
        545: fly_mount_swim_walk
        546: mount_swim_walk_backwards
        547: fly_mount_swim_walk_backwards
        548: mount_flight_idle
        549: fly_mount_flight_idle
        550: mount_flight_backwards
        551: fly_mount_flight_backwards
        552: mount_flight_left
        553: fly_mount_flight_left
        554: mount_flight_right
        555: fly_mount_flight_right
        556: mount_flight_run
        557: fly_mount_flight_run
        558: mount_flight_sprint
        559: fly_mount_flight_sprint
        560: mount_flight_walk
        561: fly_mount_flight_walk
        562: mount_flight_walk_backwards
        563: fly_mount_flight_walk_backwards
        564: mount_flight_start
        565: fly_mount_flight_start
        566: mount_swim_start
        567: fly_mount_swim_start
        568: mount_swim_land
        569: fly_mount_swim_land
        570: mount_swim_land_run
        571: fly_mount_swim_land_run
        572: mount_flight_land
        573: fly_mount_flight_land
        574: mount_flight_land_run
        575: fly_mount_flight_land_run
        576: ready_blow_dart
        577: fly_ready_blow_dart
        578: load_blow_dart
        579: fly_load_blow_dart
        580: hold_blow_dart
        581: fly_hold_blow_dart
        582: attack_blow_dart
        583: fly_attack_blow_dart
        584: carriage_mount  # Carriage (Sit)
        585: fly_carriage_mount
        586: carriage_passenger_mount
        587: fly_carriage_passenger_mount
        588: carriage_mount_attack  # Carriage (Reins)
        589: fly_carriage_mount_attack
        590: bar_tend_stand  # Bartender (Idle)
        591: fly_bar_tend_stand
        592: bar_server_walk  # Waiter (Walk)
        593: fly_bar_server_walk
        594: bar_server_run
        595: fly_bar_server_run
        596: bar_server_shuffle_left
        597: fly_bar_server_shuffle_left
        598: bar_server_shuffle_right
        599: fly_bar_server_shuffle_right
        600: bar_tend_emote_talk  # Bartender (Talk)
        601: fly_bar_tend_emote_talk
        602: bar_tend_emote_point  # Bartender (Point)
        603: fly_bar_tend_emote_point
        604: bar_server_stand  # Waiter (Idle)
        605: fly_bar_server_stand
        606: bar_sweep_walk
        607: fly_bar_sweep_walk
        608: bar_sweep_run
        609: fly_bar_sweep_run
        610: bar_sweep_shuffle_left
        611: fly_bar_sweep_shuffle_left
        612: bar_sweep_shuffle_right
        613: fly_bar_sweep_shuffle_right
        614: bar_sweep_emote_talk
        615: fly_bar_sweep_emote_talk
        616: bar_patron_sit_emote_point
        617: fly_bar_patron_sit_emote_point
        618: mount_self_idle  # Running Wild (Idle) (human and worgen only)
        619: fly_mount_self_idle
        620: mount_self_walk
        621: fly_mount_self_walk
        622: mount_self_run
        623: fly_mount_self_run
        624: mount_self_sprint
        625: fly_mount_self_sprint
        626: mount_self_run_left
        627: fly_mount_self_run_left
        628: mount_self_run_right
        629: fly_mount_self_run_right
        630: mount_self_shuffle_left
        631: fly_mount_self_shuffle_left
        632: mount_self_shuffle_right
        633: fly_mount_self_shuffle_right
        634: mount_self_walk_backwards
        635: fly_mount_self_walk_backwards
        636: mount_self_special
        637: fly_mount_self_special
        638: mount_self_jump
        639: fly_mount_self_jump
        640: mount_self_jump_start
        641: fly_mount_self_jump_start
        642: mount_self_jump_end
        643: fly_mount_self_jump_end
        644: mount_self_jump_land_run
        645: fly_mount_self_jump_land_run
        646: mount_self_start  # Running Wild (Start) (human and worgen only)
        647: fly_mount_self_start
        648: mount_self_fall
        649: fly_mount_self_fall
        650: stormstrike  # Great Attack (Stab)
        651: fly_stormstrike
        652: ready_joust_no_sheathe
        653: fly_ready_joust_no_sheathe
        654: slam  # Great Attack 1 (1H)
        655: fly_slam
        656: death_strike  # Great Attack 1 (2H)
        657: fly_death_strike
        658: swim_attack_unarmed
        659: fly_swim_attack_unarmed
        660: spinning_kick
        661: fly_spinning_kick
        662: round_house_kick  # Kick (Monk)
        663: fly_round_house_kick
        664: roll_start
        665: fly_roll_start
        666: roll
        667: fly_roll
        668: roll_end
        669: fly_roll_end
        670: palm_strike  # Attack 1 (Windwalker)
        671: fly_palm_strike
        672: monk_offense_attack_unarmed  # Attack 2 (Windwalker)
        673: fly_monk_offense_attack_unarmed
        674: monk_offense_attack_unarmed_off  # Attack 3 (Windwalker)
        675: fly_monk_offense_attack_unarmed_off
        676: monk_offense_parry_unarmed  # Dodge (Windwalker)
        677: fly_monk_offense_parry_unarmed
        678: monk_offense_ready_unarmed  # Ready (Windwalker)
        679: fly_monk_offense_ready_unarmed
        680: monk_offense_special_unarmed  # Chi Burst
        681: fly_monk_offense_special_unarmed
        682: monk_defense_attack_unarmed  # Attack 1 (Brewmaster)
        683: fly_monk_defense_attack_unarmed
        684: monk_defense_attack_unarmed_off  # Attack 2 (Brewmaster)
        685: fly_monk_defense_attack_unarmed_off
        686: monk_defense_parry_unarmed  # Dodge (Brewmaster)
        687: fly_monk_defense_parry_unarmed
        688: monk_defense_ready_unarmed  # Ready (Brewmaster)
        689: fly_monk_defense_ready_unarmed
        690: monk_defense_special_unarmed  # Attack 3 (Brewmaster)
        691: fly_monk_defense_special_unarmed
        692: monk_heal_attack_unarmed  # Attack 1 (Mistweaver)
        693: fly_monk_heal_attack_unarmed
        694: monk_heal_attack_unarmed_off
        695: fly_monk_heal_attack_unarmed_off
        696: monk_heal_parry_unarmed  # Attack 2 (Mistweaver)
        697: fly_monk_heal_parry_unarmed
        698: monk_heal_ready_unarmed  # Ready (Mistweaver)
        699: fly_monk_heal_ready_unarmed
        700: monk_heal_special_unarmed
        701: fly_monk_heal_special_unarmed
        702: flying_kick  # Flying Serpent Kick
        703: fly_flying_kick
        704: flying_kick_start  # Flying Serpent Kick (Begin)
        705: fly_flying_kick_start
        706: flying_kick_end  # Flying Serpent Kick (Land)
        707: fly_flying_kick_end
        708: crane_start
        709: fly_crane_start
        710: crane_loop
        711: fly_crane_loop
        712: crane_end
        713: fly_crane_end
        714: despawned
        715: fly_despawned
        716: thousand_fists  # Fists of Fury
        717: fly_thousand_fists
        718: monk_heal_ready_spell_directed  # Ready (Mistweaver)
        719: fly_monk_heal_ready_spell_directed
        720: monk_heal_ready_spell_omni  # Ready (Mistweaver)
        721: fly_monk_heal_ready_spell_omni
        722: monk_heal_spell_cast_directed  # Cast 1 (Mistweaver)
        723: fly_monk_heal_spell_cast_directed
        724: monk_heal_spell_cast_omni  # Cast 2 (Mistweaver)
        725: fly_monk_heal_spell_cast_omni
        726: monk_heal_channel_cast_directed  # Channel 1 (Mistweaver)
        727: fly_monk_heal_channel_cast_directed
        728: monk_heal_channel_cast_omni  # Channel 2 (Mistweaver)
        729: fly_monk_heal_channel_cast_omni
        730: torpedo  # Chi Torpedo
        731: fly_torpedo
        732: meditate
        733: fly_meditate
        734: breath_of_fire
        735: fly_breath_of_fire
        736: rising_sun_kick  # Kick Flip
        737: fly_rising_sun_kick
        738: ground_kick
        739: fly_ground_kick
        740: kick_back
        741: fly_kick_back
        742: pet_battle_stand
        743: fly_pet_battle_stand
        744: pet_battle_death
        745: fly_pet_battle_death
        746: pet_battle_run
        747: fly_pet_battle_run
        748: pet_battle_wound
        749: fly_pet_battle_wound
        750: pet_battle_attack
        751: fly_pet_battle_attack
        752: pet_battle_ready_spell
        753: fly_pet_battle_ready_spell
        754: pet_battle_spell_cast
        755: fly_pet_battle_spell_cast
        756: pet_battle_custom0
        757: fly_pet_battle_custom0
        758: pet_battle_custom1
        759: fly_pet_battle_custom1
        760: pet_battle_custom2
        761: fly_pet_battle_custom2
        762: pet_battle_custom3
        763: fly_pet_battle_custom3
        764: pet_battle_victory
        765: fly_pet_battle_victory
        766: pet_battle_loss
        767: fly_pet_battle_loss
        768: pet_battle_stun
        769: fly_pet_battle_stun
        770: pet_battle_dead
        771: fly_pet_battle_dead
        772: pet_battle_freeze
        773: fly_pet_battle_freeze
        774: monk_offense_attack_weapon  # Staff Attack (Monk)
        775: fly_monk_offense_attack_weapon
        776: bar_tend_emote_wave  # Waiter (Talk)
        777: fly_bar_tend_emote_wave
        778: bar_server_emote_talk
        779: fly_bar_server_emote_talk
        780: bar_server_emote_wave
        781: fly_bar_server_emote_wave
        782: bar_server_pour_drinks
        783: fly_bar_server_pour_drinks
        784: bar_server_pickup
        785: fly_bar_server_pickup
        786: bar_server_put_down
        787: fly_bar_server_put_down
        788: bar_sweep_stand
        789: fly_bar_sweep_stand
        790: bar_patron_sit
        791: fly_bar_patron_sit
        792: bar_patron_sit_emote_talk
        793: fly_bar_patron_sit_emote_talk
        794: bar_patron_stand
        795: fly_bar_patron_stand
        796: bar_patron_stand_emote_talk
        797: fly_bar_patron_stand_emote_talk
        798: bar_patron_stand_emote_point
        799: fly_bar_patron_stand_emote_point
        800: carrion_swarm
        801: fly_carrion_swarm
        802: wheel_loop
        803: fly_wheel_loop
        804: stand_character_create  # Idle
        805: fly_stand_character_create
        806: mount_chopper  # Mount (Motorcycle)
        807: fly_mount_chopper
        808: face_pose  # G-Pose
        809: fly_face_pose
        810: combat_ablity_2h_big01  # Great Attack 2 (2H)
        811: fly_combat_ablity_2h_big01
        812: combat_ablity_2h_01  # Great Attack 3 (2H)
        813: fly_combat_ablity_2h_01
        814: combat_whirlwind
        815: fly_combat_whirlwind
        816: combat_charge_loop
        817: fly_combat_charge_loop
        818: combat_ablity_1h_01  # Great Attack 2 (1H)
        819: fly_combat_ablity_1h_01
        820: combat_charge_end
        821: fly_combat_charge_end
        822: combat_ablity_1h_02  # Great Attack 3 (1H)
        823: fly_combat_ablity_1h_02
        824: combat_ablity_1h_big01  # Great Attack 4 (1H)
        825: fly_combat_ablity_1h_big01
        826: combat_ablity_2h_02  # Wake of Ashes
        827: fly_combat_ablity_2h_02
        828: sha_spell_precast_both
        829: fly_sha_spell_precast_both
        830: sha_spell_cast_both_front
        831: fly_sha_spell_cast_both_front
        832: sha_spell_cast_left_front
        833: fly_sha_spell_cast_left_front
        834: sha_spell_cast_right_front
        835: fly_sha_spell_cast_right_front
        836: ready_crossbow
        837: fly_ready_crossbow
        838: load_crossbow
        839: fly_load_crossbow
        840: attack_crossbow
        841: fly_attack_crossbow
        842: hold_crossbow  # Aim (Gun/Crossbow)
        843: fly_hold_crossbow
        844: combat_ablity_2h_l01
        845: fly_combat_ablity_2h_l01
        846: combat_ablity_2h_l02
        847: fly_combat_ablity_2h_l02
        848: combat_ablity_2h_lbig01
        849: fly_combat_ablity_2h_lbig01
        850: combat_unarmed01
        851: fly_combat_unarmed01
        852: combat_stomp_left
        853: fly_combat_stomp_left
        854: combat_stomp_right
        855: fly_combat_stomp_right
        856: combat_leap_loop
        857: fly_combat_leap_loop
        858: combat_leap_end
        859: fly_combat_leap_end
        860: sha_ready_spell_cast
        861: fly_sha_ready_spell_cast
        862: sha_spell_precast_both_channel  # Shaman (Channel)
        863: fly_sha_spell_precast_both_channel
        864: sha_spell_cast_both_up
        865: fly_sha_spell_cast_both_up
        866: sha_spell_cast_both_up_channel
        867: fly_sha_spell_cast_both_up_channel
        868: sha_spell_cast_both_front_channel
        869: fly_sha_spell_cast_both_front_channel
        870: sha_spell_cast_left_front_channel
        871: fly_sha_spell_cast_left_front_channel
        872: sha_spell_cast_right_front_channel
        873: fly_sha_spell_cast_right_front_channel
        874: pri_ready_spell_cast  # Priest (Hover)
        875: fly_pri_ready_spell_cast
        876: pri_spell_precast_both
        877: fly_pri_spell_precast_both
        878: pri_spell_precast_both_channel
        879: fly_pri_spell_precast_both_channel
        880: pri_spell_cast_both_up
        881: fly_pri_spell_cast_both_up
        882: pri_spell_cast_both_front
        883: fly_pri_spell_cast_both_front
        884: pri_spell_cast_left_front
        885: fly_pri_spell_cast_left_front
        886: pri_spell_cast_right_front
        887: fly_pri_spell_cast_right_front
        888: pri_spell_cast_both_up_channel
        889: fly_pri_spell_cast_both_up_channel
        890: pri_spell_cast_both_front_channel
        891: fly_pri_spell_cast_both_front_channel
        892: pri_spell_cast_left_front_channel
        893: fly_pri_spell_cast_left_front_channel
        894: pri_spell_cast_right_front_channel
        895: fly_pri_spell_cast_right_front_channel
        896: mag_ready_spell_cast
        897: fly_mag_ready_spell_cast
        898: mag_spell_precast_both
        899: fly_mag_spell_precast_both
        900: mag_spell_precast_both_channel
        901: fly_mag_spell_precast_both_channel
        902: mag_spell_cast_both_up
        903: fly_mag_spell_cast_both_up
        904: mag_spell_cast_both_front
        905: fly_mag_spell_cast_both_front
        906: mag_spell_cast_left_front
        907: fly_mag_spell_cast_left_front
        908: mag_spell_cast_right_front
        909: fly_mag_spell_cast_right_front
        910: mag_spell_cast_both_up_channel
        911: fly_mag_spell_cast_both_up_channel
        912: mag_spell_cast_both_front_channel
        913: fly_mag_spell_cast_both_front_channel
        914: mag_spell_cast_left_front_channel
        915: fly_mag_spell_cast_left_front_channel
        916: mag_spell_cast_right_front_channel
        917: fly_mag_spell_cast_right_front_channel
        918: loc_ready_spell_cast
        919: fly_loc_ready_spell_cast
        920: loc_spell_precast_both  # Warlock (Ready)
        921: fly_loc_spell_precast_both
        922: loc_spell_precast_both_channel
        923: fly_loc_spell_precast_both_channel
        924: loc_spell_cast_both_up
        925: fly_loc_spell_cast_both_up
        926: loc_spell_cast_both_front
        927: fly_loc_spell_cast_both_front
        928: loc_spell_cast_left_front
        929: fly_loc_spell_cast_left_front
        930: loc_spell_cast_right_front
        931: fly_loc_spell_cast_right_front
        932: loc_spell_cast_both_up_channel
        933: fly_loc_spell_cast_both_up_channel
        934: loc_spell_cast_both_front_channel
        935: fly_loc_spell_cast_both_front_channel
        936: loc_spell_cast_left_front_channel
        937: fly_loc_spell_cast_left_front_channel
        938: loc_spell_cast_right_front_channel
        939: fly_loc_spell_cast_right_front_channel
        940: dru_ready_spell_cast
        941: fly_dru_ready_spell_cast
        942: dru_spell_precast_both
        943: fly_dru_spell_precast_both
        944: dru_spell_precast_both_channel
        945: fly_dru_spell_precast_both_channel
        946: dru_spell_cast_both_up
        947: fly_dru_spell_cast_both_up
        948: dru_spell_cast_both_front
        949: fly_dru_spell_cast_both_front
        950: dru_spell_cast_left_front
        951: fly_dru_spell_cast_left_front
        952: dru_spell_cast_right_front
        953: fly_dru_spell_cast_right_front
        954: dru_spell_cast_both_up_channel
        955: fly_dru_spell_cast_both_up_channel
        956: dru_spell_cast_both_front_channel
        957: fly_dru_spell_cast_both_front_channel
        958: dru_spell_cast_left_front_channel
        959: fly_dru_spell_cast_left_front_channel
        960: dru_spell_cast_right_front_channel
        961: fly_dru_spell_cast_right_front_channel
        962: art_main_loop  # Hold Artifact (Main Hand)
        963: fly_art_main_loop
        964: art_dual_loop  # Hold Artifact (Dual)
        965: fly_art_dual_loop
        966: art_fists_loop  # Hold Artifact (Fists)
        967: fly_art_fists_loop
        968: art_bow_loop  # Hold Artifact (Bow)
        969: fly_art_bow_loop
        970: combat_ablity_1h_01off  # Great Attack 5 (1H)
        971: fly_combat_ablity_1h_01off
        972: combat_ablity_1h_02off  # Great Attack 6 (1H)
        973: fly_combat_ablity_1h_02off
        974: combat_furious_strike01
        975: fly_combat_furious_strike01
        976: combat_furious_strike02
        977: fly_combat_furious_strike02
        978: combat_furious_strikes
        979: fly_combat_furious_strikes
        980: combat_ready_spell_cast
        981: fly_combat_ready_spell_cast
        982: combat_shield_throw
        983: fly_combat_shield_throw
        984: pal_spell_cast_1h_up
        985: fly_pal_spell_cast_1h_up
        986: combat_ready_post_spell_cast
        987: fly_combat_ready_post_spell_cast
        988: pri_ready_post_spell_cast
        989: fly_pri_ready_post_spell_cast
        990: dh_combat_run
        991: fly_dh_combat_run
        992: combat_shield_bash
        993: fly_combat_shield_bash
        994: combat_throw  # Rogue (Throw)
        995: fly_combat_throw
        996: combat_ablity_1h_pierce  # Rogue (Stab Right)
        997: fly_combat_ablity_1h_pierce
        998: combat_ablity_1h_off_pierce  # Rogue (Stab Left)
        999: fly_combat_ablity_1h_off_pierce
        1000: combat_mutilate  # Rogue (Stab Both)
        1001: fly_combat_mutilate
        1002: combat_blade_storm  # Rogue (Fan of Blades)
        1003: fly_combat_blade_storm
        1004: combat_finishing_move  # Heroic Leap (End)
        1005: fly_combat_finishing_move
        1006: combat_leap_start  # Heroic Leap (Begin)
        1007: fly_combat_leap_start
        1008: glv_throw_main  # Demon Hunter (Glaive Right)
        1009: fly_glv_throw_main
        1010: glv_thrown_off  # Demon Hunter (Glaive Left)
        1011: fly_glv_thrown_off
        1012: dh_combat_sprint  # Demon Hunter (Ready Run)
        1013: fly_dh_combat_sprint
        1014: combat_ability_glv01  # Demon Hunter (Throw Glaive Right)
        1015: fly_combat_ability_glv01
        1016: combat_ability_glv02
        1017: fly_combat_ability_glv02
        1018: combat_ability_glv_off01  # Demon Hunter (Throw Glaive Left)
        1019: fly_combat_ability_glv_off01
        1020: combat_ability_glv_off02
        1021: fly_combat_ability_glv_off02
        1022: combat_ability_glv_big01  # Demon Hunter (Jump Slash Right 1)
        1023: fly_combat_ability_glv_big01
        1024: combat_ability_glv_big02  # Demon Hunter (Jump Slash Right 2)
        1025: fly_combat_ability_glv_big02
        1026: ready_glv  # Demon Hunter (Ready)
        1027: fly_ready_glv
        1028: combat_ability_glv_big03  # Demon Hunter (Jump and Pound)
        1029: fly_combat_ability_glv_big03
        1030: double_jump_start  # Demon Hunter (Double Jump)
        1031: fly_double_jump_start
        1032: double_jump  # Demon Hunter (Fall)
        1033: fly_double_jump
        1034: combat_eviscerate  # Great Attack 1 (Dual)
        1035: fly_combat_eviscerate
        1036: double_jump_land_run
        1037: fly_double_jump_land_run
        1038: back_flip_start  # Demon Hunter (Eye Beam Begin)
        1039: fly_back_flip_start
        1040: back_flip_loop  # Demon Hunter (Eye Beam)
        1041: fly_back_flip_loop
        1042: fel_rush_loop  # Demon Hunter (Ready Run)
        1043: fly_fel_rush_loop
        1044: fel_rush_end  # Demon Hunter (Plant Sigil)
        1045: fly_fel_rush_end
        1046: dh_to_altered_start
        1047: fly_dh_to_altered_start
        1048: dh_to_altered_end
        1049: fly_dh_to_altered_end
        1050: dh_glide  # Demon Hunter (Glide)
        1051: fly_dh_glide
        1052: fan_of_knives
        1053: fly_fan_of_knives
        1054: single_jump_start  # Demon Hunter (Jump Begin)
        1055: fly_single_jump_start
        1056: dh_blade_dance1  # Demon Hunter (Blade Dance 1)
        1057: fly_dh_blade_dance1
        1058: dh_blade_dance2  # Demon Hunter (Blade Dance 2)
        1059: fly_dh_blade_dance2
        1060: dh_blade_dance3  # Demon Hunter (Blade Dance 3)
        1061: fly_dh_blade_dance3
        1062: dh_meteor_strike  # Demon Hunter (Blade Dance 4)
        1063: fly_dh_meteor_strike
        1064: combat_execute  # Great Attack 2 (Dual)
        1065: fly_combat_execute
        1066: art_loop
        1067: fly_art_loop
        1068: parry_glv
        1069: fly_parry_glv
        1070: combat_unarmed02
        1071: fly_combat_unarmed02
        1072: combat_pistol_shot
        1073: fly_combat_pistol_shot
        1074: combat_pistol_shot_off  # Rogue (Pistol Shot)
        1075: fly_combat_pistol_shot_off
        1076: monk_2h_l_idle  # Hold Staff on Shoulder (Fu Zan)
        1077: fly_monk_2h_l_idle
        1078: art_shield_loop  # Hold Artifact (Shield)
        1079: fly_art_shield_loop
        1080: combat_ablity_2h_03  # Spin Attack 1
        1081: fly_combat_ablity_2h_03
        1082: combat_stomp
        1083: fly_combat_stomp
        1084: combat_roar
        1085: fly_combat_roar
        1086: pal_ready_spell_cast
        1087: fly_pal_ready_spell_cast
        1088: pal_spell_precast_right  # Paladin (Channel Book)
        1089: fly_pal_spell_precast_right
        1090: pal_spell_precast_right_channel
        1091: fly_pal_spell_precast_right_channel
        1092: pal_spell_cast_right_front
        1093: fly_pal_spell_cast_right_front  # Paladin (Cast Book)
        1094: sha_spell_cast_both_out
        1095: fly_sha_spell_cast_both_out
        1096: attack_weapon
        1097: fly_attack_weapon
        1098: ready_weapon
        1099: fly_ready_weapon
        1100: attack_weapon_off
        1101: fly_attack_weapon_off
        1102: special_dual  # Spin Attack 2
        1103: fly_special_dual
        1104: dk_cast_1h_front  # Death Knight (Cast)
        1105: fly_dk_cast_1h_front
        1106: cast_strong_right
        1107: fly_cast_strong_right
        1108: cast_strong_left
        1109: fly_cast_strong_left
        1110: cast_curse_right
        1111: fly_cast_curse_right
        1112: cast_curse_left
        1113: fly_cast_curse_left
        1114: cast_sweep_right
        1115: fly_cast_sweep_right
        1116: cast_sweep_left
        1117: fly_cast_sweep_left
        1118: cast_strong_up_left
        1119: fly_cast_strong_up_left
        1120: cast_twist_up_both
        1121: fly_cast_twist_up_both
        1122: cast_out_strong
        1123: fly_cast_out_strong
        1124: drum_loop
        1125: fly_drum_loop
        1126: parry_weapon
        1127: fly_parry_weapon
        1128: ready_fl  # Ready (1H)
        1129: fly_ready_fl
        1130: attack_fl  # Attack Up (1H)
        1131: fly_attack_fl
        1132: attack_floff  # Attack Forward (1H)
        1133: fly_attack_floff
        1134: parry_fl  # Block (Shield)
        1135: fly_parry_fl
        1136: special_fl  # Spin Attack 1
        1137: fly_special_fl
        1138: pri_hover_forward  # Priest (Hover)
        1139: fly_pri_hover_forward
        1140: pri_hover_backward  # Priest (Hover Backwards)
        1141: fly_pri_hover_backward
        1142: pri_hover_right  # Priest (Hover Right)
        1143: fly_pri_hover_right
        1144: pri_hover_left  # Priest (Hover Left)
        1145: fly_pri_hover_left
        1146: run_backwards
        1147: fly_run_backwards
        1148: cast_strong_up_right
        1149: fly_cast_strong_up_right
        1150: wa_walk
        1151: fly_wa_walk
        1152: wa_run
        1153: fly_wa_run
        1154: wa_drunk_stand
        1155: fly_wa_drunk_stand
        1156: wa_drunk_shuffle_left
        1157: fly_wa_drunk_shuffle_left
        1158: wa_drunk_shuffle_right
        1159: fly_wa_drunk_shuffle_right
        1160: wa_drunk_walk
        1161: fly_wa_drunk_walk
        1162: wa_drunk_walk_backwards
        1163: fly_wa_drunk_walk_backwards
        1164: wa_drunk_wound
        1165: fly_wa_drunk_wound
        1166: wa_drunk_talk
        1167: fly_wa_drunk_talk
        1168: wa_trance01  # Chant Standing 1 (troll only)
        1169: fly_wa_trance01
        1170: wa_trance02
        1171: fly_wa_trance02
        1172: wa_chant01  # Chant Kneeling (troll only)
        1173: fly_wa_chant01
        1174: wa_chant02  # Chant Bowing (troll only)
        1175: fly_wa_chant02
        1176: wa_chant03  # Chant (troll only)
        1177: fly_wa_chant03
        1178: wa_hang01  # Hanging by Arms
        1179: fly_wa_hang01
        1180: wa_hang02  # Hanging by Arms and Screaming (troll only)
        1181: fly_wa_hang02
        1182: wa_summon01#  # Chant Standing 2 (troll only)
        1183: fly_wa_summon01
        1184: wa_summon02
        1185: fly_wa_summon02
        1186: wa_beggar_talk
        1187: fly_wa_beggar_talk
        1188: wa_beggar_stand
        1189: fly_wa_beggar_stand
        1190: wa_beggar_point
        1191: fly_wa_beggar_point
        1192: wa_beggar_beg
        1193: fly_wa_beggar_beg
        1194: wa_sit01  # Sit Special 1
        1195: fly_wa_sit01
        1196: wa_sit02  # Sit Special 2
        1197: fly_wa_sit02
        1198: wa_sit03  # Sit Special 3
        1199: fly_wa_sit03
        1200: wa_crier_stand01  # Crier (Idle)
        1201: fly_wa_crier_stand01
        1202: wa_crier_stand02  # Crier (Ring Bell)
        1203: fly_wa_crier_stand02
        1204: wa_crier_stand03
        1205: fly_wa_crier_stand03
        1206: wa_crier_talk  # Crier (Read)
        1207: fly_wa_crier_talk
        1208: wa_crate_hold  # Hold (Front)
        1209: fly_wa_crate_hold
        1210: wa_barrel_hold  # Hold (Shoulder)
        1211: fly_wa_barrel_hold
        1212: wa_sack_hold  # Rest on Shoulder
        1213: fly_wa_sack_hold
        1214: wa_wheel_barrow_stand  # Wheelbarrow (Idle)
        1215: fly_wa_wheel_barrow_stand
        1216: wa_wheel_barrow_walk  # Wheelbarrow (Walk)
        1217: fly_wa_wheel_barrow_walk
        1218: wa_wheel_barrow_run
        1219: fly_wa_wheel_barrow_run
        1220: wa_hammer_loop  # Hammer on Wall
        1221: fly_wa_hammer_loop
        1222: wa_crank_loop  # Row (Both)
        1223: fly_wa_crank_loop
        1224: wa_pour_start  # Pour (Begin)
        1225: fly_wa_pour_start
        1226: wa_pour_loop
        1227: fly_wa_pour_loop
        1228: wa_pour_end
        1229: fly_wa_pour_end
        1230: wa_emote_pour
        1231: fly_wa_emote_pour
        1232: wa_rowing_stand_right
        1233: fly_wa_rowing_stand_right
        1234: wa_rowing_stand_left
        1235: fly_wa_rowing_stand_left
        1236: wa_rowing_right
        1237: fly_wa_rowing_right
        1238: wa_rowing_left
        1239: fly_wa_rowing_left
        1240: wa_guard_stand01
        1241: fly_wa_guard_stand01
        1242: wa_guard_stand02
        1243: fly_wa_guard_stand02
        1244: wa_guard_stand03
        1245: fly_wa_guard_stand03
        1246: wa_guard_stand04
        1247: fly_wa_guard_stand04
        1248: wa_freezing01  # Carve
        1249: fly_wa_freezing01
        1250: wa_freezing02  # Stir
        1251: fly_wa_freezing02
        1252: wa_vendor_stand01
        1253: fly_wa_vendor_stand01
        1254: wa_vendor_stand02
        1255: fly_wa_vendor_stand02
        1256: wa_vendor_stand03
        1257: fly_wa_vendor_stand03
        1258: wa_vendor_talk
        1259: fly_wa_vendor_talk
        1260: wa_lean01
        1261: fly_wa_lean01
        1262: wa_lean02  # Scrub
        1263: fly_wa_lean02
        1264: wa_lean03
        1265: fly_wa_lean03
        1266: wa_lean_talk
        1267: fly_wa_lean_talk
        1268: wa_boat_wheel
        1269: fly_wa_boat_wheel
        1270: wa_smith_loop
        1271: fly_wa_smith_loop
        1272: wa_scrubbing
        1273: fly_wa_scrubbing
        1274: wa_weapon_sharpen
        1275: fly_wa_weapon_sharpen
        1276: wa_stirring
        1277: fly_wa_stirring
        1278: wa_perch01
        1279: fly_wa_perch01
        1280: wa_perch02
        1281: fly_wa_perch02
        1282: hold_weapon
        1283: fly_hold_weapon
        1284: wa_barrel_walk  # Hold (Shoulder Walk)
        1285: fly_wa_barrel_walk
        1286: wa_pour_hold  # Hold (Jug)
        1287: fly_wa_pour_hold
        1288: cast_strong
        1289: fly_cast_strong
        1290: cast_curse
        1291: fly_cast_curse
        1292: cast_sweep
        1293: fly_cast_sweep
        1294: cast_strong_up
        1295: fly_cast_strong_up
        1296: wa_boat_wheel_stand
        1297: fly_wa_boat_wheel_stand
        1298: wa_smith_stand
        1299: fly_wa_smith_stand
        1300: wa_crank_stand  # Row (Both Idle)
        1301: fly_wa_crank_stand

        # starting with 7.3.0.24781
        1302: wa_pour_walk
        1303: fly_wa_pour_walk
        1304: falconeer_start
        1305: fly_falconeer_start
        1306: falconeer_loop
        1307: fly_falconeer_loop
        1308: falconeer_end
        1309: fly_falconeer_end

        # starting with 7.3.2.25079
        1310: wa_drunk_drink
        1311: fly_wa_drunk_drink
        1312: wa_stand_eat
        1313: fly_wa_stand_eat
        1314: wa_stand_drink
        1315: fly_wa_stand_drink
        1316: wa_bound01
        1317: fly_wa_bound01
        1318: wa_bound02
        1319: fly_wa_bound02
        1320: combat_ablity_1h_03off
        1321: fly_combat_ablity_1h_03off
        1322: combat_ability_dual_wield01
        1323: fly_combat_ability_dual_wield01

        # Starting with 8.0.1.25902
        1324: wa_cradle01  # Hold (Sack or Baby)
        1325: fly_wa_cradle01

        # Starting with 8.0.1.25976
        1326: loc_summon  # Warlock (Summon)
        1327: fly_loc_summon
        1328: load_weapon
        1329: fly_load_weapon

        # Starting with 8.0.1.26131
        1330: art_off_loop  # Hold Artifact (Offhand) (Used for Heart of Azeroth)
        1331: fly_art_off_loop

        # Starting with 8.0.1.26476
        1332: wa_dead01
        1333: fly_wa_dead01
        1334: wa_dead02
        1335: fly_wa_dead02
        1336: wa_dead03
        1337: fly_wa_dead03
        1338: wa_dead04
        1339: fly_wa_dead04
        1340: wa_dead05
        1341: fly_wa_dead05
        1342: wa_dead06
        1343: fly_wa_dead06
        1344: wa_dead07
        1345: fly_wa_dead07

        # Starting with 8.1.0.27826
        1346: giant_run
        1347: fly_giant_run
        1348: bar_tend_emote_cheer
        1349: fly_bar_tend_emote_cheer
        1350: bar_tend_emote_talk_question
        1351: fly_bar_tend_emote_talk_question
        1352: bar_tend_emote_talk_exclamation
        1353: fly_bar_tend_emote_talk_exclamation
        1354: bar_tend_walk
        1355: fly_bar_tend_walk
        1356: bartend_shuffle_left
        1357: fly_bartend_shuffle_left
        1358: bar_tend_shuffle_right
        1359: fly_bar_tend_shuffle_right
        1360: bar_tend_custom_spell01
        1361: fly_bar_tend_custom_spell01
        1362: bar_tend_custom_spell02
        1363: fly_bar_tend_custom_spell02
        1364: bar_tend_custom_spell03
        1365: fly_bar_tend_custom_spell03
        1366: bar_server_emote_cheer
        1367: fly_bar_server_emote_cheer
        1368: bar_server_emote_talk_question
        1369: fly_bar_server_emote_talk_question
        1370: bar_server_emote_talk_exclamation
        1371: fly_bar_server_emote_talk_exclamation
        1372: bar_server_custom_spell01
        1373: fly_bar_server_custom_spell01
        1374: bar_server_custom_spell02
        1375: fly_bar_server_custom_spell02
        1376: bar_server_custom_spell03
        1377: fly_bar_server_custom_spell03
        1378: bar_patron_emote_drink
        1379: fly_bar_patron_emote_drink
        1380: bar_patron_emote_cheer
        1381: fly_bar_patron_emote_cheer
        1382: bar_patron_custom_spell01
        1383: fly_bar_patron_custom_spell01
        1384: bar_patron_custom_spell02
        1385: fly_bar_patron_custom_spell02
        1386: bar_patron_custom_spell03
        1387: fly_bar_patron_custom_spell03
        1388: hold_dart  # Throw Weapon (Ready)
        1389: fly_hold_dart
        1390: ready_dart
        1391: fly_ready_dart
        1392: attack_dart  # Throw Weapon
        1393: fly_attack_dart
        1394: load_dart  # Throw Weapon (Reload)
        1395: fly_load_dart
        1396: wa_dart_target_stand
        1397: fly_wa_dart_target_stand
        1398: wa_dart_target_emote_talk
        1399: fly_wa_dart_target_emote_talk
        1400: bar_patron_sit_emote_cheer
        1401: fly_bar_patron_sit_emote_cheer
        1402: bar_patron_sit_custom_spell01
        1403: fly_bar_patron_sit_custom_spell01
        1404: bar_patron_sit_custom_spell02
        1405: fly_bar_patron_sit_custom_spell02
        1406: bar_patron_sit_custom_spell03
        1407: fly_bar_patron_sit_custom_spell03
        1408: bar_piano_stand
        1409: fly_bar_piano_stand
        1410: bar_piano_emote_talk
        1411: fly_bar_piano_emote_talk
        1412: wa_hearth_sit
        1413: fly_wa_hearth_sit
        1414: wa_hearth_sit_emote_cry
        1415: fly_wa_hearth_sit_emote_cry
        1416: wa_hearth_sit_emote_cheer
        1417: fly_wa_hearth_sit_emote_cheer
        1418: wa_hearth_sit_custom_spell01
        1419: fly_wa_hearth_sit_custom_spell01
        1420: wa_hearth_sit_custom_spell02
        1421: fly_wa_hearth_sit_custom_spell02
        1422: wa_hearth_sit_custom_spell03
        1423: fly_wa_hearth_sit_custom_spell03
        1424: wa_hearth_stand
        1425: fly_wa_hearth_stand
        1426: wa_hearth_stand_emote_cheer
        1427: fly_wa_hearth_stand_emote_cheer
        1428: wa_hearth_stand_emote_talk
        1429: fly_wa_hearth_stand_emote_talk
        1430: wa_hearth_stand_custom_spell01
        1431: fly_wa_hearth_stand_custom_spell01
        1432: wa_hearth_stand_custom_spell02
        1433: fly_wa_hearth_stand_custom_spell02
        1434: wa_hearth_stand_custom_spell03
        1435: fly_wa_hearth_stand_custom_spell03
        1436: wa_scribe_start
        1437: fly_wa_scribe_start
        1438: wa_scribe_loop
        1439: fly_wa_scribe_loop
        1440: wa_scribe_end
        1441: fly_wa_scribe_end
        1442: wa_emote_scribe
        1443: fly_wa_emote_scribe
        1444: haymaker  # Haymaker (Kul Tiran only)
        1445: fly_haymaker
        1446: haymaker_precast  # Haymaker (Windup) (Kul Tiran only)
        1447: fly_haymaker_precast
        1448: channel_cast_omni_up

        # starting with 8.2.0.30080
        1449: fly_channel_cast_omni_up
        1450: dh_jump_land_run
        1451: fly_dh_jump_land_run
        1452: cinematic01
        1453: fly_cinematic01
        1454: cinematic02
        1455: fly_cinematic02
        1456: cinematic03
        1457: fly_cinematic03
        1458: cinematic04
        1459: fly_cinematic04
        1460: cinematic05
        1461: fly_cinematic05
        1462: cinematic06
        1463: fly_cinematic06
        1464: cinematic07
        1465: fly_cinematic07
        1466: cinematic08
        1467: fly_cinematic08
        1468: cinematic09
        1469: fly_cinematic09
        1470: cinematic10
        1471: fly_cinematic10

        # Starting wth 8.2.5.31337
        1472: take_off_start
        1473: fly_take_off_start
        1474: take_off_finish
        1475: fly_take_off_finish
        1476: land_start
        1477: fly_land_start
        1478: land_finish
        1479: fly_land_finish

        # Starting with 8.3.0.32044
        1480: wa_walk_talk
        1481: fly_wa_walk_talk
        1482: wa_perch03
        1483: fly_wa_perch03

        # Starting with 8.3.0.32593
        1484: carriage_mount_moving
        1485: fly_carriage_mount_moving

        # Starting with 9.0.1.33978
        1486: take_off_finish_fly
        1487: fly_take_off_finish_fly
        1488: combat_ablity_2h_big02
        1489: fly_combat_ablity_2h_big02
        1490: mount_wide
        1491: fly_mount_wide

        # Starting with 9.0.1.34199
        1492: emote_talk_subdued
        1493: fly_emote_talk_subdued

        # Starting with 9.0.1.34365
        1494: wa_sit04
        1495: fly_wa_sit04

        # Starting with 9.0.1.35432
        1496: mount_summon
        1497: fly_mount_summon

        # Starting with 9.0.5.37503
        1498: emote_selfie
        1499: fly_emote_selfie
        1500: custom_spell11
        1501: fly_custom_spell11
        1502: custom_spell12
        1503: fly_custom_spell12
        1504: custom_spell13
        1505: fly_custom_spell13
        1506: custom_spell14
        1507: fly_custom_spell14
        1508: custom_spell15
        1509: fly_custom_spell15
        1510: custom_spell16
        1511: fly_custom_spell16
        1512: custom_spell17
        1513: fly_custom_spell17
        1514: custom_spell18
        1515: fly_custom_spell18
        1516: custom_spell19
        1517: fly_custom_spell19
        1518: custom_spell20
        1519: fly_custom_spell20
        1520: future_patch01
        1521: fly_future_patch01
        1522: future_patch02
        1523: fly_future_patch02
        1524: future_patch03
        1525: fly_future_patch03
        1526: future_patch04
        1527: fly_future_patch04
        1528: future_patch05
        1529: fly_future_patch05
        1530: future_patch06
        1531: fly_future_patch06
        1532: future_patch07
        1533: fly_future_patch07
        1534: future_patch08
        1535: fly_future_patch08
        1536: future_patch09
        1537: fly_future_patch09
        1538: future_patch10
        1539: fly_future_patch10
        1540: future_patch11
        1541: fly_future_patch11
