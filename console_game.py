import random
from time import sleep

while True:
    total_rounds = input("How many rounds would you like to play? ")
    try:
        number = int(total_rounds)
        break;
    except ValueError:
        print("Please enter the NUMBER of rounds.")
        sleep(0.8)
print("OK, we'll play", total_rounds, "rounds.")
total_rounds_number = int(total_rounds)
round = 0
user_wins = 0
cpu_wins = 0
sleep(1)

while round < total_rounds_number:
    print("Round number", round + 1)
    sleep(1)
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
    print("You go with", attack + ".")
    sleep(0.5)

    cpu_choice = ['ROCK', 'PAPER', 'SCISSORS']
    defense = random.choice(cpu_choice)
    print("I go with", defense + ".")
    round += 1
    sleep(0.8)

    if attack == 'ROCK':
        if defense == 'ROCK': 
            print("We have a draw...")
        if defense == 'PAPER':
            print('I won!')
            cpu_wins +=1
        if defense == 'SCISSORS':
            print('You won... THIS TIME!')
            user_wins += 1

    if attack == 'PAPER':
        if defense == 'PAPER': 
            print("We have a draw...")
        if defense == 'SCISSORS':
            print('I won!')
            cpu_wins += 1
        if defense == 'ROCK':
            print('You won... THIS TIME!')
            user_wins += 1

    if attack == 'SCISSORS':
        if defense == 'SCISSORS': 
            print("We have a draw...")
        if defense == 'ROCK':
            print('I won!')
            cpu_wins += 1
        if defense == 'PAPER':
            print('You won... THIS TIME!')
            user_wins += 1
else:
    print("OK, that's it. Let's see the results.")
    sleep(1)
    if user_wins == cpu_wins:
        print("We have a draw, thanks for playing!")
    if user_wins > cpu_wins:
        print("Well, you win - congratulations...")
    if user_wins < cpu_wins:
        print("You lose! Better luck next time.")