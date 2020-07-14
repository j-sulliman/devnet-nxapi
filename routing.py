class OspfFeature(object):
    def __init__(self, status='enabled'):
        self.topSystem = {
            "children": [
              {
                "fmEntity": {
                  "children": [
                    {
                      "fmOspf": {
                        "attributes": {
                          "adminSt": status
                        }
                      }
                    }
                  ]
                }
              }
            ]
          }



class OspfInt(object):
    def __init__(self, interface='eth1/1', area='0.0.0.0',
        vrf='underlay-1', type='p2p'):
        self.topSystem = {
    "children": [
          {
            "ospfEntity": {
              "children": [
                {
                  "ospfInst": {
                    "attributes": {
                      "name": "1"
                    },
                    "children": [
                      {
                        "ospfDom": {
                          "attributes": {
                            "name": vrf
                          },
                          "children": [
                            {
                              "ospfIf": {
                                "attributes": {
                                  "advertiseSecondaries": "yes",
                                  "area": area,
                                  "id": interface,
                                  "nwT": type
                                }
                              }
                            }
                          ]
                        }
                      }
                    ]
                  }
                }
              ]
            }
          },
          {
            "interfaceEntity": {
              "children": [
                {
                  "l3LbRtdIf": {
                    "attributes": {
                      "id": interface
                    }
                  }
                }
              ]
            }
          }
        ]
        }
    def __repr__(self):
        return str(self.topSystem)
