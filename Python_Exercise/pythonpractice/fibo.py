# Fibonacci numbers module
namelist = []
str1 = "a string"
num1 = 1

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print() ## just prints a blank line
    
def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
