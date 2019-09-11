#this script adds multiple config files to multiple routers. 
#however, this is in a situation where all routers require the same configs, such
#as control plane, spanning-tree or vty configuration. This does not apply to OSPF or #BGP, route-reflector, where each router advertises a different network and config would most likely be different on each router. 


import json
from napalm import get_network_driver
devicelist = ['192.168.122.26',
              '192.168.122.27', 
              '192.168.122.28',
              '192.168.122.29'
             ]                
                 

for ip_address in devicelist:
    print('connecting to ' + str(ip_address))
    driver = get_network_driver('ios')
    rtrs = driver(ip_address, 'cisco', 'cisco')
    rtrs.open()
    rtrs.load_merge_candidate(filename='acl1.cfg')
    diffs = rtrs.compare_config()
    if len (diffs) > 0:
        print(diffs)
        rtrs.commit_config()
    else:
        print('no acl changes required.')
        rtrs.discard_config()

    rtrs.load_merge_candidate(filename='cp.cfg')

    diffs = rtrs.compare_config()
    if len (diffs) > 0:
        print(diffs)
        rtrs.commit_config()
    else:
        print('no CP config changes required.')
        rtrs.discard_config()
    rtrs.close()
