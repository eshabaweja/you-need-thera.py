# List comprehension

my_list = [1,2,3]
new_list = [(item+1) for item in my_list]
print(new_list)

name = "eshcapist"
listed_name = [letter for letter in name]
print(listed_name)

my_nums = range(1,5)
new_nums = [2*num for num in my_nums]
print(new_nums)

my_nums = range(10)
my_hashes = [num*"#" for num in my_nums if num%2!=0]
print(my_hashes)