# Call Stack example

def a():
    
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    
    print('b() starts')
    c()
    print('b() returns')

def c():
    
    print('c() starts')
    print('c() returns')

def d():
    
    print('d() starts')
    print('d() returns')

a()

'''
The call stack is how Python remembers where to return the execution after each function call. 
The call stack isn't stored in a variable in your program; rather, Python handles it behind the scenes. 
When your program calls a function, Python creates a frame object on the top of the call stack. 
Frame objects store the line number of the original function call so that Python can remember where to return. 
If another function call is made, Python puts another frame object on the call stack above the other one.

When a function call returns, Python removes a frame object from the top of the stack and moves the execution to the line number stored in it. 
Note that frame objects are always added and removed from the top of the stack and not from any other place.
'''