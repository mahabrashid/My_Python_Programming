'''
Created on 9 Jan 2017

@author: marashid
'''

### Not sure this needs to be a dedicated class, maybe should exist in SessionMgmt script as local variable instead

class WebUrl:
    '''
    This class will set the web url for mgmt server
    '''
    __web_url = None
    
    def __init__(self):
        '''
        api web_url
        '''
        self.__set_web_url()
   
    def get_web_url(self):
        if(self.__web_url == None):  ## can't access the 
            __web_url = self.__set_web_url()
        else:
            print("in get method, web url: ", self._web_url)
            return __web_url
   
    def __set_web_url(self):
        ip_ = "35.159.17.192"
#       input("Enter the server ip-address: ") ## needs verifying for invalid input
        protocol = "https" 
#       input("Enter the web protocol: ") ## needs verifying for invalid input
        port_ = 443 
#       input("Enter the port number: ") ## needs verifying for invalid input
        self._web_url = protocol + "://" + ip_ + ":" + str(port_) + "/web_api/"
        print("in set method, web url for server: ", self._web_url)