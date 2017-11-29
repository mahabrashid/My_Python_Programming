'''
Created on 9 Jan 2017

@author: marashid
'''
# import SameClassName
'''Above import will result is "TypeError: 'module' object is not callable" when instantiating the object. 
This is because the SameClassName class actually resides in module called SameClassName (i.e. class has same name as the module name).
So in order to actually import the class for instantiating, the import has to follow module_name.class_name pattern, i.e. SameClassName.SameClassName, An alternative way of importing the class is: from SameClassName import SameClassName
'''

from SameClassName import SameClassName


tstCls = SameClassName([[11, 22, 33], "a string", 9999])
print("object attributes\n", "-" * 20)
print(tstCls._list, tstCls._str, tstCls._int)
tstCls.method_one()

''' what happens when we call a class function on the object? '''
try:
    tstCls.method_two()
except Exception as e:
    print("oops! Exception raised by attempt to call a class function on an object, exception: ", e.__str__())

print("\nclass attributes\n", "-" * 20)
print(SameClassName._list, SameClassName._int, SameClassName._str)

''' what happens when we call an instance function on the class? ''' 
try: 
    SameClassName.method_one()
except Exception as e:
    print("oops! Exception raised by attempt to call an instance function on a class, exception : ", e.__str__())
    pass    # The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action
SameClassName.method_two()