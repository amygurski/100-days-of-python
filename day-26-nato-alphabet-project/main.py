import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (i,row) in df.iterrows()}

print("Hi! I'll tell you the phonetic spelling of a word.")

def generate_phonetic_alphabet():
    word = input("Enter a word: ")
    try:
        nato_spelling = [nato_dict[letter.capitalize()] for letter in word]
    except KeyError:
        print("Sorry, only letters in the English alphabet please.")
        generate_phonetic_alphabet()
    else:
        print(nato_spelling)

generate_phonetic_alphabet()
