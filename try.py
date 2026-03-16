import random

attampt = 10
a = random.randint(1,100)
print(a)

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
        try_again = input("type YES to play again,else type NO: ").lower()
        if try_again == "yes".lower():
            a = random.randint(1,100)
            attampt = 10
            print(a)
            continue
        else:
            break

    if attampt == 0:
        print("game over")
        print(f"the actual number was {a}")
        try_again = input("type YES to play again,else type NO: ").lower()
        if try_again == "yes".lower():
            a = random.randint(1,100)
            attampt = 10
            print(a)
            continue
        else:
            break
        

