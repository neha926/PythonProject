import random

easy_words=["cat", "cup","run","fun","pen","rain","camel"]
medium_words=["bottle","mobile","tablet","tiger","team","book"]
hard_words=["crocodile","dinasours","human","computer","technical","coding"]


print('Welcome To uessing Game : ')
print('Choose Level For Playing Game (easy,hard,medium): ')
level=input("Enter Difficulty : ").lower()

if level=="easy":
    secret=random.choice(easy_words)
elif level=="medium":
    secret=random.choice(medium_words)
elif level=="hard":
    secret=random.choice(hard_words)
else:
    print("Invalid Level For Your Begining I'll suggest by default easy" )
    secret=random.choice(easy_words)


tries=0
print('Guess The Secret Password ')
while True:
    guess=input("Enter word : ")
    tries+=1

    if guess==secret:
        print(f"Congrats in attempts : {tries}")
        break
    

    hint=""
    for i in range(len(secret)):
        if i<len(guess) and guess[i]==secret[i]:
            hint+=guess[i]
        else:
            hint+="_"
    print("Hint : ", hint)
print('Game Over')


