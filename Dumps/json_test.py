import json
from pprint import pprint

device = {
    'device_type': 'cisco_ios',
    'ip':   '10.10.10.10',
    'username': 'test',
    'password': 'password',
    'port' : 8022,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
    'verbose': False,       # optional, defaults to False
}

# Writing JSON data
#with open('device.json', 'w') as f:
#     json.dump(device, f)

# Reading data back
with open('device.json', 'r') as f:
     data = json.load(f)

print type(data)
print "-------------------------------"
pprint(data)
