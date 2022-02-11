# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
name_list = []
with open("./Input/Names/invited_names.txt", mode="r+") as file:
    for line in file:
        name_list.append(line.strip())

for name in name_list:
    with open("./Input/Letters/starting_letter.txt", mode="r+") as file:
        for line in file:
            new_line = line.replace("[name]", name)
            with open(f"./Output/{name}.txt", "a+") as result_file:
                result_file.write(new_line)
                print(result_file.read())
