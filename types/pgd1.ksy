# FIXME: Really this should be in chunk_pgd1, probably, but we need it in
# the main type repo so that m2array can find it. We shouldn't need to do
# this once we have m2array fixed up to be more sane somehow, or maybe we
# can deep merge special types into the m2array enum? Not sure.
types:
    pgd1_entry:
        seq:
            - id: geoset
              type: u2
