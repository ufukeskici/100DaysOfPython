import random
import os
from art import logo, vs
from game_data import data

game_over = False
final_score = 0

while game_over == False:
    number_a = random.randint(0, len(data)-1)
    number_b = random.randint(0, len(data))-1
    
    if number_a == number_b:
        continue
    else:
        print(logo)
        if final_score  > 0:
            print(f"You're right! Current score: {final_score}")

        print(f"Compare A: {data[number_a]['name']}, a {data[number_a]['description']}, from {data[number_a]['country']}")
        print(vs)
        print(f"Compare B: {data[number_b]['name']}, a {data[number_b]['description']}, from {data[number_b]['country']} \n")
        
        answer = input("Who has more followers? Type 'A' or 'B':")

        if answer == 'A':
            if data[number_a]['follower_count'] > data[number_b]['follower_count']:
                final_score += 1
                os.system('clear')
            else:
                game_over = True
                break

        elif answer == 'B':
            if data[number_b]['follower_count'] > data[number_a]['follower_count']:
                final_score += 1
                os.system('clear')
            else:
                game_over = True
                break

os.system('clear')
print(logo)
print(f"Sorry, that's wrong. Final score: {final_score}")
