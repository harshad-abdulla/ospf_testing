from netmiko import ConnectHandler

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
