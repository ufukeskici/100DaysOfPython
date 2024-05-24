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

#Write your code below this line 👇

import random

image = [rock, paper, scissors]

person_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
print(image[person_choice])

computer_choice = random.randint(0, 2)
print("Computer Choice:")
print(image[computer_choice])

if person_choice == computer_choice:
  print("It's a draw.")
elif person_choice == 0 and computer_choice == 1:
  print("You lose.")
elif person_choice == 0 and computer_choice == 2:
  print("You win!")
elif person_choice == 1 and computer_choice == 0:
  print("You win!")
elif person_choice == 1 and computer_choice == 2:
  print("You lose.")
elif person_choice == 2 and computer_choice == 0:
  print("You lose.")
elif person_choice == 2 and computer_choice == 1:
  print("You win.")
