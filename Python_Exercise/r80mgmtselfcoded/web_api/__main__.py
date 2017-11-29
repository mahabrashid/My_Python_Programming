'''
Created on 9 Jan 2017

@author: marashid

The program can be started from the command-line using "python web_api" command
'''
# import os, sys
# 
# project_path = os.path.abspath((os.path.join(os.path.dirname(__file__), "..\\")))
# print(project_path)
# sys.path.append(project_path)

from sessions_package import session_mgmt, session
from utility import api_mgmt
from objects_package import host_mgmt

if __name__ == '__main__':
    print("web_api module started")

try:
    login_res = session_mgmt.login()
    print(login_res)    
    ## if the login_res is successful
    if(api_mgmt.api_call_successful(login_res)):
        ## get the 'sid' from the login_res and set the session id
        session.set_sessioni_id(login_res['sid'])
        ## then add a host
        add_host_res = host_mgmt.add_host("py-api_mgmt-host1", "192.168.1.101")
        ## ONLY print the response in case of a failed execution
        if(not api_mgmt.api_call_successful(add_host_res)):
            print(add_host_res)
        ## otherwise go ahead and publish the session
        else:
            pub_res = session_mgmt.publish()
            print(pub_res)
            
except Exception as e:
    print("Something went wrong!")
    print(e.__str__())