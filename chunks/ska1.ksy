
types:
    chunk_ska1:
        doc: "Skeleton Attachment Data"
        doc-ref: https://wowdev.wiki/M2/.skel#SKA1
        seq:

            - id: attachments
              type: m2array(m2array_types::m2attachment)
            - id: attachment_lookup_table
              type: m2array(m2array_types::int16)
