Want_play = input("Do you want to play?:\n")
if Want_play.lower() == "no":
    print("Quiting the program.")
    quit()
score = 0
print("Lets Play it:")

answer = input("CPU stands for?:\n")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("GPU stands for?:\n")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("RAM stands for?:\n")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("PSU stands for?:\n")
if answer.lower() == "power supply":
    print("Correct")
    score += 1
else:
    print('Incorrect')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
