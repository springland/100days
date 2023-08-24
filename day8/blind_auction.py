from blind_auction_art import logo
import os

def format_name(first_name , last_name):
    """
    format name in last_name , first_name
    :param first_name:
    :param last_name:
    :return:
    """
    return f"{last_name},{first_name}"
has_next = True

bidders = {}
while has_next:

    print(logo)
    print("Welcome to the secret auction program. ")
    name = input("What is your name?:")
    bid = int(input("What's your bid?:")[1:])
    bidders[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other_bidders == "yes":
        has_next = True
    else:
        has_next = False
    os.system('cls')

highest_bid = -1
highest_bidder = ''
for name in bidders:
    bid = bidders[name]
    if bid > highest_bid:
        highest_bidder = name
        highest_bid = bid

print(f"The winner is {highest_bidder} with a bid of {highest_bid}")
print(format_name("ddd" , "eee"))

