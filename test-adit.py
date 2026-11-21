import random

num = random.randint(1, 1000)

if num <= 6:
    print("Jackpot!!")
elif num <= 57:
    print("4 star")
else:
    print("Loseer")