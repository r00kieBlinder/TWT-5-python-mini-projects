print("Welcome to my computer quiz!")

playing = input("Do you want to play? (yes or no) : ")

if playing.lower() != "yes": # converts everything to lowercase
    print("It's okay we'll play sometime.")
    quit() # quits the program

score = 0

print("Okay! Let's play! 😃")

answer = input("What does CPU stands for? : ") # we can also use .lower() function here
if answer.lower() == "central processing unit":
    print("Correct! 🫡")
    score += 1
else:
    print("Wrong answer. Sorry try again! ☹️")

answer = input("What does GPU stands for? : ")
if answer.lower() == "graphics processing unit":
    print("Correct! 🫡")
    score += 1
else:
    print("Wrong answer. Sorry try again! ☹️")

answer = input("What does RAM stands for? : ")
if answer.lower() == "random access memory":
    print("Correct! 🫡")
    score += 1
else:
    print("Wrong answer. Sorry try again! ☹️")

answer = input("What does PSU stands for? : ")
if answer.lower() == "power supply":
    print("Correct! 🫡")
    score += 1
else:
    print("Wrong answer. Sorry try again! ☹️")

print(f"Thanks for playing this quiz game! your score is {score}")
print(f"You got {(score / 4) * 100}%")