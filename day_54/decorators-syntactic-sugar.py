## Python Decorators

# A decorator is a function that takes a function as its only parameter and returns a function. 
# This is helpful to “wrap” functionality with the same code over and over again. 

# Adds a welcome message to the string
# returned by fun(). Takes fun() as
# parameter and returns welcome().
def decorate_message(fun):
  
    # Nested function
    def wrapper_function(site_name):
        return "Welcome to " + fun(site_name)
  
    # Decorator returns a function
    return wrapper_function
  
# We use @func_name to specify a decorator to be applied on another function below it.

@decorate_message
def site(site_name):
    return site_name;
 
# Driver code
  
# This call is equivalent to call to
# decorate_message() with function
# site("Eshcapist") as parameter
print(site("Eshcapist"))