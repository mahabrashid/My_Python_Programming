'''
Created on 9 Dec 2017

@author: marashid
'''
from macpath import dirname
'''
https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
Logging provides a set of convenience functions for simple logging usage. These are debug(), info(), warning(), error() and critical().

DEBUG    Detailed information, typically of interest only when diagnosing problems.
INFO    Confirmation that things are working as expected.
WARNING    An indication that something unexpected happened, or indicative of some problem in the near future (e.g. "disk space low"). The software is still working as expected.
ERROR    Due to a more serious problem, the software has not been able to perform some function.
CRITICAL    A serious error, indicating that the program itself may be unable to continue running.

The default level is WARNING, which means that only events of this level and above will be tracked, unless the logging package is configured to do otherwise.
'''

import logging
import sys, os

## in this module we use a MyFileHandler class in my_logging module in tools package, 
## this needs to be added to the sys.path for python to discover the module in order to import
path_to_tools_package = os.path.abspath(os.path.join(os.path.dirname(__file__), "../tools"))
# print(path_to_tools_package)
sys.path.append(path_to_tools_package)

from my_logging import MyFileHandler


def basic_logging():
    logging.warning('Watch out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything


'''
A very common situation is that of recording logging events in a file,
'''
def configued_logging_separate_dir(filepath):
    ## check if the log directory exists, if not create it
    if not os.path.exists(dirname(filepath)):
        print("file directory doesn't exist")
        os.makedirs(os.path.dirname(filepath)) # only creates the file directory, the file gets created in basicConfig function
        print("created file directory")
    
    logging.basicConfig(filename=filepath,level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    
    ## if you want a separate log file created every time, you'd use filemode='w' in basicConfig:
#     logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)


'''
logging from multiple modules
'''
def multi_mod_logging():
    import testAway ## no need to import this as not used in any other use cases and lines in the imported module get executed when imported
    logging.basicConfig(filename='myapp.log', level=logging.INFO)   ## myapp.log will be created in the current directory
    logging.info('Started')
    testAway.do_something()
    logging.info('Finished')


"""
To display the date and time of an event, you would place '%(asctime)s' in your format string
The default format for date/time display (shown above) is ISO8601. If you need more control over the formatting of the date/time, provide a datefmt argument to basicConfig
"""
def datetime_logging():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.warning('is when this event was logged.')


"""
 good convention to use when naming loggers is to use a module-level logger, in each module which uses logging,
 This means that logger names track the package/module hierarchy, and it is intuitively obvious where events are logged just from the logger name.
"""
def mod_named_logging():
    import testAway ## no need to import this as not used in any other use cases and lines in the imported module get executed when imported
    
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='mod_named.log', level=logging.INFO)   ## myapp.log will be created in the current directory
    logger.info('Started')
    testAway.do_something2()
    logger.info('Finished')


"""
idea from: https://stackoverflow.com/questions/34726515/avoid-logger-logging-getlogger-name/34789692
whole logging format is passed to basicConfig method, 
format includes: default-formatted time, module, function, line-no, log-level, 8 blank spaces, process-id and message 
"""
def evenmore_advanced_mod_named_logging():
    import testAway ## no need to import this as not used in any other use cases and lines in the imported module get executed when imported
    
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(module)s.%(funcName)s line:%(lineno)s: %(levelname)-8s [%(process)d] %(message)s')
    logging.info('Started')
    testAway.do_something3()
    logging.info('Finished')

"""
custom logging feature, pls read the doc in MyFileHandler to learn more
"""
def customized_logging(filepath=None):
#     logger = logging.getLogger()
    my_hanlder = MyFileHandler(filepath)
#     print((my_hanlder.baseFilename))
    logging.basicConfig(filename=my_hanlder.baseFilename,level=logging.DEBUG)
    
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')

# basic_logging()
# configued_logging_separate_dir("./Logs/test.log")
# multi_mod_logging()
# datetime_logging()
# mod_named_logging()
evenmore_advanced_mod_named_logging()

# customized_logging("./Logs/test.log")