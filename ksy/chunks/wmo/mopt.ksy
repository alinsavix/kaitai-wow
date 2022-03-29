types:
    chunk_mopt:
        doc: "Map Object Portal Information"
        doc-ref: https://wowdev.wiki/WMO#MOPT_chunk

        seq:
            - id: portal_info  # FIXME: name?
              type: portal_info  # FIXME: Actual type is SMOPortal
              repeat: eos

    portal_info:
        doc: |
            This structure describes one portal separating two WMO groups. A single portal is usually made up of four vertices in a quad (starting at startVertex and going to startVertex + count). However, portals support more complex shapes, and can fully encompass holes such as the archway leading into Ironforge and parts of the Caverns of Time.

            It is likely that portals are drawn as GL_TRIANGLE_STRIP in WoWs occlusion pipeline, since some portals have a vertex count that is not evenly divisible by four. One example of this is portal #21 in CavernsOfTime.wmo from Build #5875 (WoW 1.12.1), which has 10 vertices.

        seq:
            - id: start_vertex
              type: u2
            - id: count
              type: u2
            - id: plane
              type: c4plane
