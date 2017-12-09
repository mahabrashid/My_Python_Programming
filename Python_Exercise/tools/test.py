'''
Created on 3 Dec 2017

@author: marashid
'''

def method1():
    return False

if(__name__ == "__main__"):
    print(method1())
#     print(method2())
    
def method2():
    return True    

if ((x=1) == 2):    ## no such this as inline declaration within if statement, 
                    ## more on: https://stackoverflow.com/questions/24751423/python-flexible-inline-variable-assignment
    print()