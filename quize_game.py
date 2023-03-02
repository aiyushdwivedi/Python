print("Welcome to the quize !")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit("ok :( , see you soon ! ")

print("Ok! ,Let's play :)")
score =0
wrong =0

print("Answer in small letters only !!")
answer = input("What does IOT stands for? ")
if answer.lower() == "internet of things":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")
    wrong += 1

answer = input("What does GPU stands for ?")
if answer.lower() == "graphics processing unit":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")
    wrong += 1

answer = input("What does RAM? ")
if answer.lower() == "random access memory":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")
    wrong += 1

answer = input("What does CPU stands for ?  ").lower()
if answer == "central processing unit":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")
    wrong += 1

print("You got " + str(score) + " out of 4 question correct!")
print("You got " + str(wrong) + " out of 4 question Incorrect!")

print("You got " + str((score/4) *100) + "% questions correct!")
print("You got " + str((wrong/4) *100) + "% questions Incorrect!")

