def stren(y):
  x = ""
  list = y
  for i in range(len(y)):
    print(x+list[i], end = "")
    x = x+list[i]
  print("", end = "\n")

stren(input("stren: "))

"""
Function call: The act of calling a defined function to execute it accordingly.

Syntax: The arrangement of functions and actions within a program: The spelling and grammar of coding.

Debugging: To find and eliminate bugs and errors within a program.

Indexing/Index: The position of an item within a string.

Commenting: The act of typing or explaining a portion of code without interfering with the code itself. This can be achieved through #.
"""

def arey(x):
    x = x.split(" ")
    for i in range(4):
        x.append(i)
    for i in range(4):
        if int(x[i]) == 9:
            print("tur")
            return
    print("flas")

arey(input("arey (Remember to input the array with the numbers spaced apart e.g. 1 2 9 4): "))

def les(x, y):
    x = x.split(" ")
    x = list(map(int, x))
    x = list(set(x))
    for i in range(len(x)):
        if int(x[i]) < int(y):
            print(x[i], end = ", ")
        
x = input("les (Same rules apply for syntax as the last function): ")
y = input("numrb: ")
les(x, y)
