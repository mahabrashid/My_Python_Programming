'''
Created on 9 Jan 2017

@author: marashid
'''
from classes_and_objects import MyObject, MyClass

print('executing module "%s" now' %__name__)

def test_obj_ref(obj):
    print("object type {0} is passed as parameter".format(obj.__class__))
    if isinstance(obj, MyObject):
        print("object variable: ", obj.obj_var)
    else:
        print("The type of the object is:{0} from module:{1}".format(obj.__class__, obj.__module__), ".Following attributes are available on this object.")
        print(dir(obj))

def test_cls_ref():
    print("class variable of type {0} is : {1}".format(MyClass, MyClass.cls_var))