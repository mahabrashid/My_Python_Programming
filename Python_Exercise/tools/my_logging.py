'''
Created on 10 Dec 2017

@author: marashid
'''
import inspect
import os

import logging
from logging import FileHandler


class MyFileHandler(FileHandler):  # # inherit from logging.FileHandler
    """
    MyFileHandler is a sub-class of logging.FileHandler which introduces some extra features in addition to what's in FileHandler class.
    
    Added features:
        + provided directory structure check and create one if doesn't exist for user given log file, by default code will fail if directory didn't exist
        + added option to create log file by the name of the module that calls it, this executes if no parameter for a log file is given
    """
    def __init__(self, filepath=None):  
        # if file didn't exist while directory structure does, then the file creation will be handled by the logging module
        # however, if the directory structure doesn't exist, an exception is thrown instead.
        # so if a filepath is given, we want to make sure the directory structure exists to avoid exception
        if((filepath is not None) and (not os.path.exists(os.path.dirname(filepath)))):  # # if a filepath parameter is passed and it doesn't exist, then create the directory structure (ONLY)
#             print("filepath doesn't exist, parent dir of the path: " + dirname(os.path.abspath(filepath)))
            os.makedirs(os.path.dirname(filepath))
            print("created logs directory")
        elif((filepath is not None) and (os.path.exists(os.path.dirname(filepath)))):
            pass ## do nothing
        else:  # # otherwise set the name of the log by the name of the module that called the logger
            fullpath_of_caller_module = inspect.stack()[1][1]
            caller_module_name = fullpath_of_caller_module.split(os.path.sep).pop()
            if(not os.path.exists(os.path.dirname("./Logs/"))):
                os.makedirs(os.path.dirname("./Logs/"))
                print("created logs directory")
            filepath = os.path.join("./Logs/", caller_module_name + ".log")
        
        print("path to log file: " + filepath)
        # # finally call the FileHandler super constructor
        FileHandler.__init__(self, filepath)