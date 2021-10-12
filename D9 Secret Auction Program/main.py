from replit import clear

# HINT: You can call clear() to clear the output in the console.


dic = {}
gaming = 1

while gaming:
    name = input("What's your name?: ")
    bid = input("How much do you want to bid? $")
    check_bidder = input("Is there other bidder? Type 'Yes' or 'No'.: ").lower()
    dic[name] = bid

    if check_bidder == "yes":
        clear()
    else:
        clear()
        highest_bid = 0
        winner = ""
        for member in dic:
            bid = int(dic[member])
            if bid >= highest_bid:
                highest_bid = bid
                winner = member
                gaming = 0
        print(f"The winner is {winner} with a bid of {highest_bid}")
