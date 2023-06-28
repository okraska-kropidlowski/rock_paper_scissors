import random

available_choice = ['R', 'P', 'S', 'r', 'p', 's', 'Rock', 'Paper', 'Scissors', 'rock', 'paper', 'scissors']
while True:
    user_choice = str(input("Enter your choice (Rock/Paper/Scissors): "))
    if user_choice in available_choice:
        break
if user_choice == 'R' or user_choice == 'r' or user_choice == 'Rock' or user_choice == 'rock':
    attack = 'ROCK'
    if user_choice == 'P' or user_choice == 'p' or user_choice == 'Paper' or user_choice == 'paper':
        attack = 'PAPER'
    if user_choice == 'S' or user_choice == 's' or user_choice == 'Scissors' or user_choice == 'scissors':
        attack = 'SCISSORS'
print("You go with",attack + ".")

cpu_choice = ['ROCK', 'PAPER', 'SCISSORS']
defense = random.choice(cpu_choice)
print("I go with",defense + ".")
