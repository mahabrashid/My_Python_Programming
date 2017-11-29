'''
Created on 21 Nov 2017

@author: marashid
'''
from utility import api_mgmt

host1 = {"name":"py-api_mgmt-host1", "ip-address":"192.168.1.101", "color":"green"}
host2 = {"name":"py-api_mgmt-host2", "ip-address":"192.168.1.102", "color":"green"}
host3 = {"name":"py-api_mgmt-host3", "ip-address":"192.168.1.103", "color":"green"}
host4 = {"name":"py-api_mgmt-host4", "ip-address":"192.168.1.104", "color":"green"}
host5 = {"name":"py-api_mgmt-host5", "ip-address":"192.168.1.105", "color":"green"}

def add_host(name, ip_address, color="green", comments="added from python code", set_if_exists=True):
    _data = {"name":name, "ip-address":ip_address, "color":color, "comments":comments}
    return api_mgmt.api_call("add-host", _data)

def delete_host():
    pass

def show_host():
    pass

def show_hosts():
    pass

def set_host():
    pass