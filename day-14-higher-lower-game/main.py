# Who has more twitter followers game (A vs. B)

from higher_lower_game_data import data
from higher_lower_game_art import logo, vs
import random
from replit import clear

def get_random_account():
    return random.choice(data)

def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def play_game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
    
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(guess, account_a["follower_count"], account_b["follower_count"])

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

play_game()