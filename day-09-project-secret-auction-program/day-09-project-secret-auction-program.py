# You can call clear() to clear the output in the console.
import os
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bidder_dict = {}

def add_bidder(name, bid):
    bidder_dict[name] = bid

def calculate_bid(bidder_dict):
    highest_score = 0
    winner = ""
    for key in bidder_dict:
        if bidder_dict[key] >= highest_score:
            highest_score = bidder_dict[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_score}.")

other_bidders = "yes"
while other_bidders == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    add_bidder(name, bid)
    
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    os.system('clear')
    if other_bidders == "no":
        calculate_bid(bidder_dict)