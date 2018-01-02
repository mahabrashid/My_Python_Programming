'''
Created on 16 Dec 2017

@author: marashid
'''
import os, sys, linecache

''' list all files with fullpath in directory and subdirectory recursively
'''
def list_out_content(pathstr):
    try:
        if os.path.isfile(pathstr):
            print("file: " + os.path.normpath(pathstr))
            
        if os.path.isdir(pathstr):
            for filename in os.listdir(pathstr):
                list_out_content(os.path.join(pathstr, filename) )
    
    except FileNotFoundError as fnferr:
        print(fnferr.strerror)
    except Exception as exp:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

''' list all files with fullpath in directory and subdirectory without recursion, using os.walk method
'''        
def easy_listing(pathstr):
    for dir, subdirs, files in os.walk(pathstr):
        print("="*20)
        print("dir: " + dir.__str__())
        print("subdirs: " + subdirs.__str__())
        print("files is {}: {}".format(dir, files.__str__()))
        for file in files:
            filepath = os.path.join(dir, file)
#             filepath = dir + os.sep + file
            print("file in {}: {}".format(dir, filepath))

''' list all files without path, i.e. filenames only, in directory and subdirectory recursively
'''
def list_filenames_only(pathstr):
    try:
        if os.path.isfile(pathstr):
            print("file: " + os.path.basename(pathstr))
            
        if os.path.isdir(pathstr):
            for filename in os.listdir(pathstr):
                list_out_content(os.path.join(pathstr, filename) )
    
    except FileNotFoundError as fnferr:
        print(fnferr.strerror)
    except Exception as exp:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

# list_out_content("./test files")
# easy_listing("./test files")
list_filenames_only("./test files")