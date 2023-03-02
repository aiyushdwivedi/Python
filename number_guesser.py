import random

top_of_ranger = input("Type a number: ")

if top_of_ranger.isdigit():
    top_of_ranger = int(top_of_ranger)

    if top_of_ranger <= 0:
        print("Please type a number larger than zero next time ")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0, top_of_ranger)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess  ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number next time")
        continue
    if user_guess == random_number:
        print("You got it !")
        break

    elif user_guess > random_number:
            print("You guessed greater then the number")
    else:
            print("You guessed smaller then the number!")
print("You got it in", guesses, "guesses")