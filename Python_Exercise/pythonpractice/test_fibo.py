import fibo

print("dir(): {0} \nand _name_: {1}".format(dir(fibo), (fibo.__name__))) ## built-in function dir() is used to find out which names a module defines and __name__ will print 'fibo'

print("-"*10)
fibo.fib(1000)

print("-"*10)
fibo.fib2(100) ## only gets the return value from fib2 function, doesn't print them on console

print("-"*10)
### If you intend to use a function often you can assign it to a local name:
fib = fibo.fib2
print("fib:", fib(500))
input("press any key to exit...")