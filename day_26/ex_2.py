# list comprehension to select only even numbers from list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

result = [num for num in numbers if num%2==0]

print(result)
