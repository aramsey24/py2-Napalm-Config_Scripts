#you can add more configs to teh file "acl1.cfg" and change its name to reflect
#this script may be a bit raw but configures the devices. 
#still need to get the output to print via json


import json
from napalm import get_network_driver

acl_routers = ['192.168.122.27',
               '192.168.122.28',
               '192.168.122.29'
               ]

for ip_address in acl_routers:
    print('connecting to ' + str(ip_address))
    driver = get_network_driver('ios')
    acl_routers = driver(ip_address, 'cisco', 'cisco')
    acl_routers.open()
    print(acl_routers.compare_config())
    acl_routers.load_merge_candidate(filename ='acl1.cfg')
    acl_routers.commit_config()
    acl_routers.close()