import random

options = ['R', 'P', 'S']
computer = random.choice(options)
user_choice = input("Make a choice: (R,P,S)\n")

if user_choice.upper() == 'R' and computer == 'R':
    print("Tiee")
    print(computer)
elif user_choice.upper() == "P" and computer == "P":
    print("Tie")
    print(computer)

elif user_choice.upper() == "S" and computer == "S":
    print("Tie")
    print(computer)

elif user_choice.upper() == "R" and computer == "P":
    print("Computer wins")
    print(computer)

elif user_choice.upper() == "R" and computer == "S":
    print("User wins")
    print(computer)

elif user_choice.upper() == "P" and computer == "R":
    print("User wins")
    print(computer)

elif user_choice.upper() == "P" and computer == "S":
    print("Computer Wins")
    print(computer)

elif user_choice.upper() == "S" and computer == "P":
    print("Computer wins")
    print(computer)

elif user_choice.upper() == "S" and computer == "R":    
    print("Computer wins")
    print(computer)
