#Rock, paper, Scissors Game
import random           #importing the random module


while True:
    winner = ""
    possible_options = ["R", "P", "S"] #possible options

    #determine computer's choice
    CPU_choice = random.choice(possible_options)

    #Making sure Player's choice is valid
    player_choice = ""
    while (player_choice != "R" and player_choice != "P"
           and player_choice != "S"):
         #prompting the player to enter their choice.
        player_choice = input ('R for rock, P for paper and S for scissors? pick an option between \"R\",\"P\" or \"S\" :')
    

    #game logic to determine who the winner is?

    if CPU_choice == player_choice:
        winner = "Tie"
    elif CPU_choice == "P" and player_choice == "R" :
        winner = "Computer"
    elif CPU_choice == "R" and player_choice == "S" :
        winner == "Computer"
    elif CPU_choice == "S" and player_choice == "P" :
        winner = "Computer"
    else:
        winner = "Player"

        #announcing the Winner 

    if winner == "Tie":
        print ("We both chose ", CPU_choice + ", Play again.")
    else:
        print (winner," won.The Computer chose ", CPU_choice + ".")
        break
    

