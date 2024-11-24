import pandas

# Create dictionary in format: { "A":"Alfa", "B":"Bravo"}
phonetic_alpha_df = pandas.read_csv("./nato_phonetic_alphabet.csv")
phonetic_alpha_dict = {row.letter:row.code for (index,row) in phonetic_alpha_df.iterrows()}

# Create a list of the phonetic code words from a word the user inputs
line_breaks = "\n\n"

def generate_phonetic():
    
    user_input = input(f"{line_breaks}Enter a word you would like translated to the Nato phonetic alphabet: \n").upper()
    
    try:
        program_output = [phonetic_alpha_dict[letter] for letter in user_input]
    except KeyError:
        print("No translation available for the word you entered.")
        generate_phonetic()
    else:
        print(f"\nTranslation: {program_output}{line_breaks}")

generate_phonetic()