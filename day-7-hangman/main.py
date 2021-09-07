import random
import hangman_art
from hangman_words import word_list

print(hangman_art.logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
game_over = False
lives = 6

for _ in range(word_length):
    display += "_"

# print(chosen_word) #for testing

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for i in range(word_length):
        letter = chosen_word[i]
        if guess == letter:
            display[i] = letter

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"You lose.\nThe word was {chosen_word}.")

    if "_" not in display:
        game_over = True
        print("You win!")

    print(hangman_art.stages[lives])
