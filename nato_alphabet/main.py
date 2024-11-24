import pandas

# Create dictionary in format: { "A":"Alfa", "B":"Bravo"}
phonetic_alpha_df = pandas.read_csv("./nato_phonetic_alphabet.csv")
phonetic_alpha_dict = {row.letter:row.code for (index,row) in phonetic_alpha_df.iterrows()}

# Create a list of the phonetic code words from a word the user inputs
line_breaks = "\n\n"
run_program = True
while run_program:
    
    user_input = input(f"{line_breaks}Enter a word you would like translated to the Nato phonetic alphabet: \n").upper()
    # program_output = [phonetic_alpha_dict[letter] for letter in user_input if letter in phonetic_alpha_dict]

    try:
        program_output = [phonetic_alpha_dict[letter] for letter in user_input]
    except KeyError:
        program_output = []

    if len(program_output) == 0:
        print(f"\nTranslation: No translation available for the word you entered.{line_breaks}")
    else:
        print(f"\nTranslation: {program_output}{line_breaks}")
        
    user_continue = input("Would you like to translate another word? Type 'yes' or 'no': ").lower()
    if user_continue == "yes":
        run_program = True
    else:
        run_program = False