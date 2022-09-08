import random
import time

while True:
    current_number = 0
    current_player = random.randint(0, 1)

    if current_player == 0:
        print("Player is human")
    else:
        print("Player is computer")

    while current_number <=21:
        print("The current number is ",current_number)
        if current_player == "human":
            myList = ['1','2','3']
            
            player_choice = ""
            while player_choice not in myList:
                player_choice = input("Your turn, pick your number: ")
            player_choice = int(player_choice)
            current_number += player_choice
            if current_number >= 21:
                print("The current number is " + str(current_number) + ".")
                print("Sorry, you lose.")
                break
            current_player = "computer"
        else:
            computer_choice = random.randint(1, 3)
            current_number = current_number + computer_choice
            print("Computer turn. The computer choses " +
                  str(computer_choice) + ".")
            print()
            time.sleep(1)

            if current_number >= 21:
                print("The current number is " + str(current_number) + ".")
                print()
                print("Well done, you won!")
                break
            current_player = "human"
    print()
    play_again = input("Do you want to play again? ")
    if play_again.lower().startswith("y"):
        continue
    else:
        print("Goodbye")
        break