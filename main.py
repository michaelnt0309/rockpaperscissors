rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

rps = [rock, paper, scissors]

computer_random = random.randint(0, 2)
computer = rps[computer_random]

print("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors")
user_choice = int(input())
user = rps[user_choice]
print(user)
print("Computer chose:")
print(computer)

if user == rock:
    if computer == rock:
        print("It's a tie!")
    elif computer == paper:
        print("You lose!")
    else:
        print("You win!")
      
if user == paper:
    if computer == rock:
        print("You win!")
    elif computer == paper:
        print("It's a tie!")
    else:
        print("You lose!")
      
if user == scissors:
    if computer == rock:
        print("You lose!")
    elif computer == paper:
        print("You win!")
    else:
        print("It's a tie!")
