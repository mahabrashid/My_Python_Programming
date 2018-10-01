'''
Created on 8 Nov 2017
@author: marashid

In the book Learning Python by Mark Lutz, he suggests the following mnenomic for remember how Python scoping works: LEGB

Going from the narrowest scope to the widest scope:

L stands for "Local". It refers to variables that are defined in the local scope of functions.
E stands for "Enclosing". It refers to variables defined in the local scope of functions wrapping other functions.
G stands for "Global". These are the variables defined at the top level of files and modules.
B stands for "Built in". These are the names that are loaded into scope when the interpreter starts up. You can look at them here: https://docs.python.org/3.5/library/functions.html
'''
var = "value assigned in module or global level"   # var declared at module-level, aka global level

def errorsome_func():
    print("var in errorsome_func: ", var) # this will generally print the module-level var unless there's another var referenced somewhere in this scope of errorsome_func
    ## the above print stmt will result in below error if the following code block is activated
    ## UnboundLocalError: local variable 'var' referenced before assignment
#     if(var is None):
#         var = "value assigned in errorsome_func"
    print("-"*10)

def shadowing_var():
    var = "value assigned in shadowing_var" # this will create a local-level var shadowing the module-level var, i.e. glboal var
    print("var in shadowing_var: ", var)
    print("-"*10)
    
def accessing_global_var():
    global var  # global keyword is required to refer to the module-level, i.e. global var
    var = "value assigned in accessing_global_var" # this will modify the value of the global var
    print("-"*10)

def checking_modified_var_in_other_func():
    print("testing module-level var after it's modified in another method: ", var)
    print("-"*10)

# errorsome_func()    
# shadowing_var()
#  
# print("module-level var before modifying in the method: ", var)
# accessing_global_var() # let's modify the global var here
# print("module-level var after modifying in the method: ", var)
# print("-"*10)
#  
# checking_modified_var_in_other_func()    # let's check what the global var is now


'''
this function demonstrates the dominance of local declaration of a variable over global declaration
'''
def var_in_nested_func():
    def func_lvl1():
        var = "value assigned in func_lvl1" # this will create a local-level var shadowing the module-level var, i.e. glboal var
        
        def func_lvl2():
            var = "value assigned in func_lvl2"            
            
            def func_lvl3():
                print("var in nested func_lvl3: {}, here we didn't declare a var".format(var))
        
            print("calling func_lvl3...")
            func_lvl3()
            print("var in nested func_lvl2: {}, here we declared a local var".format(var))
            
        print("calling func_lvl2...")
        func_lvl2()
        print("var in nested func_lvl1: {}, here we declared a local var".format(var))
            
    print("calling func_lvl1...")
    func_lvl1()    
    print("-"*10)

'''
this function demonstrates how a local declaration of a variable in enclosing function can be modified in nested function
''' 
def changing_var_declared_in_enclosing_func():
    def func_lvl1():
        var = "value assigned in func_lvl1"
        
        def func_lvl2():
            nonlocal var    # nonlocal keyword is required to refer to the var declared in the enclosing scope, i.e. the func_lvl1
            var = "value assigned in func_lvl2" # this modifies the var in func_lvl1
            
            def func_lvl3():
                var = "value assigned in func_lvl3" # this is just a local declaration of var and doesn't change var on uppper levels
                print("var in nested fun func_lvl3: {}, here we declared a local var".format(var))
        
            print("calling func_lvl3...")
            func_lvl3()
            print("var in nested func_lvl2: {}, here we changed lvl1 value using nonlocal keyword".format(var))
            
        print("calling func_lvl2...")
        func_lvl2()
        print("var in nested func_lvl1: {}, here we declared a local var which changed in lv2 using nonlocal keyword".format(var))
        
    print("calling func_lvl1...")
    func_lvl1()    
    print("-"*10)

# print("Check out the local declaration behaviour in nested functions:")
# var_in_nested_func()
# 
# print("Finally, check out the nonlocal declaration behaviour in nested functions:")
# changing_var_declared_in_enclosing_func()