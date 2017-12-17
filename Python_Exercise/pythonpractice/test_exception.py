'''
Created on 21 Nov 2017

@author: marashid
'''
import linecache
import sys

def print_detailed_exception():
    print(sys.exc_info())
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))
    
def raise_user_defined_exception():
    try:
        print("raising exception now...")
        raise RuntimeError("raised a custom exception")
    except RuntimeError as rterr:
        print(rterr.__str__())
        
# try:
#     print(1/0)
# except:
#     PrintException()

raise_user_defined_exception()