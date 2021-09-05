import random

rock_img = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_img = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_img = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#I'd rather this be a dictionary but doing what was covered for this section
options = ['rock', 'paper', 'scissors']
pictures = [rock_img, paper_img, scissors_img]

# Player choice
print("Let's play RPS")
player_index = int(input("What do you choose? 0 for rock, 1 for paper, 2 for scissors"))
print(pictures[player_index])

player_choice = options[player_index]

# Computer choice
computer_index = random.randint(0,2)
print(f"Computer chose:\n{pictures[computer_index]}")

computer_choice = options[computer_index]

# Determine and print winner
match = [player_choice, computer_choice]

if (player_choice == computer_choice):
  print("It's a tie!")

if ('rock' in match) and ('scissors' in match):
  if player_choice == 'rock':
    print("You win. Rock wins against scissors.")
  else:
    print("You lose. Rock wins against scissors.")

if ('scissors' in match) and ('paper' in match):
  if player_choice == 'scissors':
    print("You win. Scissors win against paper.")
  else:
    print("You lose. Scissors win against paper.")

if ('rock' in match) and ('paper' in match):
  if player_choice == 'paper':
    print("You win. Paper wins against rock.")
  else:
    print("You lose. Paper wins against rock.")
