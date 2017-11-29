'''
Created on 9 Jan 2017

@author: marashid
'''
from classes_and_objects import *

print("-"*20, "Class Attributes", "-"*20)
print("initial value: ", MyClass.cls_var)
MyClass.cls_var = "new class variable" ## new variables are visible in other modules after reassignment 
print("value after reassignment: ", MyClass.cls_var)

print("function call: ", MyClass.cls_func())

print("function object before reassignment: ", MyClass.cls_func)
MyClass.cls_func = "some random text" ## you can even temper with the Class's function object, same should be true for an object's method object
print("function object after reassignment: ", MyClass.cls_func)


print("-"*20, "Object Attributes", "-"*20)
obj = MyObject("object variable")
print(obj.obj_var)

print(obj.obj_mthd1()) ## prints the return value from the method call which is 'None'
print(obj.obj_mthd2())
print("-"*50)

## Now we want to see if the MyClass and obj attributes are available in other modules
import testAway
testAway.test_obj_ref(obj)
testAway.test_cls_ref()