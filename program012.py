import os
os.system("cls")
investment_websites = ["1.-Motley Fool", "2.-IBD", "3.-Alpha Picks", "4.-Nates Notes", "5.-Special Situation Survey", "6.-Forbes Investor"]
for i in range(len(investment_websites)):
    print(investment_websites[i])

websites_opinions = [
    "The best for long term investments",
    "Great for growth stocks. Difficult to manage.",
    "Claim great performance, but don't like it much",
    "Don't believe in this.",
    "Value investing oriented. Does not exist anymore.",
    "Small caps oriented. Does not exist anymore."
]
favorite_website = int(input("Enter your favorite website (1-" + str(len(investment_websites)) + "): "))

if favorite_website <= len(investment_websites) and favorite_website > 0:
    print("You selected:", investment_websites[favorite_website - 1][3:])  # Skip the number and dot
    print("Opinion:", websites_opinions[favorite_website - 1])

else:
    print("Invalid selection.")


