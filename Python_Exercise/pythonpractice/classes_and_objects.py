'''
Standard Code Layout and Naming Convention
--------------------------------------------
Classes and Functions at the top level can have 2 blank lines between them
Methods within a Class should have 1 blank line separating them
Functions or methods, instance variables and global variables should all be lowercased with underscore separating words
'''
class MyClass:
    cls_var = "Class Variable" ## this variable can be accessed ONLY in an instance method, i.e. method with self param with self. prefix
    

    def cls_func():
        return "Class function"
    
    def cls_func2():
        return "Class function 2"
    
    def test(self):
        print(self.cls_var)
    
## mainly a class function do not require to have a 'self' param while an object method does

class MyObject:
    obj_var = ''
    
    
    def __init__(self, param):
        self.obj_var = param
    
    def obj_mthd1(self):
        print("Object method1")
        
    def obj_mthd2(self):
        return "Object method2"