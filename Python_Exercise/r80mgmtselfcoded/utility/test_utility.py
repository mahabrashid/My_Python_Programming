# from utility import util

# from utility import WebUrl
'''Above import will result is "TypeError: 'module' object is not callable" when instantiating the object. 
This is because the WebUrl class actually resides in module called WebUrl (i.e. class has same name as the module name).
So in order to actually import the class for instantiating, the import has to follow module_name.class_name pattern, i.e. WebUrl.WebUrl
'''
from utility.api import *

api_call("a command", "set of data", "some headers")