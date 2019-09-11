#note: config for file "acls4"
#spanning-tree mode rapid-pvst

#interface range g0/0 - 1
#switchport trunk encap dot1q
#switchport mode trunk
#spanning-tree portfast

#ip access-list extended 100
#permit icmp any any 
#permit ospf any any
#permit tcp any any eq bgp
#permit tcp any eq bgp any
#permit tcp any any eq 22
#permit tcp any eq 22 any
#permit tcp any any eq 443

#interface vlan 1
#ip access-group 100 in


import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.30', 'cisco', 'cisco')
iosvl2.open()
 
print ('Accessing 192.168.122.30')
print(iosvl2.compare_config())
iosvl2.load_merge_candidate(filename='acls4.cfg')
iosvl2.commit_config()
iosvl2.close()