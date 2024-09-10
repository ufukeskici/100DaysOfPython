import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if choice == "easy":
    attempts = 10
elif choice == "hard":
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))

    if guess > number:
        print(f"Too high")
        attempts -= 1
    elif guess < number:
        print(f"Too low")
        attempts -= 1
    else:
        print(f"You got it! The answer was {number}.")
        break

if attempts == 0:
    print(f"You've run out of guesses, you lose.")
