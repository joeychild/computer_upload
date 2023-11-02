import time
import random
print('Count word occurences')
time.sleep(1)
string = input("Please enter a string: ")
word = input("Please enter the string you would like to have counted: ")
if string.count(word) == 1:
    print("There was 1 occurence of the string "+word+" in the string "+string+".")
else:
    print("There were "+str(string.count(word))+" occurences of the string "+word+" in the string "+string+".")
time.sleep(2)
print('Average')
time.sleep(1)
sum = 0
num = 0
while True:
    string = input("Please enter a number: ")
    try:
        float(string)
    except ValueError:
        print("The value you entered was not a number. Please try again.")
        continue
    string = float(string)
    sum += string
    num += 1
    go = input('If you would like to enter another value, please enter y. Otherwise, enter n.')
    if go == 'y':
        continue
    elif go == 'n':
        break
    else:
        print("Term not recognized. Please try again.")
        continue
print("The average is "+str(sum / num)+".")
time.sleep(2)
print('Pick a random item')
time.sleep(1)
while True:
    string = input("Please enter a value: ")
    list.append(string)
    go = input('If you would like to enter another value, please press y. Otherwise, enter n.')
    if go == 'y':
        continue
    elif go == 'n':
        break
    else:
        print("Term not recognized. Please try again.")
        continue
x = random.randint(0, (len(list)-1))
print("The chosen value is: "+list[x]+".")
time.sleep(2)
list.clear()
while True:
    string = input("Please enter a value: ")
    list.append()
    go = input('If you would like to enter another value, please press y. Otherwise, enter n.')
    if go == 'y':
        continue
    elif go == 'n':
        break
    else:
        print("Term not recognized. Please try again.")
        continue
print(random.shuffle(list))
time.sleep(2)
list.clear()
list1 = []
list2 = []
list3 = []
list4 = []
while True:
    string = input("Please enter the first name: ")
    string.append(list)
    string = input("Please enter the last name: ")
    string.append(list1)
    while True:
        string = input("Please enter the age: ")
        try:
            string = int(string)
        except ValueError:
            print("The value entered was not an integer. Please try again.")
            continue
        string.append(list2)
    string = input("Please enter the email: ")
    string.append(list3)
    string = input("Lastly, please enter the state: ")
    string.append(list4)
    go = input("If you would like to enter another contact, enter y. Otherwise, enter n.")
    if go == 'y':
        continue
    elif go == 'n':
        break
    else:
        print("Term not recognized. Please try again.")
        continue
print("Here is all of the information recorded:")
print("First names: ")
print(list)
print("Last names: ")
print(list1)
print("Ages: ")
print(list2)
print("Emails: ")
print(list3)
print("States: ")
print(list4)
time.sleep(2)
list.clear()
while True:
    string = input("Please enter a value: ")
    list.append()
    go = input('If you would like to enter another value, please press y. Otherwise, enter n.')
    if go == 'y':
        continue
    elif go == 'n':
        break
    else:
        print("Term not recognized. Please try again.")
        continue
print("The list entered without duplicates is shown here:")
print(set(list))
time.sleep(2)




        
    

