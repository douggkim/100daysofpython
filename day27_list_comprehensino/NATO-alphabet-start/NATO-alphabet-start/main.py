import pandas as pd

# TODO 0. Import the file
phonetic_pd = pd.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_pd.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Input a word : ")
output_list = [phonetic_dict[letter.upper()] for letter in user_input]
print(output_list)
