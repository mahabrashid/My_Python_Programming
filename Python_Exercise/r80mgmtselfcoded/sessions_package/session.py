'''
Created on 8 Jan 2017

@author: marashid
'''
__session_id = None

def set_sessioni_id(sid):
    global __session_id
    __session_id = sid
    
def get_session_id():
    return __session_id