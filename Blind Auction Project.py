# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)

def highest_bidder(bid):
    winner=""
    highest_bid = 0
    for bidder in bid:
        bid_price = bid[bidder]
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
bids={}
continue_bidding=True
while continue_bidding:
    name = input("What is your name?: ")
    price = float(input("What is your price?: $"))
    bids[name] = price
    ask = input("Are ther any other bidders?Type 'yes' or 'no':").lower()
    if ask == "no":
        continue_bidding=False
        highest_bidder(bids)
    elif ask == "yes":
        print("\n"*100)
