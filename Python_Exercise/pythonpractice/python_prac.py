### Run using Python 3.6
'''
### Standard Code Layout and Naming Convention
1.	Python PEP8 code standard site: https://www.python.org/dev/peps/pep-0008/
2.	4 spaces to indicate one level of indentation, don't use tab characters
3.	A single line of code should not exceed 17-19 characters
4.	Import statements should be at the top of the module
5.	Standard libraries should be imported first, then third party modules and import from other modules in the same project
6.	There should be a blank line between each group of imports
7.	Classes and Functions at the top level can have 2 blank lines between them
8.	Methods within a Class should have 1 blank line separating them
9.	Within a method, blank lines should be inserted to separate conceptual grouping of code
10.	Don't insert extra space before parenthesis, brackets or braces
11.	Don't insert space before commas and colons
12.	Always put a single space on either sides of binary operators
13.	Don't put more than 1 statement on the same line
14.	Comments should be in human language
15.	Comment should precede every section of code describing the code and be indented at the code level
16.	Every public module, class, or method should have a properly formatted doc string
17.	Objects are named according how they are used, for example a Factory function should be named as if it were a class because the usage case is the same as it were a class
18.	Packages and modules have to have short names and lowercase letters
19.	Module names have leading and trailing double underscores
20.	Class names are CamelCased starting with a Capital letter
21.	Exception are classes so should follow naming convention for Classes but the last word in the name should be Err.
22.	Functions or methods, instance variables and global variables should all be lowercased with underscore separating words
23.	Private (internal) methods or variable should begin with a single underscore
24.	The first parameter of an instance method should always be named self
25.	Constants to be written in all capital letters with underscore separating words
'''

'''
### Declaration of docstrings
"""
Assuming this is file mymodule.py, then this string, being the
first statement in the file, will become the "mymodule" module's
docstring when the file is imported.
"""
 
class MyClass(object):
    """The class's docstring"""
 
    def my_method(self):
        """The method's docstring"""
 
def my_function():
    """The function's docstring
    which can even be
    across multiple lines if need to be
    """
'''

'''
### some observations:
1. Python will let you assign a variable to a method call that doesn't return. This will return a None value which is assigned to the variable. This wouldn't be possible in java, a call to a method with return type "void" wouldn't be allowed to be assigned to a variable.
'''

### List ###
'''
a = [11,22,33,44,55,66,77,88]
b = ['|||']
# print(b * 4 #print result multiplying the list 4 times, will output ['|||', '|||', '|||', '|||'])
# print(a[2 : 4]) #print from item2 to item4(excluding 4th) in the list a, will output [33, 44])
# print(a[0 : len(a)] #print from first to the last item in list a)
# print(a[-1] #print the last item in the list)
# print(a[-2] #print the 2nd to last item in the list)
# print(a[0:4:2] #print from element 0 to 4 with step 2, will output [11, 33])
# print(a[::2] #print from first to last with step 2, will output [11, 33, 55, 77]. Default params inside the [] are first_element:last_element:step_1)
'''


### Tuple ###
'''
red = (255, 0, 0)
print(red[2])
for r in red:
	print(r)
'''


### Range ###
'''
 for r in range(0,11,2):
	 print(r)
'''


### String fomatting ###
'''
str = "hello World!"
print str[0:5] #print from 0 to 4th characters from str
print str[::2] #print from start to end of the string with character step 2
print str[1] #print character 1 in the string
'''


### if statements ###
'''
 if(2==1):
	 print("if executed")
 elif(2==3):
	 print("elif exucuted")
 else:
	 print("else exucuted")

 if(2==1) and (3==3) :
	 print("if executed")
 else:
	 print("else executed")

 if(2!=1) and not (3!=3) :
	 print("if executed")
 else:
	 print("else executed")

 if(2==1) or (3==3) :
	 print("if executed")
 else:
	 print("else executed")
'''

### while statement ###
'''
 count = 0
 target = 10
 while (count < target):
	 count = count + 1	
	 if(count==5):
		 print("halfway there!")
		 continue
	 print('The count is:', count)
	 if(count==9):
		 print('target achieved')
		 break
 else:
	 print('count is out of bound')
'''

	
### Print prime number in a range - it's a weak program as it breaks when range(1,10) ###
'''
for n in range(2, 10):
	print('n: ', n)
	for x in range(2, n):
		print('x: ', x)
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		#loop fell through without finding a factor
		print(n, 'is a prime number')
'''


### Print complex data type ###
'''
from pprint import pprint
print([{1:2, 3:4}, {5:6, 7:list(range(25))}])
pprint([{1:2, 3:4}, {5:6, 7:list(range(25)), 3:4}]) ##pprint provides a capability to pretty-print arbitrary Python data structures in a form which can be used as input to the interpreter. Dictionaries are sorted by key before the display is computed.
'''

### Classes ###
## Example from the tutorial
'''
class MyClass:
    """A simple example class"""
    i = 12345

    def f():
        return 'hello world'

print(dir(__name__))
print(MyClass.i)
print(MyClass.f())
'''


### package ###
## Module's parent package is not recognised for import statement
# import pythonpractice #will result in ModuleNotFoundError: No module named 'pythonpractice'

## however you can import other modules within the same parent package without the parent package namespace
'''
import classes_and_objects
print(dir(classes_and_objects))
'''


### Text-mode interactivity ###
'''
print("hello world")
name = input("name: ") #input() is a built-in function
print("hello", name)

from getpass import getpass
import pprint
password = getpass("Please enter your password: ")
print("The password you typed is: {0}".format(password))
'''