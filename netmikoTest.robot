*** Settings ***
Library           E:/Dev/Netmiko/netmiko_fun.py    # Netmiko user defined functions

*** Test Cases ***
intConfig
    ${handler}=    connect device    192.168.122.72    david    cisco
    log    Connected to device
    log    Configuring interface
    int config    ${handler}    loop 1    2.2.2.2    255.255.255.0
    show command    ${handler}    show ip int brief
