import random

attampt = 10
a = random.randint(1,100)


while True:
    user = int(input("enter a number to guess: "))
    attampt -=1
    
    if user>a:
        print("Lower number please")
        print(f"{attampt} attampt is remaining")

    elif user<a:
        print("higher number please")
        print(f"{attampt} attampt is remaining")

    elif user==a:
        print("you win")
        
    if attampt == 0:
        print("game over")
        print(f"the actual number was {a}")
        