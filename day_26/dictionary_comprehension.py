# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for item in dict.items() if test}


import random

# from list
names = ["Annie", "Beth", "Belle", "Catherine", "Doug Judy", "Ntropy"]
student_score = {name : random.randint(1,100) for name in names}
print(student_score)

# from dictionary
score_dict = {'Annie': 13, 'Beth': 5, 'Belle': 23, 'Catherine': 81, 'Doug Judy': 32, 'Ntropy': 74}
passed_students = {name:score_dict[name] for name in score_dict if score_dict[name]>30}
print(passed_students)

