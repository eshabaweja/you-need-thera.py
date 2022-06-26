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
        print("I'm a fiiish under waterrr. Glub glub glub.")

    def swim(self):
        print("Just keep swimming!")

# the object
dory = Fish()
dory.swim()
# inherited class
dory.breathe()
print(dory.num_eyes)