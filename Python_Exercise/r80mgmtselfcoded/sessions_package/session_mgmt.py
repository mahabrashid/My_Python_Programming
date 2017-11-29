# should inherit from sessions_package
import requests
import json
import getpass

from utility import api_mgmt
from objects_package import host_mgmt
from sessions_package import session

def __get_credentials():
    user_name = "Skyler"
#     input("Enter user name: ")
    password = "vpn123"  
#     getpass.getpass("Enter password: ")
    credentials = {"user" : user_name, "password" : password}
    return credentials

def login():
    _data = __get_credentials()
    return api_mgmt.api_call("login", _data)

def publish():
    _data = {}
    return api_mgmt.api_call("publish", _data) 

## function to return a json object to imitate object returned by R80 api_mgmt call in absense of a real server
def _get_example_json_for_test():
    ##json.dumps() serializes a python object to a json object while json.loads() deserializes a json obj to a python object (dictionary)
    return json.dumps({'uid': '056ccb14-bb96-4392-b076-53b56a2240ac', 'sid': 'fKyT5hDZx7bfWMLYfnmYBa_RgF2vj-X2AFnW8GsN2EI', 'url': 'https://35.158.94.126:443/web_api', 'session-timeout': 600, 'api_mgmt-server-version': '1.1'})

def logout():
    pass

'''
needs to be somewhere else
'''
def _get_uid(res):
    return res['uid']