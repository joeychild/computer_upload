import time
import sys
name=input("What's your name, little one? ")
hi=input("Oh. "+name+". That's a very nice name... ")
print("Oh, nothing. It's fine. My old friend had that very same name...")
time. sleep(4)
print("Never mind. This is a calculation office. What was I thinking?")
time. sleep(4)
job=input("What is your occupation? ")
#Debugging dumb answers; Kills the code.
list3=["nothing","never mind", "stupid", "dumb"]
if job in list3:
    print("Come on now, little one. You can't be serious. "+job+"? How do you expect me to react?")
    time. sleep(4.75)
    print("You know what? Get out of here, ya little one! Get out!")
    time. sleep(3.5)
    print("Stupid kids these days, trying to be funny at my office.")
    time. sleep(3)
    sys.exit()
else:
    time. sleep(0.5)
print("Oh, you are a..."+job+", little one? Very good job, very profitable, yes...")
time. sleep(5)
print("Sorry, I was thinking about something...carry on...")
time. sleep(3)
#Hours worked per day
hours=input("How many hours do you work per day, little one? ")
#Really bad debugs
if "." in hours:
    hours=float(hours)
else:
    hours=int(hours)
print("Yes...ok.")
time. sleep(1)
#Rate of pay
pay=input("How much pay do you recieve per hour, little one? $")
print("$"+pay+"...ok. Got it. Let me just input everything...")
#Really bad debugs
if "." in pay:
    pay=float(pay)
else:
    pay=int(pay)
time. sleep(4)
#All calculations
dayPay=pay*hours
weekPay=dayPay*7
monthPay=dayPay*30
yearPay=dayPay*365
#Rounding all calculations to monetary values
dayPay=round(dayPay,2)
weekPay=round(weekPay,2)
monthPay=round(monthPay,2)
yearPay=round(yearPay,2)
#Convert to strings
dayPay=str(dayPay)
weekPay=str(weekPay)
monthPay=str(monthPay)
yearPay=str(yearPay)
print("All right, little one. Your daily salary is around $"+dayPay+"...")
time. sleep(4)
print("Your weekly salary is around $"+weekPay+"...")
time. sleep(3.5)
print("Your monthly salary is around $"+monthPay+"...")
time. sleep(3.5)
print("and your yearly salary is...")
time. sleep(2.75)
hih=input("Oh, no... ")
print("Your yearly salary is around $"+yearPay+", which means...")
time. sleep(5)
hihh=input("You need to go, NOW! ")
print("You were one of the chosen men to help free the kingdom, little one!")
time. sleep(3.5)
print("You must head west and join the alliance to free us all!")
time. sleep(3.5)
print("Now, quick! Run! Run before I am terminated!")
time. sleep(2.5)
print("The kingdom knows of your presence!")
time. sleep(2.5)
print("They know I have spread forbidden knowledge!")
time. sleep(2.5)
print("Once I am terminated, we will BOTH perish!")
time. sleep(2.5)
print("Run, little one, RUN!")
time. sleep(1.75)
print("You follow the man's instructions and run.")
time. sleep(3)
print("You look behind you and watch as the office's alarms blare.")
time. sleep(3.5)
print("The man you were talking to looks at you with hope, and yells with his final breath,")
time. sleep(4.5)
print("I am free!")
time. sleep(1.75)
print("You watch as the man implodes in a fiery explosion, engulfing the entire office.")
time. sleep(4.5)
print("You continue running for many days, until you finally collapse in front of a strange house.")
time. sleep(4.5)
print("You see a man inside the building, looking at you in confusion.")
time. sleep(3)
print("He comes up to you, saying,")
time. sleep(2)
print("Would you like to know the temperature, little one?")
time. sleep(3)
print("You suddenly realize that this is another calculation office, but you can't leave.")
time. sleep(4)
print("The man says,")
time. sleep(2)
list1=["Fahrenheit","fahrenheit"]
list2=["Celsius","celsius"]
word=input("Would you like to have the temperature in Fahrenheit or Celsius? ")
#Fahrenheit
if word in list1:
    cTemp=input("Alrighty, just give me the temperature right now...")
    print("Just give me a second to put this in...")
    time. sleep(3)
    if "." in cTemp:
        float(cTemp)
    else:
        int(cTemp)
    fTemp=(cTemp*1.8)+32
    fTemp=round(fTemp,2)
    fTemp=str(fTemp)
    print("The temperature in Fahrenheit is about "+fTemp+" degre-")
    time. sleep(4)
    print("Hold on, what is your name?")
    time. sleep(3)
    print("Boys, I think we found the fugitive.")
    time. sleep(3)
    print("You realize that they were talking about you and you take off running.")
    time. sleep(4)
    print("The men chase you, but run out of strength after a while, letting you go.")
    time. sleep(4)
    print("You continue running off into the distance, in search of shelter.")
    time. sleep(3.5)
    print("But shelter does not appear for ages, as more dangers await you.")
    time. sleep(3.5)
    sys.exit()
#Celsius
if word in list2:
    fTemp=input("Alrighty, just give me the temperature right now...")
    print("Just give me a second to put this in...")
    time. sleep(3)
    if "." in fTemp:
        float(fTemp)
    else:
        int(fTemp)
    cTemp=(fTemp-32)*(5/9)
    cTemp=round(cTemp,2)
    cTemp=str(cTemp)
    print("The temperature in Celsius is about "+cTemp+" degre-")
    time. sleep(4)
    print("Hold on, what is your name?")
    time. sleep(3)
    print("Boys, I think we found the fugitive.")
    time. sleep(3)
    print("You realize that they were talking about you and you take off running.")
    time. sleep(4)
    print("The men chase you, but run out of strength after a while, letting you go.")
    time. sleep(4)
    print("You continue running off into the distance, in search of shelter.")
    time. sleep(3.5)
    print("But shelter does not appear for ages, as more dangers await you.")
    time. sleep(3.5)
    sys.exit()



