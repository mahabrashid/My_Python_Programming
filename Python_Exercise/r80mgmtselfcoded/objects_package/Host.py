'''
Created on 21 Nov 2017

@author: marashid
'''
class Host():
    __uid = None
    __name = None
    __ip_address = None
    
    ## optional parameters
    __color = None
    __comments = None
    
    def __init__(self, uid, name, ip_address, color, commments):
        self.__name = name
        self.__ip_address = ip_address
        
        if 