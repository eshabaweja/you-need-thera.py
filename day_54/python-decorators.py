# operations offered
def add(n1, n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

# In computer science, a programming language is said to support first-class functions (or function literal) if it treats functions as first-class objects. Specifically, this means that the language supports constructing new functions during the execution of a program, storing them in data structures, 
# passing them as arguments to other functions, and returning them as the values of other functions.
# functions can be returned from other functions

def calculate(calc_func):
    return calc_func

# returning a function
adding = calculate(add)
print(adding)
# calling the returned function
print(adding(6,9))