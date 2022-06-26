# Class Inheritance

A class can inherit properties as well as behavior from another class ["super class"].


Inheritance allows us to define a class that inherits all the *methods and properties* from another class.

- **Parent class** is the class being inherited from, also called base class.

- **Child class** is the class that inherits from another class, also called derived class.


```
Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function.

```

```python
# the parent class
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
class Fish(Animal):

    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("under waterrr. Glub glub glub.")

    def swim(self):
        print("Just keep swimming!")

# the object
dory = Fish()
dory.swim()
# inherited class
dory.breathe()
print(dory.num_eyes)

```