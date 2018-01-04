from Final_Functions import *
from netmiko_fun import show_command

devices = get_devices("devices.yaml")
print devices

get_handle(devices)
print devices

for device in devices:
    print "Interface details of device: " + device['ip']
    show_command(device['handle'],'show ip int brief')

"""net_connect = connect_device(device)"""

"""
print "Configuring interface..."

int_config(net_connect,"loop 0","1.1.1.1","255.255.255.0")

print net_connect.send_command('show ip int brief')

show_command(net_connect,"show ip int brief")

"""