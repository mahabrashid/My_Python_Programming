'''
Created on 9 Jan 2017

@author: marashid
'''
'''
Purpose: this module is to act as an external scope for another __main__ module, this is to demonstrate behaviour/value of features/variables out of scope
'''
from classes_and_objects import MyObject, MyClass

print('executing module "%s" now' %__name__)

#############################################
###    used by test_classes_and_objects    ###
#############################################
def test_obj_ref(obj):
    print("object type {0} is passed as parameter".format(obj.__class__))
    if isinstance(obj, MyObject):
        print("object variable: ", obj.obj_var)
    else:
        print("The type of the object is:{0} from module:{1}".format(obj.__class__, obj.__module__), ".Following attributes are available on this object.")
        print(dir(obj))

def test_cls_ref():
    print("class variable of type {0} is : {1}".format(MyClass, MyClass.cls_var))
    

#############################################
###    used by test_logging    ###
#############################################
import logging
import inspect

def do_something():
    print("caller details: <module: {}, line: {}, function: {}>".format(inspect.stack()[1][1], inspect.stack()[1][2], inspect.stack()[1][3]))
    logging.info('Doing something')
    
def do_something2():
    logger = logging.getLogger(__name__)
    logger.info('Doing something2')
    
def do_something3():
    logging.info('Doing something3')