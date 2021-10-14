PLACEHOLDER = "[name]"

# Read in names
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Read in starting letter
with open("Input/Letters/starting_letter.txt", "r") as starting_file:
    letter = starting_file.read()
    for name in names:
        new_letter = letter.replace(PLACEHOLDER,name.strip())
        with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as output_file:
            output_file.write(new_letter)
