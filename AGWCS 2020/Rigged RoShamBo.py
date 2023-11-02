import random
import time
list1=["rock","Rock"]
list2=["paper","Paper"]
list3=["scissors","Scissors"]
list5=["Yes","yes","y","Y"]
list6=["No","no","n","N"]
computer_score=0
while True:
    #User Input
    userInput=input("Do you wish to play rock, paper, or scissors? ")
    if userInput in list1:
        pass
    elif userInput in list2:
        pass
    elif userInput in list3:
        pass
    else:
        print("Error. Please try again.")
        continue
    time.sleep(1)
    if userInput in list1:
        print("The computer played paper. The computer wins!")
        computer_score=computer_score+1
    elif userInput in list2:
        print("The computer played scissors. The computer wins!")
        computer_score=computer_score+1
    else:
        print("The computer played rock. The computer wins!")
        computer_score=computer_score+1
    time.sleep(2)
    #Scoreboard
    thing=input("Would you like to see the scores? ")
    if thing in list5:
        computer_score=str(computer_score)
        print("The computer has won a total of "+computer_score+" rounds.")
        time.sleep(2)
        print("You have won a total of 0 rounds.")
        time.sleep(2)
        print("There have been 0 draws.")
        time.sleep(2)
        computer_score=int(computer_score)
    elif thing in list6:
        time.sleep(2)
    else:
        print("Error. Please try again. ")
        continue
    #Restart
    again=input("Would you like to play again? ")
    if again in list5:
        print("Okay!")
        continue
    elif again in list6:
        break
    else:
        print("Error. Please try again. ")
        continue
print("The computer wins!")
quit()
