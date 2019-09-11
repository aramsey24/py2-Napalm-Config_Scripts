#This script compares the spcified file of configs. If it exists
#this it writes "no changes required", else it would write the config and save. 
#**important to note that any configs to be compared on teh router must be written exactly
#as it appears on the router, pay attention to spacing in running-config. 
#Otherwise it will fail. 
#note: if the acl exists but an acl entry is missing the script will add it and display
#the added entry.




import json
from napalm import get_network_driver
driver = get_network_driver('ios')
rtr = driver('192.168.122.27', 'cisco', 'cisco')
rtr.open()
print('accessing Sw1')
rtr.load_merge_candidate(filename='acl1.cfg')

diffs = rtr.compare_config()
if len(diffs) > 0:
    print(diffs)
    rtr.commit_config()
else:
    print('no changes required on' + rtr)
    rtr.discard_config()

rtr.close()

