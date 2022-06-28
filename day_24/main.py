# https://docs.python.org/3/library/functions.html#open

file_1 = open("my_file.txt")
contents = file_1.read()
print(contents)
file_1.close()

# In python the with keyword is used when working with unmanaged resources (like file streams). It is similar to the using statement in VB.NET and C#. It allows you to ensure that a resource is "cleaned up" when the code that uses it finishes running, even if exceptions are thrown.

# tl;dr if you don't wanna write file.close(), open using with keyword
with open("song.txt") as song:
    lyrics = song.read()
    print(lyrics)


# writing to a file
# open in write mode
# write truncates the file
file_2 = open("my_file.txt", mode="w")
file_2.write("New text.")
file_2.close()

# appending by opening in append mode
# append adds to the file
file_3 = open("my_file.txt",mode="a")
file_3.write("\nAppended text.")
file_3.close()


# if doesn't exist, 'w' or 'a' create the file
# open in write mode
file_4 = open("new_file.txt", mode="w")
file_4.write("This file was created by python.")
file_4.close()

file_5 = open("new_appended_file.txt", mode="a")
file_5.write("This file was created and appended by python.")
file_5.close()
