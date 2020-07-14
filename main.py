from nx_requests import post
from interfaces import RoutedInterface, LoopbackInterface
from routing import OspfInt, OspfFeature



switches = [{
        'hostname': 'nxosv-1',
        'management': '192.168.200.136',
        'interfaces': [
                    {
                    'id' : 'lo0',
                    'description' : 'nxosv-1_RID',
                    'ip' : '10.254.254.1/32',
                    'layer' : 'Layer3',
                    'vrf' : 'underlay-1',
                    'admin_state' : 'up'
                    },
                    {
                    'id' : 'eth1/1',
                    'description' : 'L3_nxosv-2_e1/1',
                    'ip' : '10.0.0.1/30',
                    'layer' : 'Layer3',
                    'vrf' : 'underlay-1',
                    'admin_state' : 'up'
                    },
                    {
                    'id' : 'eth1/2',
                    'description' : 'L3_nxosv-3_e1/2',
                    'ip' : '10.0.0.5/30',
                    'layer' : 'Layer3',
                    'vrf' : 'underlay-1',
                    'admin_state' : 'up'
                    },
                    {
                    'id' : 'eth1/3',
                    'description' : 'L3_nxosv-4_e1/3',
                    'ip' : '10.0.0.9/30',
                    'layer' : 'Layer3',
                    'vrf' : 'underlay-1',
                    'admin_state' : 'up'
                    }
                    ],
        'routing': [
                    {
                    'protocol' : 'ospf',
                    'id' : 'lo0',
                    'type' : 'p2p',
                    'vrf' : 'underlay-1',
                    'process' : 'ospf_underlay-1',
                    'area' : '0.0.0.0'
                    },
                    {
                    'protocol' : 'ospf',
                    'id' : 'eth1/1',
                    'type' : 'p2p',
                    'vrf' : 'underlay-1',
                    'process' : 'ospf_underlay-1',
                    'area' : '0.0.0.0'
                    },
                    {
                    'protocol' : 'ospf',
                    'id' : 'eth1/2',
                    'type' : 'p2p',
                    'vrf' : 'underlay-1',
                    'process' : 'ospf_underlay-1',
                    'area' : '0.0.0.0'
                    },
                    {
                    'protocol' : 'ospf',
                    'id' : 'eth1/3',
                    'type' : 'p2p',
                    'vrf' : 'underlay-1',
                    'process' : 'ospf_underlay-1',
                    'area' : '0.0.0.0'
                    }
        ]
},
{
                'hostname': 'nxosv-2',
                'management': '192.168.200.135',
                'interfaces': [
                            {
                            'id' : 'lo0',
                            'description' : 'nxosv-2_RID',
                            'ip' : '10.254.254.2/32',
                            'layer' : 'Layer3',
                            'vrf' : 'underlay-1',
                            'admin_state' : 'up'
                            },
                            {
                            'id' : 'eth1/1',
                            'description' : 'L3_nxosv-2_e1/1',
                            'ip' : '10.0.0.2/30',
                            'layer' : 'Layer3',
                            'vrf' : 'underlay-1',
                            'admin_state' : 'up'
                            },
                            {
                            'id' : 'eth1/2',
                            'description' : 'L3_nxosv-3_e1/2',
                            'ip' : '10.0.0.13/30',
                            'layer' : 'Layer3',
                            'vrf' : 'underlay-1',
                            'admin_state' : 'up'
                            },
                            {
                            'id' : 'eth1/3',
                            'description' : 'L3_nxosv-4_e1/3',
                            'ip' : '10.0.0.17/30',
                            'layer' : 'Layer3',
                            'vrf' : 'underlay-1',
                            'admin_state' : 'up'
                            }
                            ],
                'routing': [
                            {
                            'protocol' : 'ospf',
                            'id' : 'lo0',
                            'type' : 'p2p',
                            'vrf' : 'underlay-1',
                            'process' : 'ospf_underlay-1',
                            'area' : '0.0.0.0'
                            },
                            {
                            'protocol' : 'ospf',
                            'id' : 'eth1/1',
                            'type' : 'p2p',
                            'vrf' : 'underlay-1',
                            'process' : 'ospf_underlay-1',
                            'area' : '0.0.0.0'
                            },
                            {
                            'protocol' : 'ospf',
                            'id' : 'eth1/2',
                            'type' : 'p2p',
                            'vrf' : 'underlay-1',
                            'process' : 'ospf_underlay-1',
                            'area' : '0.0.0.0'
                            },
                            {
                            'protocol' : 'ospf',
                            'id' : 'eth1/3',
                            'type' : 'p2p',
                            'vrf' : 'underlay-1',
                            'process' : 'ospf_underlay-1',
                            'area' : '0.0.0.0'
                            }
                            ]
                    },
                    {
                            'hostname': 'nxosv-3',
                            'management': '192.168.200.137',
                            'interfaces': [
                                        {
                                        'id' : 'lo0',
                                        'description' : 'nxosv-3_RID',
                                        'ip' : '10.254.254.3/32',
                                        'layer' : 'Layer3',
                                        'vrf' : 'underlay-1',
                                        'admin_state' : 'up'
                                        },
                                        {
                                        'id' : 'eth1/1',
                                        'description' : 'L3_nxosv-4_e1/1',
                                        'ip' : '10.0.0.21/30',
                                        'layer' : 'Layer3',
                                        'vrf' : 'underlay-1',
                                        'admin_state' : 'up'
                                        },
                                        {
                                        'id' : 'eth1/2',
                                        'description' : 'L3_nxosv-1_e1/2',
                                        'ip' : '10.0.0.6/30',
                                        'layer' : 'Layer3',
                                        'vrf' : 'underlay-1',
                                        'admin_state' : 'up'
                                        },
                                        {
                                        'id' : 'eth1/3',
                                        'description' : 'L3_nxosv-2_e1/3',
                                        'ip' : '10.0.0.18/30',
                                        'layer' : 'Layer3',
                                        'vrf' : 'underlay-1',
                                        'admin_state' : 'up'
                                        }
                                        ],
                            'routing': [
                                        {
                                        'protocol' : 'ospf',
                                        'id' : 'lo0',
                                        'type' : 'p2p',
                                        'vrf' : 'underlay-1',
                                        'process' : 'ospf_underlay-1',
                                        'area' : '0.0.0.0'
                                        },
                                        {
                                        'protocol' : 'ospf',
                                        'id' : 'eth1/1',
                                        'type' : 'p2p',
                                        'vrf' : 'underlay-1',
                                        'process' : 'ospf_underlay-1',
                                        'area' : '0.0.0.0'
                                        },
                                        {
                                        'protocol' : 'ospf',
                                        'id' : 'eth1/2',
                                        'type' : 'p2p',
                                        'vrf' : 'underlay-1',
                                        'process' : 'ospf_underlay-1',
                                        'area' : '0.0.0.0'
                                        },
                                        {
                                        'protocol' : 'ospf',
                                        'id' : 'eth1/3',
                                        'type' : 'p2p',
                                        'vrf' : 'underlay-1',
                                        'process' : 'ospf_underlay-1',
                                        'area' : '0.0.0.0'
                                        }
                                        ]
                                        },
                    {
                                    'hostname': 'nxosv-4',
                                    'management': '192.168.200.138',
                                    'interfaces': [
                                                {
                                                'id' : 'lo0',
                                                'description' : 'nxosv-4_RID',
                                                'ip' : '10.254.254.4/32',
                                                'layer' : 'Layer3',
                                                'vrf' : 'underlay-1',
                                                'admin_state' : 'up'
                                                },
                                                {
                                                'id' : 'eth1/1',
                                                'description' : 'L3_nxosv-2_e1/1',
                                                'ip' : '10.0.0.22/30',
                                                'layer' : 'Layer3',
                                                'vrf' : 'underlay-1',
                                                'admin_state' : 'up'
                                                },
                                                {
                                                'id' : 'eth1/2',
                                                'description' : 'L3_nxosv-2_e1/2',
                                                'ip' : '10.0.0.14/30',
                                                'layer' : 'Layer3',
                                                'vrf' : 'underlay-1',
                                                'admin_state' : 'up'
                                                },
                                                {
                                                'id' : 'eth1/3',
                                                'description' : 'L3_nxosv-4_e1/3',
                                                'ip' : '10.0.0.10/30',
                                                'layer' : 'Layer3',
                                                'vrf' : 'underlay-1',
                                                'admin_state' : 'up'
                                                }
                                                ],
                                    'routing': [
                                                {
                                                'protocol' : 'ospf',
                                                'id' : 'lo0',
                                                'type' : 'p2p',
                                                'vrf' : 'underlay-1',
                                                'process' : 'ospf_underlay-1',
                                                'area' : '0.0.0.0'
                                                },
                                                {
                                                'protocol' : 'ospf',
                                                'id' : 'eth1/1',
                                                'type' : 'p2p',
                                                'vrf' : 'underlay-1',
                                                'process' : 'ospf_underlay-1',
                                                'area' : '0.0.0.0'
                                                },
                                                {
                                                'protocol' : 'ospf',
                                                'id' : 'eth1/2',
                                                'type' : 'p2p',
                                                'vrf' : 'underlay-1',
                                                'process' : 'ospf_underlay-1',
                                                'area' : '0.0.0.0'
                                                },
                                                {
                                                'protocol' : 'ospf',
                                                'id' : 'eth1/3',
                                                'type' : 'p2p',
                                                'vrf' : 'underlay-1',
                                                'process' : 'ospf_underlay-1',
                                                'area' : '0.0.0.0'
                                                }
                                                ]
                                                }
                            ]

for switch in switches:
    for interface in switch['interfaces']:
        if 'lo' in interface['id']:
            int_mode = LoopbackInterface(interface=interface['id'],
                        description=interface['description'],
                        vrf=interface['vrf'],
                        ip_address=interface['ip'],
                        admin_state=interface['admin_state'])
        elif 'lo' not in interface['id']:
            int_mode = RoutedInterface(interface=interface['id'],
                        description=interface['description'],
                        vrf=interface['vrf'],  layer=interface['layer'],
                        ip_address=interface['ip'],
                        admin_state=interface['admin_state'])
        post_data = post(mo_dn='mo/sys.json', mo='topSystem', mo_data=int_mode,
                    apic_url=switch['management'], apic_user='admin', apic_pw='Cisco123!')
    for protocol in switch['routing']:
        if protocol['protocol'] == 'ospf':
            print(switch['management'])
            ospf_feature = OspfFeature(status='enabled')
            post_data = post(mo_dn='mo/sys.json', mo='topSystem', mo_data=ospf_feature,
                        apic_url=switch['management'], apic_user='admin', apic_pw='Cisco123!')
            ospf_int = OspfInt(interface=protocol['id'], area=protocol['area'],
                vrf=protocol['vrf'], type=protocol['type'])
            post_data = post(mo_dn='mo/sys.json', mo='topSystem', mo_data=ospf_int,
                        apic_url=switch['management'], apic_user='admin', apic_pw='Cisco123!')
