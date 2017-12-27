from netmiko import ConnectHandler
import logging

def connect_device(ip, username, password):
    """Connects to a device"""
    cisco_L2 = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password
    }

    return ConnectHandler(**cisco_L2)


def int_config(handler, int, ip, mask):
    """Configure the interface"""
    config_commands = ['int '+ int, 'ip address ' +ip + " "+ mask, 'no shut']
    output = handler.send_config_set(config_commands)
    print output

def show_command(handler,cmd):
    print handler.send_command(cmd)
