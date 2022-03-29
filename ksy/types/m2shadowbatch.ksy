types:
    m2shadowbatch:
        doc: |
            Shadow Batches

            Generated on the fly, conditionally:
            if !(batches[i].flags & 4) && !batches[i].texunit
               && !(renderflags[batches[i].renderFlag].flags & 0x40)
               && (renderflags[batches[i].renderFlag].blendingmode < 2u
               || renderflags[batches[i].renderFlag].flags & 0x80)
        doc-ref: https://wowdev.wiki/M2/.skin#shadow_batches
        seq:
            - id: flags
              type: u1
              doc: "if auto-generated: M2Batch.flags & 0xFF"
            - id: flags2
              type: u1
              doc: |
                if auto-generated: (renderFlag[i].flags & 0x04 ? 0x01 : 0x00)
                    | (!renderFlag[i].blendingmode ? 0x02 : 0x00)
                    | (renderFlag[i].flags & 0x80 ? 0x04 : 0x00)
                    | (renderFlag[i].flags & 0x400 ? 0x06 : 0x00)
            - id: unknown1
              type: u2
            - id: submesh_id
              type: u2
            - id: texture_id
              type: u2
            - id: color_id
              type: u2
            - id: transparency_id
              type: u2
