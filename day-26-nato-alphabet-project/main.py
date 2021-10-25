import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (i,row) in df.iterrows()}

print("Hi! I'll tell you the phonetic spelling of a word.")
word = input("Enter a word: ")

nato_spelling = [nato_dict[letter.capitalize()] for letter in word]

print(nato_spelling)