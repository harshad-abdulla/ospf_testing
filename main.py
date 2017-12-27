from netmiko_fun import *

net_connect = connect_device('192.168.122.72','david','cisco')

print "Configuring interface..."

int_config(net_connect,"loop 0","1.1.1.1","255.255.255.0")

print net_connect.send_command('show ip int brief')

show_command(net_connect,"show ip int brief")