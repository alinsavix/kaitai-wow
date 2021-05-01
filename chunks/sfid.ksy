# FIXME: This is broken, because we need to repeat this whole tiny structure
# some number of times
#
# Here's the whole description off of wowdev.wiki:
# Some model files, for example 'Creature\NightborneFemaleCitizen\NightborneFemaleCitizen.m2'
# have 4 skin files and 2 lod files but only 20 bytes are in chunk. In chunk there are 4
# skins and 1 lod present.

# Lod skins are selected based on distance to entity/doodad and chosen based on
# GetCVar("entityLodDist")/X and GetCVar("doodadLodDist")/X where X - distance.
# Lods are ignored when "M2UseLOD" CVar is set to 0.
types:
    chunk_sfid:
        doc: "Skin File Data IDs"
        doc-ref: https://wowdev.wiki/M2#SFID
        seq:
            - id: skin_file_data_ids
              type: u4
              repeat: expr
              repeat-expr: _root.chunks[0].data.as<chunk_md21>.data.as<chunk_md20>.num_skin_profiles

            # Doesn't seem to be a way to calculate how many of these there
            # are, so just run to end of chunk.
            - id: lod__skin_file_data_ids
              type: u4
              repeat: eos
