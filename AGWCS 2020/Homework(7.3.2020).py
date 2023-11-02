import time
string = input('Please enter a string: ')
for i in string:
    print(i)
    time.sleep(0.1)
time.sleep(2)
string = input('Please enter a string: ')
length = len(string)
if length < 2:
    print('')
else:
    print(string[0]+string[1]+string[length-2]+string[length-1])
time.sleep(2)
string = input('Please enter a string: ')
phase = string.replace('a','@')
phase = phase.replace('s','$')
phase = phase.replace('l','!')
phase = phase.replace('o','0')
print(phase)
time.sleep(2)
string = input('Please enter a string: ')
word = input('Please enter the word you want to have counted in the string: ')
print('There are '+str(string.count(word))+' occurences of the word -'+word+'-.')
time.sleep(2)
list1 = []
list2 = ""
string = input('Please enter a string: ')
for i in string:
    n = ord(i)
    list1.append(n)
list1.sort()
for i in list1:
    n = chr(i)
    list2 = list2 + n
print(list2)
time.sleep(2)
Upper = ''
lower = ''
for i in range(65, 65+26):
    n = chr(i)
    Upper = Upper + n
for i in range(97, 97+26):
    n = chr(i)
    lower = lower + n
print(Upper)
print(lower)
print('All operations are complete. System shutting down...')
time.sleep(3)
quit()

            