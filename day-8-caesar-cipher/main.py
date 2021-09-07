import string
from cipher_art import logo

print(logo)

def caesar(text,shift,direction):
    result = ""
    for i in range(len(text)):
        if text[i] not in string.ascii_lowercase:
            result += text[i]
        else:
            # ASCII codes for lowercase letters are 97-122
            if direction == "decode":
                result += chr((ord(text[i]) - shift - 97) % 26 + 97)
            else: #encode
                result += chr((ord(text[i]) + shift - 97) % 26 + 97)
    print(f"The decoded text is {result}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    response = input("Do you want to continue? (yes/no)\n").lower()
    if response == "no":
        should_continue = False
        print("Goodbye!")


