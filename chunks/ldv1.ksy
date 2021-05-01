types:
    chunk_ldv1:
        doc: "LoD (Level of Detail) Data"
        doc-ref: https://wowdev.wiki/M2#LDV1
        seq:
            - id: unk0
              type: u2
            - id: lod_count
              type: u2
              doc: "maxLod = lod_count - 1"
            - id: unk2
              type: f4
              doc: "Purpose unknown, but is loaded into the formula `xf(fminf(740.0 / unk2_f, 5.0), 0.5)`"
            - id: particle_bone_lod
              type: u1
              repeat: expr
              repeat-expr: 4
              doc: |
                Defines `_lod%02d.skin` files. As an example, on `pandarenfemale.m2`, lod_count == 4. SFID has 7 files, the first 4 are ordinary `.skin` files, the last 3 are `_lod%02d.skin` files. Enumeration starts from 1, and the last file in SFID is `pandarenfemale_lod03.skin`.

                LodData.particleBoneLod works this way: Each model has current lod which is `[0..3]`. Then:

                ```
                if ( lod < 1 )
                    result = 0

                if ( LodData )
                    result = (0x10000 << LodData->particleBoneLod[lod])
                else
                    result = (0x10000 << (lod- 1))


                //For each ParticleEmitter and related M2Particle record
                if ( result & M2CompBone[M2Particle->old.boneIndex].flags ) {
                    // Do not animate this emitter
                }
                ```

            - id: unk4
              type: u4
