import pandas

# TODO 1. Create dictionary in format: { "A":"Alfa", "B":"Bravo"}

phonetic_alpha_df = pandas.read_csv("./nato_phonetic_alphabet.csv")
phonetic_alpha_dict = {row[0]:row[1] for (index,row) in phonetic_alpha_df.iterrows()}
print(phonetic_alpha_dict)

# TODO 2. Create a list of the phonetic code words from a word the user inputs
