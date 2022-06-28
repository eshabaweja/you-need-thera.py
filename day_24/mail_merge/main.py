#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp

#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp

#Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# reading the reference letter
reference = open("./Input/Letters/starting_letter.txt","r")
ref_letter = reference.read()
# print(ref_letter)

# listing out the names
name_file = open("./Input/Names/invited_names.txt","r")
name_list = name_file.readlines()
# print(name_list)

# replacing names in letter
for name in name_list:
    name = name.strip()
    new_letter = ref_letter.replace("[name]", name)
    # print(new_letter)

# saving the letters in files by their name
    invite = open(f"./Output/ReadyToSend/{name}_invite.txt","w")
    invite.write(new_letter)
    invite.close()