'''
Created on 21 Nov 2017

@author: marashid
'''
import linecache
import sys

def PrintException():
    print(sys.exc_info())
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))
    
try:
    print(1/0)
except:
    PrintException()