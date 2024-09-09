############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import os
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_card(list):
    list.append(random.choice(cards))

def calculate_score(list1, list2):
    if sum(list1) > sum(list2):
        print_final()
        print("You win \U0001F603")
    elif sum(list1) < sum(list2):
        print_final()
        print("You lose \U0001F624")
    elif sum(list1) ==sum(list2):
        print_final()
        print("Draw \U0001F643") 

def change_ace(list):
    index = list.index(11)
    list[index] = 1
    return list

def print_cards():
    print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"    Computer's first card: {computer_cards[0]}")

def print_final():
    print(f"   Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"   Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

game_over = False

while game_over == False:
    
    user_cards = []
    computer_cards = []

    users_turn = True
    computers_turn = True
    calculation = True

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        os.system('clear')
        print(logo)

        for i in range(0, 2):
            get_card(user_cards)
            get_card(computer_cards)

        print_cards()

        if sum(user_cards) == 21 and sum(user_cards) > sum(computer_cards):
            print_final()
            print("Win with a Blackjack \U0001F60E")
        elif sum(computer_cards) == 21 and sum(computer_cards) > sum(user_cards):
            print_final()
            print("Lose, opponent has Blackjack \U0001F631")
        elif sum(computer_cards) == 21 and sum(computer_cards) == 21:
            print_final()
            print("Draw \U0001F643")
        else:
            while users_turn == True:
                if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                    get_card(user_cards)
                    print_cards()

                    if sum(user_cards) > 21:
                        if 11 in user_cards:
                            user_cards = change_ace(user_cards)
                        else:
                            user_cards = user_cards

                    if sum(user_cards) > 21:
                        # print_cards()
                        print_final()
                        print("You went over. You lose \U0001F62D")
                        users_turn = False
                        computers_turn = False
                        calculation = False
                else:
                    users_turn = False

            while computers_turn == True:
                if sum(computer_cards) < 17:
                    get_card(computer_cards)

                if sum(computer_cards) > 21:
                        if 11 in computer_cards:
                            computer_cards = change_ace(computer_cards)
                        else:
                            computer_cards = computer_cards

                if sum(computer_cards) > 21:
                    print_final()
                    print("Opponent went over. You win \U0001F604")
                    computers_turn = False
                    calculation = False
                
                if sum(computer_cards) >= 17 and sum(computer_cards) <= 21:
                    computers_turn = False
            
            if calculation == True:
                calculate_score(user_cards, computer_cards)
    else:
        game_over = True
