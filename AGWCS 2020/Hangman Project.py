import time
import random
import os

strikes = 0
right = 0
blanks = []
wrongs = []
list1 = []
other = []

f = open("Words.txt")
f = f.read()
for i in f.split("\n"):
    list1.append(i)
r = list1[random.randint(0,999)]
for i in r:
    blanks.append(" _ ")
wordletters = []
for i in r:
    wordletters.append(i)


print("                                                            You are now playing")
time.sleep(2)
print("")
print("")
print(" .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.")
print("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
print("| |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |")
print("| | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |")
print("| |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |")
print("| |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |")
print("| |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |")
print("| | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |")
print("| |              | || |              | || |              | || |              | || |              | || |              | || |              | |")
print("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
print(" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'") 
time.sleep(1)
print("                                                               By: Joey Zhang")
print("")
time.sleep(2)
os.system("cls")
for i in range(0,2):
    for y in range(0,4):
        b = "                                                    The computer is now choosing a word" + "." * y
        print(b, end = "\r")
        time.sleep(1)
    print("")
    os.system("cls")
print("                                                      The computer has selected a word!")
time.sleep(2)
os.system("cls")

while True:

    if strikes == 0:
        print("                                                                             ____________________")
        print("                                                                            |                    |")
        print("                                                                            |                    |")
        print("                                                                                                 |")
        print("                                                                                                 |")
        print("                                                                                                 |")
        print("                                                                                                 |")
        print("                                                                                                 |")
        print("                                                                                                 |")
        print("                                                                                                 |")
        print("                                                                                                 |")
        print("                                                                                                 |")
        print("                                                                                                / \ ")
        print("                                                                                               /   \ ")
        print("----------------------------------------------------------------------------------------------'-----'--")
    elif strikes == 1:
        print("                                                                             ____________________")
        print("                                                                            |                    |")
        print("                                                                            |                    |")
        print("                                                                          .---.                  |")
        print("                                                                         /     \                 |")
        print("                                                                         \     /                 |")
        print("                                                                          '───'                  |")
        print("                                                                                                 |")
        print("                                                                                                 |")
        print("                                                                                                 |")
        print("                                                                                                 |")
        print("                                                                                                 |")
        print("                                                                                                / \ ")
        print("                                                                                               /   \ ")
        print("----------------------------------------------------------------------------------------------'-----'--")
    elif strikes == 2:
        print("                                                                             ____________________")
        print("                                                                            |                    |")
        print("                                                                            |                    |")
        print("                                                                          .---.                  |")
        print("                                                                         /     \                 |")
        print("                                                                         \     /                 |")
        print("                                                                          '─┬─'                  |")
        print("                                                                            |                    |")
        print("                                                                            |                    |")
        print("                                                                            |                    |")
        print("                                                                                                 |")
        print("                                                                                                 |")
        print("                                                                                                / \ ")
        print("                                                                                               /   \ ")
        print("----------------------------------------------------------------------------------------------'-----'--")
    elif strikes == 3:
        print("                                                                             ____________________")
        print("                                                                            |                    |")
        print("                                                                            |                    |")
        print("                                                                          .---.                  |")
        print("                                                                         /     \                 |")
        print("                                                                         \     /                 |")
        print("                                                                          '─┬─'                  |")
        print("                                                                           /|                    |")
        print("                                                                       o__/ |                    |")
        print("                                                                            |                    |")
        print("                                                                                                 |")
        print("                                                                                                 |")
        print("                                                                                                / \ ")
        print("                                                                                               /   \ ")
        print("----------------------------------------------------------------------------------------------'-----'--")
    elif strikes == 4:
        print("                                                                             ____________________")
        print("                                                                            |                    |")
        print("                                                                            |                    |")
        print("                                                                          .---.                  |")
        print("                                                                         /     \                 |")
        print("                                                                         \     /  o              |")
        print("                                                                          '─┬─'  /               |")
        print("                                                                           _|___/                |")
        print("                                                                          / |                    |")
        print("                                                                         |  |                    |")
        print("                                                                         o                       |")
        print("                                                                                                 |")
        print("                                                                                                / \ ")
        print("                                                                                               /   \ ")
        print("----------------------------------------------------------------------------------------------'-----'--")
    elif strikes == 5:
        print("                                                                             ____________________")
        print("                                                                            |                    |")
        print("                                                                            |                    |")
        print("                                                                          .---.                  |")
        print("                                                                         /     \                 |")
        print("                                                                         \     /  o              |")
        print("                                                                      o   '─┬─'  /               |")
        print("                                                                       \____|___/                |")
        print("                                                                            |                    |")
        print("                                                                            |                    |")
        print("                                                                           /                     |")
        print("                                                                          /                      |")
        print("                                                                         d                      / \ ")
        print("                                                                                               /   \ ")
        print("----------------------------------------------------------------------------------------------'-----'--")
    elif strikes == 6:
        print("                                                                             ____________________")
        print("                                                                            |                    |")
        print("                                                                            |                    |")
        print("                                                                          .---.                  |")
        print("                                                                         /     \                 |")
        print("   _      ___  _____ _____   _____ _   _  ___  _   _ _____ _____ _       \     /                 |")
        print("  | |    / _ \/  ___|_   _| /  __ \ | | |/ _ \| \ | /  __ \  ___| |    o  '─┬─'                  |")
        print("  | |   / /_\ \ `--.  | |   | /  \/ |_| / /_\ \  \| | /  \/ |__ | |     \___|                    |")
        print("  | |   |  _  |`--. \ | |   | |   |  _  |  _  | . ` | |   |  __|| |         |\                   |")
        print("  | |___| | | /\__/ / | |   | \__/\ | | | | | | |\  | \__/\ |___|_|         | \                  |")
        print("  \_____|_| |_|____/  \_/    \____|_| |_|_| |_|_| \_/\____|____/(_)        / \_o                 |")
        print("                                                                          /__  \                 |")
        print("                                                                                b               / \ ")
        print("                                                                                               /   \ ")
        print("--------------------------------------------------------------------------d-------------------'-----'--")
    if strikes < 7:
        print("")
        separator = ''
        print(" " * (46 - len(blanks)) + "Word:"+ separator.join(blanks)) 
        print("")
        print(" " * (46 - 2 * len(wrongs)) + "Wrong guesses:" + separator.join(wrongs))
        print("")
        print("                                           What is your guess?")
        string = input("                                                    ")
        x = 0
        if len(string) == 1:
            if string.isalpha() == True:
                string = string.lower()
                if string not in other:
                    other.append(string)
                    if string in wordletters:
                        print("                                            That was correct!")
                        for i in r:
                            x = x + 1
                            if string == i:
                                blanks[x-1] = " " + string + " "
                    else:
                        print("                             I'm sorry, but that was not a letter in the word. ")
                        wrongs.append(" " + string + " ")
                        strikes = strikes + 1
                else:
                    print("                                I'm sorry, but that was a duplicate letter. ")
            else:
                print("                                  I'm sorry, but that was not a letter. ")
        else:
            print("                                  I'm sorry, but that was not a letter.")
        time.sleep(3)
        os.system("cls")
        for i in blanks:
            if i == " _ ":
                pass
            else:
                right = right + 1
        if right == len(r):
            print("                                                                             ____________________")
            print("                                                                            |                    |")
            print("                                                                            |                    |")
            print("       __   _______ _   _   _    _ _____ _   _ _                                                 |")
            print("       \ \ / /  _  | | | | | |  | |_   _| \ | | |                                                |")
            print("        \ V /| | | | | | | | |  | | | | |  \| | |                     .---.                      |")
            print("         \ / | | | | | | | | |/\| | | | | . ` | |                    / ^ ^ \                     |")
            print("         | | \ \_/ / |_| | \  /\  /_| |_| |\  |_|                  o \     / o                   |")
            print("         \_/  \___/ \___/   \/  \/ \___/\_| \_(_)                   \ '─┬─' /                    |")
            print("                                                                     \__|__/                     |")
            print("                                                                        |                        |")
            print("                                                                        |                        |")
            print("                                                                       / \                      / \ ")
            print("                                                                      /   \                    /   \ ")
            print("---------------------------------------------------------------------d-----b------------------'-----'--")
            print("")
            print("")
            print("                               To play again, press Fn + F5")
            time.sleep(3)
            break
        else:
            pass
    else:
        print("                                                                             ____________________")
        print("                                                                            |                    |")
        print("                                                                            |                    |")
        print("                                                                          .---.                  |")
        print("                                                                         / x x \                 |")
        print("       __   _______ _   _   _     _____ _____ _____                      \     /                 |")
        print("       \ \ / /  _  | | | | | |   |  _  /  ___|  ___|                      '─┬─'                  |")
        print("        \ V /| | | | | | | | |   | | | \ `--.| |__                          |                    |")
        print("         \ / | | | | | | | | |   | | | |`--. \  __|                        /|\                   |")
        print("         | | \ \_/ / |_| | | |___\ \_/ /\__/ / |___                       / | \                  |")
        print("         \_/  \___/ \___/  \_____/\___/\____/\____/                      o / \ o                 |")
        print("                                                                          |   |                  |")
        print("                                                                          |   b                 / \ ")
        print("                                                                                               /   \ ")
        print("-------------------------------------------------------------------------d--------------------'-----'--")
        print("")
        print("")
        print("                                        The word was: " + r)
        time.sleep(1)
        print("                                   To play again, press Fn + F5")
        time.sleep(2)
        break
    right = 0

                


