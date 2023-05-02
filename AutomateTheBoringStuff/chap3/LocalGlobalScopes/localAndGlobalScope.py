# Parameters and variables that are assigned in a called function are said to exist in that function’s local scope. 
# Variables that are assigned outside all functions are said to exist in the global scope.

# Scopes matter for several reasons:
# 1) Code in the global scope, outside of all functions, cannot use any local variables.
# 2) However, code in a local scope can access global variables.
# 3) Code in a function’s local scope cannot use variables in any other local scope.
# 4) You can use the same name for different variables if they are in different scopes. That is, there can be a local variable named spam and a global variable also named spam.


# Local Scopes Cannot Use Variables in Other Local Scope
# A new local scope is created whenever a function is called, including when a function is called from another function. 
# Consider this program:
'''
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()
'''

# Global Variables Can Be Read from a Local Scope
# Consider the following program:
'''
def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
'''