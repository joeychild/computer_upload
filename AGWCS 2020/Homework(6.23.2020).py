import time
import math
def quad(a,b,c):
    a=int(a)
    b=int(b)
    c=int(c)
    x=((-b+math.sqrt((b**2)-4*(a)*(c)))/(2*a))
    other_x=((-b-math.sqrt((b**2)-4*(a)*(c)))/(2*a))
    a=str(a)
    b=str(b)
    c=str(c)
    x=str(x)
    other_x=str(other_x)
    if a=="1":
        a=""
    elif a=="-1":
        a="-"
    else:
        pass
    print("The answers to "+a+"x²+"+b+"x+"+c+" are "+x+" and "+other_x+".")  
a=input("Please enter the first constant: ")
b=input("Please enter the second constant: ")
c=input("Please enter the third constant: ")
try:
    a=int(a)
except ValueError:
    quit()
try:
    b=int(b)
except ValueError:
    quit()
try:
    c=int(c)
except ValueError:
    quit()
print("Calculating...")
time.sleep(3)
quad(a,b,c)
time.sleep(3)
num1=input("Please enter the first number: ")
num2=input("Please enter the second number: ")
num3=input("Please enter the third number: ")
list1=[num1,num2,num3]
print("Calculating...")
time.sleep(3)
try:
    num1=float(num1)
except ValueError:
    quit()
try:
    num2=float(num2)
except ValueError:
    quit()
try:
    num3=float(num3)
except ValueError:
    quit()
list1.sort()
print("The largest number in the list is "+list1[2]+" and the smallest number in the list is "+list1[0]+".")
time.sleep(3)
def flip(x):
    return x[::-1]
text=input("What characters would you like printed backwards? ")
print("Calculating...")
time.sleep(3)
backwards=flip(text)
print("The characters "+text+" printed backwards is "+backwards+".")
time.sleep(3)
def palindrome(x):
    x=x.lower()
    y=x[::-1]
    if y==x:
        x=x.capitalize()
        print(x+" is a palindrome.")
    else:
        x=x.capitalize()
        print(x+" is not a palindrome.")
x=input("Please enter a word: ")
print("Calculating...")
time.sleep()
palindrome(x)
    
