from random import choice

computer_choice = ['stone', 'paper', 'scissors']
computer_turn = choice(computer_choice)
player_choice = input("Enter stone, paper or scissors: ").lower()


if player_choice != 'stone' and player_choice != 'scissors' and player_choice != 'paper':
    print("Enter a valid value!")
if player_choice == 'stone' and computer_turn == 'scissors':
    print('The computer chooses ', computer_turn)
    print("You Win!!!")
elif player_choice == 'paper' and computer_turn == 'stone':
    print('The computer chooses ', computer_turn)
    print("You Win!!!")
elif player_choice == 'scissors' and computer_turn == 'paper':
    print('The computer chooses ', computer_turn)
    print("You Win!!!")
elif player_choice == computer_turn:
    print('The computer chooses ', computer_turn)
    print("Draw")
elif player_choice == 'paper' and computer_turn == 'scissors':
    print('The computer chooses ', computer_turn)
    print("You Lose")
elif player_choice == 'stone' and computer_turn == 'paper':
    print('The computer chooses ', computer_turn)
    print("You Lose")
elif player_choice == 'scissors' and computer_turn == 'stone':
    print('The computer chooses ', computer_turn)
    print("You Lose")

choice = input("Do you want to play again (y or n)").lower()

while choice == 'y':
    player_choice = input("Enter stone, paper or scissors: ").lower()
    print('The computer chooses ', computer_turn)
    if player_choice != 'stone' and player_choice != 'scissors' and player_choice != 'paper':
        print("Enter a valid value!")
    if player_choice == 'stone' and computer_turn == 'scissors':
        print('The computer chooses ', computer_turn)
        print("You Win!!!")
    elif player_choice == 'paper' and computer_turn == 'stone':
        print('The computer chooses ', computer_turn)
        print("You Win!!!")
    elif player_choice == 'scissors' and computer_turn == 'paper':
        print('The computer chooses ', computer_turn)
        print("You Win!!!")
    elif player_choice == computer_turn:
        print('The computer chooses ', computer_turn)
        print("Draw")
    elif player_choice == 'paper' and computer_turn == 'scissors':
        print('The computer chooses ', computer_turn)
        print("You Lose")
    elif player_choice == 'stone' and computer_turn == 'paper':
        print('The computer chooses ', computer_turn)
        print("You Lose")
    elif player_choice == 'scissors' and computer_turn == 'stone':
        print('The computer chooses ', computer_turn)
        print("You Lose")
    choice = input("Do you want to play again (y or n)").lower()