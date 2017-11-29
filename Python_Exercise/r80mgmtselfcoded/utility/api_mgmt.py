import requests
import json

'''
Created on 7 Nov 2017

@author: marashid
'''
from sessions_package import session

__web_url = None
__header = None

def __set_web_url():
    ip_ = "54.93.184.38"
#       input("Enter the server ip-address: ") ## needs verifying for invalid input
    protocol = "https"
#       input("Enter the web protocol: ") ## needs verifying for invalid input
    port_ = 443 
#       input("Enter the port number: ") ## needs verifying for invalid input
    global __web_url
    __web_url = protocol + "://" + ip_ + ":" + str(port_) + "/web_api/"

def get_url():
    global __web_url
    if(__web_url == None):  
        __set_web_url()
    return __web_url

def __get_header():
    if (session.get_session_id() is None):
        __header = {"Content-Type" : "application/json"}
    else:
        __header = {"Content-Type" : "application/json", "X-chkp-sid" : session.get_session_id()}
    return __header

def api_call(command, _data):
#     print("{} received: {}, {}, {}".format(__name__, command, _data, _headers))
    r = requests.post(get_url() +"/" + command, data=json.dumps(_data), headers=__get_header(), verify=False)
    return r.json()

'''
check the login_res to extract key=value pairs.
if login_res is successful, it would always have an 'uid' key, 
if unsuccessful, it would have a 'code' key with error details.
'''    
def api_call_successful(api_response):
    if('uid' in api_response): ## if the key 'uid' exists in the dictionary
            return True
    elif('code' in api_response): ## if the key 'code' exists in the dictionary
            return False
    else:
        return False