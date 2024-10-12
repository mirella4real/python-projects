
PLACEHOLDER = "[Name]"

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_template = letter_file.read()

with open("./Input/Names/invited_names.txt", mode="r") as name_file:
    names = name_file.readlines()
    names_list = []
    for name in names:
        names_list.append(name.strip('\n'))

for name in names_list:  
    letter = letter_template.replace(PLACEHOLDER, name) 
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
        new_letter.write(letter)
    
