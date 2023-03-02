name = input("Type your name :  ")
print("Welcome", name ,"to the adventure! ")
points = 0
wrong = 0
answer = input("You are on a dirt road and it came to an end , you want to go left or right ?").lower()


if answer == "left":
    answer = input("OK you came to a river , you can walk around it or swim across, write walk to walk and swim to swim across")


    if answer == "swim":
        print("you swim across and were eaten by an alligator")
        wrong += 1
    elif answer == "walk":
        print("You walked many miles and ran out of water and died . You lost the game")
        wrong += 1
    else:
        ("Not a vaild option. you lost")
        wrong += 1


elif answer == "right":
    points += 1
    answer = input("You came across a bridge. want to cross or walk back. Type cross to cross and back to walk back")

    if answer == "back":
        print("you go back and loose")
        wrong += 1
    elif answer == "cross":
        points += 1
        answer = input("You cross and meet a stranger . Do you talk to them or not(yes/no)")

        if answer == "yes":
            print("you talked to the stranger and they gave you gold. you won")
            points += 4
        elif answer == "no":
            print("you ignore the stranger and they got offended and you loose")
            wrong += 1
        else:
            print("You loose")
            wrong += 1
    else:
      ("Not a vaild option. you lost")
      wrong += 1
print("Thank you for playing",name)
print("You earned ",points," points")
print("You made ",wrong," wrong choices")