# funtion to add as many numbers as the user enters
# * (asterisk) collects all the arguments into a tuple called args
# *args gives us unlimited positional arguments

# ** (double asterisk) collects all the arguments into a dictionary called kwargs 
# **kwargs gives us unlimited keyword arguments

from numpy import multiply


def add(*args):
    sum_nums = 0
    # args is a tuple. Check using type(args)
    for i in args:
        sum_nums += i
    return sum_nums

print(add(69,243,5,34,57))


def calculate(n,**kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calculate(7,add=3, multiply=5)