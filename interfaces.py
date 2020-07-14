class RoutedInterface(object):
    def __init__(self, interface='eth1/1', description='My Description',
        vrf='default',  layer='Layer3', ip_address='10.0.0.1/32',
        admin_state='up'):
        self.topSystem = {
    "children": [
      {
        "ipv4Entity": {
          "children": [
            {
              "ipv4Inst": {
                "children": [
                  {
                    "ipv4Dom": {
                      "attributes": {
                        "name": vrf
                      },
                      "children": [
                        {
                          "ipv4If": {
                            "attributes": {
                              "id": interface
                            },
                            "children": [
                              {
                                "ipv4Addr": {
                                  "attributes": {
                                    "addr": ip_address,
                                    "pref": "0",
                                    "tag": "0"
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
            }
          ]
        }
      },
      {
        "interfaceEntity": {
          "children": [
            {
              "l1PhysIf": {
                "attributes": {
                  "adminSt": admin_state,
                  "descr": description,
                  "id": interface,
                  "layer": layer,
                  "userCfgdFlags": "admin_state"
                },
                "children": [
                  {
                    "nwRtVrfMbr": {
                      "attributes": {
                        "tDn": "sys/inst-{}".format(vrf)
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
    def __repr__(self):
        return str(self.topSystem)



class LoopbackInterface(object):
    def __init__(self, interface='eth1/1', description='My Description',
        vrf='default', ip_address='10.0.0.1/32',
        admin_state='up'):
        self.topSystem = {
    "children": [
      {
        "ipv4Entity": {
          "children": [
            {
              "ipv4Inst": {
                "children": [
                  {
                    "ipv4Dom": {
                      "attributes": {
                        "name": vrf
                      },
                      "children": [
                        {
                          "ipv4If": {
                            "attributes": {
                              "id": interface
                            },
                            "children": [
                              {
                                "ipv4Addr": {
                                  "attributes": {
                                    "addr": ip_address,
                                    "pref": "0",
                                    "tag": "0"
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
                      },
                      "children": [
                        {
                          "nwRtVrfMbr": {
                            "attributes": {
                              "tDn": "sys/inst-{}".format(vrf)
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
        def __repr__(self):
            return str(self.topSystem)
