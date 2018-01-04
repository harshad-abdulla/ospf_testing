from netmiko import ConnectHandler
from yaml import load
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

def get_devices(file_name):
    """Read the device data from the device json file and return it as a dictionary"""
    with open(file_name, 'r') as f:
        dump = load(f)
    n = int(dump['Device_count'])
    devices = []
    while (n>0):
        devices.append(dump['Device'+str(n)])
        n = n-1
    return devices

def get_handle(devices):
    """Takes a list of device dictionsary and embeds the connection handle with the dictionary"""
    for device in devices:
        ip = device['ip']
        try:
            handle = ConnectHandler(**device)
        except (AuthenticationException):
            print 'Authentication failure: ' + ip
            continue
        except (NetMikoTimeoutException):
            print 'Timeout of Device: ' + ip
            continue
        except (EOFError):
            print 'End of file attempting to device: ' + ip
            continue
        except (SSHException):
            print 'SSH issue! Make you sure SSH is enabled on:' + ip
            continue
        except Exception as unknown_error:
            print 'Error Occurred: ' + unknown_error
            continue

        device['handle'] = handle