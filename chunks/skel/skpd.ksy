types:
    chunk_skpd:
        doc: |
            Skeleton Parent Data. Parent skeleton file data id is used for
            de-duplication.   e.g. `lightforgeddraeneimale` references
            `draeneimale_hd`. The former does not have any .anim files, but
            uses those of the latter via parent-link (does not even have an
            AFID chunk).

            Note that it appears the child .skels still have SKx1 chunks, so
            apparently only FID are shared?
        doc-ref: https://wowdev.wiki/M2/.skel#SKPD
        seq:
            - id: unknown1
              type: u1
              repeat: expr
              repeat-expr: 8
              doc: "May not be used"
            - id: parent_skel_file_id
              type: u4
            - id: unknown2
              type: u1
              repeat: expr
              repeat-expr: 4
              doc: "May not be used"
