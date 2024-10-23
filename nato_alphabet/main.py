import pandas

# TODO 1. Create dictionary in format: { "A":"Alfa", "B":"Bravo"}

phonetic_alpha_df = pandas.read_csv("./nato_phonetic_alphabet.csv")
phonetic_alpha_dict = {row.letter:row.code for (index,row) in phonetic_alpha_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word the user inputs
line_breaks = "\n\n\n\n\n"
user_input = input(f"{line_breaks}Enter a word you would like translated to the Nato phonetic alphabet: \n").upper()
program_output = [phonetic_alpha_dict[letter] for letter in user_input if letter in phonetic_alpha_dict]
print(f"\nTranslation: {program_output}{line_breaks}")