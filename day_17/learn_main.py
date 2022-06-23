# use PascalCase for classes

class User:
    pass # use this if you wanna leave the class empty

user_1 = User()

# adding attributes to the object (not class)

user_1.id = "001"
user_1.username = "eshcapist"

print(user_1.username)

###########################################################

class Student:

# __init__ is used to create the constructor which gets called every time an object is created
# self keyword
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("New user being created.")
        print(f"Name = {self.name}\tMarks = {self.marks}")

stu_1 = Student("ennnnn",69)

###########################################################

class Insta:
    def __init__(self, user_id):
        self.user_id = user_id
        self.followers = 0  # default value
        self.following = 0  # default value

insta_1 = Insta("rezonanceindia")
insta_1.followers = 55
print(insta_1.user_id)
print(insta_1.followers)
print(insta_1.following)
