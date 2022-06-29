# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

# You are going to create a list called result which contains the numbers that are common in both files.

file1 = open("file1.txt")
file2 = open("file2.txt")

arr1 = file1.readlines()
arr2 = file2.readlines()

result = [int(item) for item in arr1 if item in arr2]

print(result)
