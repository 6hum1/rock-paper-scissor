from tkinter import *
import random

root = Tk()
root.geometry("600x400")
root.title("Rock Paper Scissors")

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        result_text.set("Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result_text.set("You win!")
    else:
        result_text.set("Computer wins!")

# Function to handle user choice
def choose_rock():
    user_choice_text.set("You chose rock")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    computer_choice_text.set(f"Computer chose {computer_choice}")
    determine_winner("rock", computer_choice)

def choose_paper():
    user_choice_text.set("You chose paper")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    computer_choice_text.set(f"Computer chose {computer_choice}")
    determine_winner("paper", computer_choice)

def choose_scissors():
    user_choice_text.set("You chose scissors")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    computer_choice_text.set(f"Computer chose {computer_choice}")
    determine_winner("scissors", computer_choice)

# Create widgets
heading = Label(root, text="Rock Paper Scissors", font=("Arial", 24, "bold"), pady=20)
heading.pack()

user_choice_text = StringVar()
user_choice_label = Label(root, textvariable=user_choice_text, font=("Arial", 16))
user_choice_label.pack()

computer_choice_text = StringVar()
computer_choice_label = Label(root, textvariable=computer_choice_text, font=("Arial", 16))
computer_choice_label.pack()

result_text = StringVar()
result_label = Label(root, textvariable=result_text, font=("Arial", 16), pady=20)
result_label.pack()

rock_button = Button(root, text="Rock", font=("Arial", 16), padx=20, pady=10, command=choose_rock)
rock_button.pack(side=LEFT, padx=10)

paper_button = Button(root, text="Paper", font=("Arial", 16), padx=20, pady=10, command=choose_paper)
paper_button.pack(side=LEFT, padx=10)

scissors_button = Button(root, text="Scissors", font=("Arial", 16), padx=20, pady=10, command=choose_scissors)
scissors_button.pack(side=LEFT, padx=10)

root.mainloop()