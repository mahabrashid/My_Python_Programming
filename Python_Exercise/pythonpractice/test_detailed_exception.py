'''
Created on 21 Nov 2017

@author: marashid
'''
import detailed_exception
try:
    print(1/0)
except:
    detailed_exception.PrintException()