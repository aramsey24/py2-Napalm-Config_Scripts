import json
from napalm import get_network_driver
driver = get_network_driver('ios')
rtr = driver('192.168.122.26', 'cisco', 'cisco')
rtr.open()

print('accessing 192.168.122.26')
rtr.load_merge_candidate(filename='acl1.cfg')

diffs = rtr.compare_config()
if len (diffs) > 0:
    print(diffs)
    rtr.commit_config()
else:
    print('no acl changes required.')
    rtr.discard_config()

rtr.load_merge_candidate(filename='ospf1.cfg')

diffs = rtr.compare_config()
if len (diffs) > 0:
    print(diffs)
    rtr.commit_config()
else:
    print('no ospf changes required.')
    rtr.discard_config()           

rtr.close()