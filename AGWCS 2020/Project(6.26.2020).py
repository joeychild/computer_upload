import random
import time
list1=["rock","Rock"]
list2=["paper","Paper"]
list3=["scissors","Scissors"]
list5=["Yes","yes","y","Y"]
list6=["No","no","n","N"]
rocks=[1]
papers=[1]
scissors=[1]
computer_score=0
user_score=0
draws=0
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
    #Determines the computer's move
    num1=len(rocks)
    num2=len(papers)
    num3=len(scissors)
    list4=[num1,num2,num3]
    list4.sort()
    if num1==num2==num3:
        nums=random.randint(0,2)
        if nums==0:
            computerInput="rocks"
        elif nums==1:
            computerInput="paper"
        else:
            computerInput="scissors"
    elif list4[2]==num1:
        computerInput="paper"
    elif list4[2]==num2:
        computerInput="scissors"
    else:
        computerInput="rock"
    #Who wins
    if userInput in list1:
        rocks.append(1)
        if computerInput in list2:
            print("The computer chose paper. The computer wins!")
            computer_score=computer_score+1
        elif computerInput in list3:
            print("The computer chose scissors. You win! ")
            user_score=user_score+1
        else:
            print("The computer chose rock. It's a draw! ")
            draws=draws+1
    elif userInput in list2:
        papers.append(1)
        if computerInput in list3:
            print("The computer chose scissors. The computer wins! ")
            computer_score=computer_score+1
        elif computerInput in list1:
            print("The computer chose rock. You win! ")
            user_score=user_score+1
        else:
            print("The computer chose paper. It's a draw! ")
            draws=draws+1
    else:
        scissors.append(1)
        if computerInput in list1:
            print("The computer chose rock. The computer wins! ")
            computer_score=computer_score+1
        elif computerInput in list2:
            print("The computer chose paper. You win! ")
            user_score=user_score+1 
        else:
            print("The computer chose scissors. It's a draw! ")
            draws=draws+1
    time.sleep(2)
    #Scoreboard
    thing=input("Would you like to see the scores? ")
    if thing in list5:
        computer_score=str(computer_score)
        user_score=str(user_score)
        draws=str(draws)
        print("The computer has won a total of "+computer_score+" rounds.")
        time.sleep(2)
        print("You have won a total of "+user_score+" rounds.")
        time.sleep(2)
        print("There have been "+draws+" draws.")
        time.sleep(2)
        computer_score=int(computer_score)
        user_score=int(user_score)
        draws=int(draws)
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
if computer_score>user_score:
    print("The computer wins!")
elif computer_score<user_score:
    print("You win!")
else:
    print("It's a draw!")
quit()

