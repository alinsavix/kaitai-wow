enums:
    m2texture_types:
        0:
            id: normal
            doc: "Texture given in filename"

        # component textures
        1:
            id: component_skin
            doc: "Skin -- Body + clothes"
        2:
            id: component_object_skin
            doc: "Object Skin -- Item, Capes (Item/ObjectComponents/Cape/*.blp)"
        3:
            id: component_weapon_blade
            doc: "Weapon Blade -- Used on several models but not in client. Armor reflect?"
        4:
            id: component_weapon_handle
            doc: "Weapon Handle"
        5:
            id: component_environment
            doc: "Environment (OBSOLETE)"
        6:
            id: component_char_hair
            doc: "Character Hair"
        7:
            id: component_char_facial_hair
            doc: "Character Facial Hair (OBSOLETE)"
        8:
            id: component_skin_extra
            doc: "Skin Extra"
        9:
            id: component_ui_skin
            doc: "UI Skin -- Used on inventory art M2s: inventoryartgeometry.m2, inventoryartgeometryold.m2"
        10:
            id: component_tauren_mane
            doc: "Character Misc (OBSOLETE)"
        11:
            id: component_monster_1
            doc: "Monster Skin 1 -- for creatures or game objects"
        12:
            id: component_monster_2
            doc: "Monster Skin 2 -- for creatures or game objects"
        13:
            id: component_monster_3
            doc: "Monster Skin 3 -- for creatures or game objects"
        14:
            id: component_item_icon
            doc: "Item Icon -- Used on inventory art M2s: ui-button.m2, forcedbackpackitem.m2"

        # Guild-related textures
        15:
            id: guild_color_background
        16:
            id: guild_color_emblem
        17:
            id: guild_color_border
        18:
            id: guild_emblem

        # Character customizations
        19:
            id: character_eyes
        20:
            id: character_accessory
        21:
            id: character_skin_secondary
        22:
            id: character_hair_secondary
        23:
            id: character_armor_secondary
        24:
            id: character_unknown

types:
    m2texture_flags:
        seq:
            - id: texture_wrap_x
              type: b1 # 0x01
            - id: texture_wrap_y
              type: b1 # 0x02

    m2texture:
        seq:
            - id: type
              type: u4
              enum: m2texture_types
              doc-ref: https://wowdev.wiki/M2#Texture_Types
              doc: |
                  Texture type is 0 for regular textures, nonzero for skinned textures (filename not referenced in the M2 file!) For instance, in the NightElfFemale model, her eye glow is a type 0 texture and has a file name, the other 3 textures have types of 1, 2 and 6. The texture filenames for these come from client database files:

                  DBFilesClient\CharSections.dbc
                  DBFilesClient\CreatureDisplayInfo.dbc
                  DBFilesClient\ItemDisplayInfo.dbc
                  (possibly more)
            - id: flags
              type: m2texture_flags
              size: 4
            - id: filename
              type: m2array<str>
