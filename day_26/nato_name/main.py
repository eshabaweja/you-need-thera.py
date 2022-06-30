#  Importing data from each of these data sources is provided by function with the prefix read_*. Similarly, the to_* methods are used to store data.

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas as pd
nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter : row.code for (index, row) in nato_alphabet.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
given_word = input("Enter the word: ")
word_chars = list(given_word.upper())
# print(word_chars)

nato_encoded_word = [phonetic_dict[letter] for letter in word_chars if letter in phonetic_dict]
print(nato_encoded_word)