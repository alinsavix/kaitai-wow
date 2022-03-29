types:
    m2event:
        seq:
            - id: eventid
              type: str
              size: 4
              encoding: ASCII
              doc: "usually a 3 character string prefixed with $"
              simplifier: simplify_events
            - id: data
              type: u4
              doc: "passed when event is fired"
            - id: bone
              type: u4
              doc: "where event is attached"
            - id: position
              type: c3vector
              doc: "relative to that bone"
            - id: enabled
              type: m2trackbase
