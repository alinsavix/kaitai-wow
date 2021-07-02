types:
    chunk_mosb:
        doc: "Map Object Sky Box - zero terminated skybox. If first byte is 0, skybox flag in all MOGI entries are cleared and there is no skybox"
        doc-ref: https://wowdev.wiki/WMO#MOSB_chunk_.28optional.29.E1.B5.98

        seq:
            - id: skybox_name
              type: strz
