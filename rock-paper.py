import random
import tkinter as tk

window = tk.Tk()
window.title("Python GUI")

options = ['R', 'P', 'S']
computer = random.choice(options)
user_choice = input("Make a choice: (R,P,S)\n")

if user_choice.upper() == 'R' and computer == 'R':
    print("Tie")
elif user_choice.upper() == "P" and computer == "P":
    print("Tie")
elif user_choice.upper() == "S" and computer == "S":
    print("Tie")
elif user_choice.upper() == "R" and computer == "P":
    print("Computer wins")
elif user_choice.upper() == "R" and computer == "S":
    print("User wins")
elif user_choice.upper() == "P" and computer == "R":
    print("User wins")
elif user_choice.upper() == "P" and computer == "S":
    print("Computer Wins")
elif user_choice.upper() == "S" and computer == "P":
    print("Computer wins")
elif user_choice.upper() == "S" and computer == "R":    
    print("Computer wins")