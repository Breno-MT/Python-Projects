from time import sleep
import random

while True:
    
    choices = ['scissors', "rock", "paper"]

    computer_choice = random.choice(choices)
    player_choice = None

    while player_choice not in choices:

        player_choice = input(f"Select  -> {choices[0]}, {choices[1]} or {choices[2]} <- : ").lower()
        

        if player_choice == computer_choice:

            print("--> HERE WE GO!!! <--")
            sleep(0.9)
            print("--> JO! <--")
            sleep(1)
            print("--> KEN! <--")
            sleep(1)
            print("--> PO! <--")
            sleep(1)
            print(f"Player's Choice: {player_choice}")
            print("-"*9)
            print(f"Computer's Choice: {computer_choice}")
            print("-"*9)
            print("It's a tie!")
        
        elif player_choice == "scissors":
            if computer_choice == "rock":
                print("--> HERE WE GO!!! <--")
                sleep(0.9)
                print("--> JO! <--")
                sleep(1)
                print("--> KEN! <--")
                sleep(1)
                print("--> PO! <--")
                sleep(1)
                print("-"*9)
                print(f"Player's Choice: {player_choice}")
                print("-"*9)
                print(f"Computer's Choice: {computer_choice}")
                print("-"*9)
                print("You Lost!")
            
            if computer_choice == "paper":
                print("--> HERE WE GO!!! <--")
                sleep(0.9)
                print("--> JO! <--")
                sleep(1)
                print("--> KEN! <--")
                sleep(1)
                print("--> PO! <--")
                sleep(1)
                print("-"*9)
                print(f"Player's Choice: {player_choice}")
                print("-"*9)
                print(f"Computer's Choice: {computer_choice}")
                print("-"*9)
                print("You Won!")
        
        elif player_choice == "rock":
            if computer_choice == "paper":
                print("--> HERE WE GO!!! <--")
                sleep(0.9)
                print("--> JO! <--")
                sleep(1)
                print("--> KEN! <--")
                sleep(1)
                print("--> PO! <--")
                sleep(1)
                print("-"*9)
                print(f"Player's Choice: {player_choice}")
                print("-"*9)
                print(f"Computer's Choice: {computer_choice}")
                print("-"*9)
                print("You Lost!")
            
            if computer_choice == "scissors":
                print("--> HERE WE GO!!! <--")
                sleep(0.9)
                print("--> JO! <--")
                sleep(1)
                print("--> KEN! <--")
                sleep(1)
                print("--> PO! <--")
                sleep(1)
                print("-"*9)
                print(f"Player's Choice: {player_choice}")
                print("-"*9)
                print(f"Computer's Choice: {computer_choice}")
                print("-"*9)
                print("You Won!")
        
        elif player_choice == "paper":
            if computer_choice == "scissors":
                print("--> HERE WE GO!!! <--")
                sleep(0.9)
                print("--> JO! <--")
                sleep(1)
                print("--> KEN! <--")
                sleep(1)
                print("--> PO! <--")
                sleep(1)
                print("-"*9)
                print(f"Player's Choice: {player_choice}")
                print("-"*9)
                print(f"Computer's Choice: {computer_choice}")
                print("-"*9)
                print("You Lost!")

            
            if computer_choice == "rock":
                print("--> HERE WE GO!!! <--")
                sleep(0.9)
                print("--> JO! <--")
                sleep(1)
                print("--> KEN! <--")
                sleep(1)
                print("--> PO! <--")
                sleep(1)
                print(f"Player's Choice: {player_choice}")
                print("-"*9)
                print(f"Computer's Choice: {computer_choice}")
                print("-"*9)
                print("You Won!")

    play_again = input("Wanna play again? (y/n): ").lower()
    if play_again != "y":
        break
print("Have a nice day!")