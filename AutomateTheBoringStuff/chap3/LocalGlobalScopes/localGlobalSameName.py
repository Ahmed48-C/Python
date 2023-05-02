# Local and Global Variables with the Same Name
# Technically, it’s perfectly acceptable to use the same variable name for a global variable and 
# local variables in different scopes in Python. 
# But, to simplify your life, avoid doing this:

def spam():
    eggs = 'spam local'
    print(eggs)    # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs)    # prints 'bacon local'
    spam()
    print(eggs)    # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs)        # prints 'global'

# Since these three separate variables all have the same name, 
# it can be confusing to keep track of which one is being used at any given time. 
# This is why you should avoid using the same variable name in different scopes.
