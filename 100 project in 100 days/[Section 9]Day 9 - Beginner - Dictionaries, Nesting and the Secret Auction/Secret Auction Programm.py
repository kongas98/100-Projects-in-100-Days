from Art import logo
bidders = []
while True:
    dic = {}
    print(logo)
    print("Welcome to the S.A.P (Secret Auction Programm)")
    name = input("What is your Name?: ")
    dic["name"] = name
    bid = int(input("What is your max bid?: "))
    dic["bid"] = bid
    bidders.append(dic)
    next_bidder = input("Are the more bidders?Type yes or no: ").lower()
    if next_bidder == "no":
        break
print(bidders)
winning_bid = 0
winner = ""
for dictionary in bidders:
    for key in dictionary:
        if key == "bid":
            if dictionary[key] > winning_bid:
                winning_bid = dictionary[key]
                winner = dictionary["name"]

print(f"The winner of this S.A.P is {winner} with {winning_bid}")

