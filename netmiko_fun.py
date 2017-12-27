from netmiko import ConnectHandler
import logging
from json import load
from pprint import pprint

def get_device(file_name):
    """Read the device data from the device json file and return it as a dictionary"""
    with open(file_name, 'r') as f:
        device = load(f)
        return pprint(device)

def connect_device(device):
    """Connects to a device"""
    return ConnectHandler(**device)


def int_config(handler, int, ip, mask):
    """Configure the interface"""
    config_commands = ['int '+ int, 'ip address ' +ip + " "+ mask, 'no shut']
    output = handler.send_config_set(config_commands)
    print output

def show_command(handler,cmd):
    print handler.send_command(cmd)
