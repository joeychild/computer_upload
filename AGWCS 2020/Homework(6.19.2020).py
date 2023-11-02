import time
sec=input("How much time is there left before the launch? ")
try:
    sec=int(sec)
except ValueError:
    quit()
sec=int(sec)
for x in range(sec,0,-1):
    x=str(x)
    print("T minus "+x)
    x=int(x)
    time.sleep(0.1)
print("And we have achieved liftoff!")
time.sleep(5)
num1=input("Enter the first number: ")
num2=input("Enter the second number: ")
try:
    num1=int(num1)
except ValueError:
    quit()
try:
    num2=int(num2)
except ValueError:
    quit()
num1=str(num1)
num2=str(num2)
print("The even numbers between "+num1+" and "+num2+" are as follows:")
num1=int(num1)
num2=int(num2)
for x in range(num1,num2+2,2):
    print(x)
    time.sleep(0.1)
time.sleep(5)
list1=[]
nums=input("How many numbers are there? ")
try:
    nums=int(nums)
except ValueError:
    quit()
nums=int(nums)
for x in range(nums):
    x=input("Please enter a number: ")
    try:
        x=float(x)
    except ValueError:
        quit()
    x=float(x)
    list1.append(x)
list1.sort()
max_value=list1[nums-1]
min_value=list1[0]
max_value=str(max_value)
min_value=str(min_value)
print("The largest value in the list is "+max_value+".")
time.sleep(3)
print("The smallest value in the list is "+min_value+".")
time.sleep(5)
add=input("Please enter a number: ")
try:
    add=int(add)
except ValueError:
    quit()
add=int(add)
sum1=0
for x in range(1,add+1,1):
    sum1+=x
sum1=str(sum1)
print("The sum is "+sum1+".")
