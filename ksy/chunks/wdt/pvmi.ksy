types:
    chunk_pvmi:
        doc: "Map Particle Volume Info. If PVPD is already read, it is nulled. If PVMI comes first, PVPD may be non-null. Actual files order as PVMI PVPD PVBD"
        doc-ref: https://wowdev.wiki/WDT#PVMI

        # FIXME: Contains a blob whose structure isn't completely known
        seq: []

        instances:
            note:
                value: '"not implemented"'
