import random
x=random.randint(1, 100)
#x=45
print("Firstly, I'm thinking of a number between 1 and 100. Can you guess what it is?")
direction = ""
guess = 0
attempts = 0

while True:
    try:
        guess = int(input("What's your guess? "))
    except:
        print("Please enter an integer")
        continue
    if guess < 1 or guess > 100:
        print("Please pick a number between 1 and 100 ")
        continue
    attempts = attempts +1
    break
while guess != x:
    if guess < x:
        print("Nope, too low")
    else:
        print("Nope, too high")
    attempts = attempts +1
    while True:
        try:
            guess = int(input("What's your guess? "))
        except:
            print("Please enter an integer")
            continue
        if guess < 1 or guess > 100:
            print("Please pick a number between 1 and 100 ")
            continue
        break
print("Correct! You guessed the correct number in only ", attempts, " tries!\nThank you for playing!", sep="")
input()