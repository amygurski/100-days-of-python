from replit import clear
from silent_auction_art import logo

print(logo)
print("Welcome to the silent auction.")

all_bids = {}

continue_bidding = True
while continue_bidding:
    bidder = input("What is your name? ")
    bid = input("Your bid: $")
    
    all_bids[bidder] = bid

    should_continue = input("Are there more bidders? (y/n): ")
    
    clear()
    
    if should_continue == 'n':
        highest_bidder = max(all_bids, key=all_bids.get)
        print(f"The winning bidder is {highest_bidder} for ${all_bids[highest_bidder]}.")
        continue_bidding = False




