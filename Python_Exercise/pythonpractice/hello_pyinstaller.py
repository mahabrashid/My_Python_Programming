'''
Created on 28 Nov 2017

@author: marashid
'''
import os, sys
import logging

input("started hello_pyinstaller, press any key to continue...")

import testAway
input("imported testAway, press any key to continue...")

## in this module we use a MyFileHandler class in my_logging module in tools package, 
## this needs to be added to the sys.path for python to discover the module in order to import
# path_to_tools_package = os.path.abspath(os.path.join(os.path.dirname(__file__), "../tools"))
'''
However, while the above statement works fine in normal circumstances, if the program is run from a different location, such as with from a pyinstaller exe 
in a designated directory, it will look for ../tools/ directory relative to that location and the program will fails without much useful message. 
To avoid this issue, a relative or absolute path to "../tools" should be given to the 'pathex=' list for pyinstaller to look to resolve the import. 
Another useful method is to check if code is running from a bundle using following technique
'''
if getattr(sys, 'frozen', False):    # running in a pyinstaller bundle, so
    bundle_dir = sys._MEIPASS
    print("bundle_dir: " + bundle_dir)
else: # running live from the python module
    path_to_tools_package = os.path.abspath(os.path.join(os.path.dirname(__file__), "../tools"))
#     print(path_to_tools_package)
    sys.path.append(path_to_tools_package)

from my_logging import MyFileHandler
  
my_hanlder = MyFileHandler()
logging.basicConfig(filename=my_hanlder.baseFilename, level=logging.DEBUG,
                        format='%(asctime)s %(module)s.%(funcName)s line:%(lineno)s: %(levelname)-8s [%(process)d] %(message)s')
      
logging.debug('Program started')
logging.error('calling foreign module...')
testAway.do_something4()
logging.warning('Program finished')
  
  
name = input("Please say your name: ")
logging.info("hello {}, nice to meet you!".format(name))
input("press any key to exit...")