from silent_auction_art import logo
import os

print(logo)
print("Welcome to the silent auction.")

bidders = {}

continue_bidding = True
while(continue_bidding):
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    more_bidders = input("Are there anymore bidders? Type 'yes' or 'no'.\n").lower()
    os.system('clear')
    if more_bidders == "no":
        continue_bidding = False
        highest_bid = 0
        winner = ""
        for bidder in bidders:
            bid_amount = bidders[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}.")
