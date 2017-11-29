'''
Created on 9 Jan 2017

@author: marashid

Standard Code Layout and Naming Convention
--------------------------------------------
Private (internal) methods or variable should begin with a single underscore
'''

class SameClassName():
    '''
    Purpose: to see how a class with same name as the file behaves
    '''
    _list = []
    _str = None
    _int = 0


    def __init__(self, params):
        '''
        Constructor
        '''
        self._list = params[0]
        self._str = params[1]
        self._int = params[2]
        
    def method_one(self):   # function can only be used by an instance
        print("method one")
        
    def method_two():   # function can only be used by a class
        print("method two")