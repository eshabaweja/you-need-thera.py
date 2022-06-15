# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_heights = 0
count = 0
for i in student_heights:
    sum_heights+=i
    count+=1

avg = sum_heights/count

print(f"Average height is {round(avg)} units.")