import sys
import math
x=0
list1=["Help","help"]
list2=["+","-","*","/","^"]
list3=["rt","nlog","log","rem","perm","com","abs","fact","cos","sin","tan","acos","asin","atan","rad","deg"]
list4=["cos","sin","tan","acos","asin","atan"]
list5=["Yes","yes","y"]
list6=["No","no","n"]
list7=["Pi","pi"]
list8=["E","e"]
answer=0
while True:
    #First number
    number=input("Please enter a number. You can also enter pi or e. ")
    if number in list7:
        number=math.pi
    elif number in list8:
        number=math.e
    elif x==0:
        try:
            number=float(number)
        except ValueError:
            print("Term not recognized. Please try again.")
            continue
    else:
        number=float(number)
    #Second number
    number2=input("Please enter a number. You can also enter pi or e. ")
    if number2 in list7:
        number2=math.pi
    elif number2 in list8:
        number2=math.e
    elif x==0:
        try:
            number2=float(number2)
        except ValueError:
            print("Term not recognized. Please try again.")
            continue
    else:
        number2=float(number2)
    #Operator
    operator=input("Please enter an operator. If you do not know what operators you can enter, please enter Help. ")
    if operator in list1:
        print("The operators you can use are the following; + for addition, - for subtraction, * for multiplication, / for division, ^ for exponents, and rt for roots.")
        print("There are also special functions. They are: nlog for natural logarithm, log for logarithm, rem for the remainder, perm for a permutation, com for a combination,")
        print("abs for the absolute value, and fact for the factorial.")
        print("There's also a few more: cos for cosine, sin for sine, tan for tangent, acos for arc cosine, asin for arc sine, and atan for arc tangent.")
        print("And finally, for angular conversions, rad is for degree to radian conversion and deg is for radian to degree conversion.")
        print("For exponents, the first number is the base.")
        print("Roots are interesting. The first number is the radicand (The number getting square-rooted) while the second number is the radicand (square, cube, etc.).")
        print("For natural logarithms, only the first number is accounted for.")
        print("For logarithms, the second number is the base.")
        print("For permutations and combinations,the first number is n and the second number is k.")
        print("For absolute values and factorials, only the first number is accounted for.")
        print("Finally, both angular conversions only account for the first number.")
        operator=input("Please enter an operator. ")
        if operator in list2:
            pass
        elif operator in list3:
            pass
        else:
            print("Term not recognized. Please try again.")
            continue
    elif operator in list2:
        pass
    elif operator in list3:
        pass
    else:
        print("Term not recognized. Please try again.")
        continue
    #Mathematics
    if operator=="+":
        answer=number+number2
        number=str(number)
        number2=str(number2)
        answer=str(answer)
        print("The sum of "+number+" and "+number2+" is "+answer+".")
    elif operator=="-":
        answer=number-number2
        number=str(number)
        number2=str(number2)
        answer=str(answer)
        print("The difference of "+number+" and "+number2+" is "+answer+".")    
    elif operator=="*":
        answer=number*number2
        number=str(number)
        number2=str(number2)
        answer=str(answer)
        print("The product of "+number+" and "+number2+" is "+answer+".")
    elif operator=="/":
        answer=number/number2
        number=str(number)
        number2=str(number2)
        answer=str(answer)
        print("The quotient of "+number+" and "+number2+" is "+answer+".")    
    elif operator=="^":
        answer=number**number2
        number=str(number)
        number2=str(number2)
        answer=str(answer)
        print(number+" raised to the "+number2+" is "+answer+".")
    elif operator=="rt":
        answer=number**(1/number2)
        number=str(number)
        number2=str(number2)
        answer=str(answer)
        print("The "+number2+" root of "+number+" is "+answer+".")
    elif operator=="nlog":
        answer=math.log(number)
        number=str(number)
        answer=str(answer)
        print("The natural logarithm of "+number+" is "+answer+".")
    elif operator=="log":
        answer=math.log(number,number2)
        number=str(number)
        number2=str(number2)
        answer=str(answer)
        print("The logarithm of "+number+" in base "+number2+" is "+answer+".")
    elif operator=="rem":
        answer=number%number2
        number=str(number)
        number2=str(number2)
        answer=str(answer)
        print("The remainder of "+number+" divided by "+number2+" is "+answer+".")
    elif operator=="perm":
        answer=math.perm(number,number2)
        number=str(number)
        number2=str(number2)
        answer=str(answer)
        print("There are "+answer+" different ways to put "+number2+ " items out of "+number+" total items when order matters.")
    elif operator=="com":
        answer=math.comb(number, number2)
        number=str(number)
        number2=str(number2)
        answer=str(answer)
        print("There are "+answer+" different ways to put "+number2+ " items out of "+number+" total items when order doesn't matter.")
    elif operator=="abs":
        answer=math.fabs(number)
        number=str(number)
        answer=str(answer)
        print("The absolute value of "+number+" is "+answer+".")
    elif operator=="fact":
        answer=math.factorial(number)
        number=str(number)
        answer=str(answer)
        print("The factorial of "+number+" is "+answer+".")
    elif operator=="cos":
        answer=math.cos(number)
        convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
        if convert in list5:
            answer=(answer/math.pi)*180
            number=str(number)
            answer=str(answer)
            print("The cosine of "+number+" is "+answer+".")
        elif convert in list6:
            answer=(answer/math.pi)
            number=str(number)
            answer=str(answer)
            print("The cosine of "+number+" is "+answer+" pi.")
        else:
            print("Term not recognized. Please try again.")
            continue
    elif operator=="sin":
        answer=math.sin(number)
        convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
        if convert in list5:
            answer=(answer/math.pi)*180
            number=str(number)
            answer=str(answer)
            print("The sine of "+number+" is "+answer+".")
        elif convert in list6:
            answer=(answer/math.pi)
            number=str(number)
            answer=str(answer)
            print("The sine of "+number+" is "+answer+" pi.")
        else:
            print("Term not recognized. Please try again.")
            continue
    elif operator=="tan":
        answer=math.tan(number)
        convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
        if convert in list5:
            answer=(answer/math.pi)*180
            number=str(number)
            answer=str(answer)
            print("The tangent of "+number+" is "+answer+".")
        elif convert in list6:
            answer=(answer/math.pi)
            number=str(number)
            answer=str(answer)
            print("The tangent of "+number+" is "+answer+" pi.")
        else:
            print("Term not recognized. Please try again.")
            continue
    elif operator=="acos":
        answer=math.acos(number)
        convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
        if convert in list5:
            answer=(answer/math.pi)*180
            number=str(number)
            answer=str(answer)
            print("The arc cosine of "+number+" is "+answer+".")
        elif convert in list6:
            answer=(answer/math.pi)
            number=str(number)
            answer=str(answer)
            print("The arc cosine of "+number+" is "+answer+" pi.")
        else:
            print("Term not recognized. Please try again.")
            continue
    elif operator=="asin":
        answer=math.asin(number)
        convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
        if convert in list5:
            answer=(answer/math.pi)*180
            number=str(number)
            answer=str(answer)
            print("The arc sine of "+number+" is "+answer+".")
        elif convert in list6:
            answer=(answer/math.pi)
            number=str(number)
            answer=str(answer)
            print("The arc sine of "+number+" is "+answer+" pi.")
        else:
            print("Term not recognized. Please try again.")
            continue
    elif operator=="atan":
        answer=math.atan(number)
        convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
        if convert in list5:
            answer=(answer/math.pi)*180
            number=str(number)
            answer=str(answer)
            print("The arc tangent of "+number+" is "+answer+".")
        elif convert in list6:
            answer=(answer/math.pi)
            number=str(number)
            answer=str(answer)
            print("The arc tangent of "+number+" is "+answer+" pi.")
        else:
            print("Term not recognized. Please try again.")
            continue
    elif operator=="rad":
        answer=(number/180)
        number=str(number)
        answer=str(answer)
        print(number+" degrees is "+answer+" pi radians.")
    elif operator=="deg":
        answer=(number/math.pi)*180
        number=(number/math.pi)
        number=str(number)
        answer=str(answer)
        print(number+" pi radians is "+answer+" degrees.")
    else:
        print("Term not recognized. Please try again.")
        continue
    #Continue
    while True:
        continue1=input("Would you like to continue? ")
        if continue1 in list6:
            print("Okay.")
            quit()
        elif continue1 in list5:
            pass
        else:
            print("Term not recognized. Please try again.")
            continue
    #Clear
        clear=input("Would you like to clear your results? ")
        if clear in list5:
            print("Okay.")
            #First number
            number=input("Please enter a number. You can also enter pi or e. ")
            if number in list7:
                number=math.pi
            elif number in list8:
                number=math.e
            elif x==0:
                try:
                    number=float(number)
                except ValueError:
                    print("Term not recognized. Please try again.")
                    continue
            else:
                number=float(number)
            #Second Number
            number2=input("Please enter a number. You can also enter pi or e. ")
            if number2 in list7:
                number2=math.pi
            elif number2 in list8:
                number2=math.e
            elif x==0:
                try:
                    number2=float(number2)
                except ValueError:
                    print("Term not recognized. Please try again.")
                    continue
            else:
                number2=float(number2)
            #Operator
            operator=input("Please enter an operator. If you do not know what operators you can enter, please enter Help. ")
            if operator in list1:
                print("The operators you can use are the following; + for addition, - for subtraction, * for multiplication, / for division, ^ for exponents, and rt for roots.")
                print("There are also special functions. They are: nlog for natural logarithm, log for logarithm, rem for the remainder, perm for a permutation, com for a combination,")
                print("abs for the absolute value, and fact for the factorial.")
                print("There's also a few more: cos for cosine, sin for sine, tan for tangent, acos for arc cosine, asin for arc sine, and atan for arc tangent.")
                print("And finally, for angular conversions, rad is for degree to radian conversion and deg is for radian to degree conversion.")
                print("For exponents, the first number is the base.")
                print("Roots are interesting. The first number is the radicand (The number getting square-rooted) while the second number is the radicand (square, cube, etc.).")
                print("For natural logarithms, only the first number is accounted for.")
                print("For logarithms, the second number is the base.")
                print("For permutations and combinations,the first number is n and the second number is k.")
                print("For absolute values and factorials, only the first number is accounted for.")
                print("Finally, both angular conversions only account for the first number.")
                operator=input("Please enter an operator. ")
                if operator in list2:
                    pass
                elif operator in list3:
                    pass
                else:
                    print("Term not recognized. Please try again.")
                    continue
            elif operator in list2:
                pass
            elif operator in list3:
                pass
            else:
                print("Term not recognized. Please try again.")
                continue
            #Mathematics
            if operator=="+":
                answer=number+number2
                number=str(number)
                number2=str(number2)
                answer=str(answer)
                print("The sum of "+number+" and "+number2+" is "+answer+".")
            elif operator=="-":
                answer=number-number2
                number=str(number)
                number2=str(number2)
                answer=str(answer)
                print("The difference of "+number+" and "+number2+" is "+answer+".")    
            elif operator=="*":
                answer=number*number2
                number=str(number)
                number2=str(number2)
                answer=str(answer)
                print("The product of "+number+" and "+number2+" is "+answer+".")
            elif operator=="/":
                answer=number/number2
                number=str(number)
                number2=str(number2)
                answer=str(answer)
                print("The quotient of "+number+" and "+number2+" is "+answer+".")    
            elif operator=="^":
                answer=number**number2
                number=str(number)
                number2=str(number2)
                answer=str(answer)
                print(number+" raised to the "+number2+" is "+answer+".")
            elif operator=="rt":
                answer=number**(1/number2)
                number=str(number)
                number2=str(number2)
                answer=str(answer)
                print("The "+number2+" root of "+number+" is "+answer+".")
            elif operator=="nlog":
                answer=math.log(number)
                number=str(number)
                answer=str(answer)
                print("The natural logarithm of "+number+" is "+answer+".")
            elif operator=="log":
                answer=math.log(number,number2)
                number=str(number)
                number2=str(number2)
                answer=str(answer)
                print("The logarithm of "+number+" in base "+number2+" is "+answer+".")
            elif operator=="rem":
                answer=number%number2
                number=str(number)
                number2=str(number2)
                answer=str(answer)
                print("The remainder of "+number+" divided by "+number2+" is "+answer+".")
            elif operator=="perm":
                answer=math.perm(number,number2)
                number=str(number)
                number2=str(number2)
                answer=str(answer)
                print("There are "+answer+" different ways to put "+number2+ " items out of "+number+" total items when order matters.")
            elif operator=="com":
                answer=math.comb(number, number2)
                number=str(number)
                number2=str(number2)
                answer=str(answer)
                print("There are "+answer+" different ways to put "+number2+ " items out of "+number+" total items when order doesn't matter.")
            elif operator=="abs":
                answer=math.fabs(number)
                number=str(number)
                answer=str(answer)
                print("The absolute value of "+number+" is "+answer+".")
            elif operator=="fact":
                answer=math.factorial(number)
                number=str(number)
                answer=str(answer)
                print("The factorial of "+number+" is "+answer+".")
            elif operator=="cos":
                answer=math.cos(number)
                convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
                if convert in list5:
                    answer=(answer/math.pi)*180
                    number=str(number)
                    answer=str(answer)
                    print("The cosine of "+number+" is "+answer+".")
                elif convert in list6:
                    answer=(answer/math.pi)
                    number=str(number)
                    answer=str(answer)
                    print("The cosine of "+number+" is "+answer+" pi.")
                else:
                    print("Term not recognized. Please try again.")
                    continue
            elif operator=="sin":
                answer=math.sin(number)
                convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
                if convert in list5:
                    answer=(answer/math.pi)*180
                    number=str(number)
                    answer=str(answer)
                    print("The sine of "+number+" is "+answer+".")
                elif convert in list6:
                    answer=(answer/math.pi)
                    number=str(number)
                    answer=str(answer)
                    print("The sine of "+number+" is "+answer+" pi.")
                else:
                    print("Term not recognized. Please try again.")
                    continue
            elif operator=="tan":
                answer=math.tan(number)
                convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
                if convert in list5:
                    answer=(answer/math.pi)*180
                    number=str(number)
                    answer=str(answer)
                    print("The tangent of "+number+" is "+answer+".")
                elif convert in list6:
                    answer=(answer/math.pi)
                    number=str(number)
                    answer=str(answer)
                    print("The tangent of "+number+" is "+answer+" pi.")
                else:
                    print("Term not recognized. Please try again.")
                    continue
            elif operator=="acos":
                answer=math.acos(number)
                convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
                if convert in list5:
                    answer=(answer/math.pi)*180
                    number=str(number)
                    answer=str(answer)
                    print("The arc cosine of "+number+" is "+answer+".")
                elif convert in list6:
                    answer=(answer/math.pi)
                    number=str(number)
                    answer=str(answer)
                    print("The arc cosine of "+number+" is "+answer+" pi.")
                else:
                    print("Term not recognized. Please try again.")
                    continue
            elif operator=="asin":
                answer=math.asin(number)
                convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
                if convert in list5:
                    answer=(answer/math.pi)*180
                    number=str(number)
                    answer=str(answer)
                    print("The arc sine of "+number+" is "+answer+".")
                elif convert in list6:
                    answer=(answer/math.pi)
                    number=str(number)
                    answer=str(answer)
                    print("The arc sine of "+number+" is "+answer+" pi.")
                else:
                    print("Term not recognized. Please try again.")
                    continue
            elif operator=="atan":
                answer=math.atan(number)
                convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
                if convert in list5:
                    answer=(answer/math.pi)*180
                    number=str(number)
                    answer=str(answer)
                    print("The arc tangent of "+number+" is "+answer+".")
                elif convert in list6:
                    answer=(answer/math.pi)
                    number=str(number)
                    answer=str(answer)
                    print("The arc tangent of "+number+" is "+answer+" pi.")
                else:
                    print("Term not recognized. Please try again.")
                    continue
            elif operator=="rad":
                answer=(number/180)
                number=str(number)
                answer=str(answer)
                print(number+" degrees is "+answer+" pi radians.")
            elif operator=="deg":
                answer=(number/math.pi)*180
                number=(number/math.pi)
                number=str(number)
                answer=str(answer)
                print(number+" pi radians is "+answer+" degrees.")
            continue
        elif clear in list6:
            pass
        else:
            print("Term not recognized. Please try again.")
            continue
        #Continue Function
        number=answer
        number2=input("Please enter a number. You can also enter pi or e. ")
        if number2 in list7:
            number2=math.pi
        elif number2 in list8:
            number2=math.e
        elif x==0:
            try:
                number2=float(number2)
            except ValueError:
                print("Term not recognized. Please try again.")
                continue
        else:
            number2=float(number2)
        #Operator
        operator=input("Please enter an operator. If you do not know what operators you can enter, please enter Help. ")
        if operator in list1:
            print("The operators you can use are the following; + for addition, - for subtraction, * for multiplication, / for division, ^ for exponents, and rt for roots.")
            print("There are also special functions. They are: nlog for natural logarithm, log for logarithm, rem for the remainder, perm for a permutation, com for a combination,")
            print("abs for the absolute value, and fact for the factorial.")
            print("There's also a few more: cos for cosine, sin for sine, tan for tangent, acos for arc cosine, asin for arc sine, and atan for arc tangent.")
            print("And finally, for angular conversions, rad is for degree to radian conversion and deg is for radian to degree conversion.")
            print("For exponents, the first number is the base.")
            print("Roots are interesting. The first number is the radicand (The number getting square-rooted) while the second number is the radicand (square, cube, etc.).")
            print("For natural logarithms, only the first number is accounted for.")
            print("For logarithms, the second number is the base.")
            print("For permutations and combinations,the first number is n and the second number is k.")
            print("For absolute values and factorials, only the first number is accounted for.")
            print("Finally, both angular conversions only account for the first number.")
            operator=input("Please enter an operator. ")
            if operator in list2:
                pass
            elif operator in list3:
                pass
            else:
                print("Term not recognized. Please try again.")
                continue
        elif operator in list2:
            pass
        elif operator in list3:
            pass
        else:
            print("Term not recognized. Please try again.")
            continue
        #Mathematics
        if operator=="+":
            answer=number+number2
            number=str(number)
            number2=str(number2)
            answer=str(answer)
            print("The sum of "+number+" and "+number2+" is "+answer+".")
        elif operator=="-":
            answer=number-number2
            number=str(number)
            number2=str(number2)
            answer=str(answer)
            print("The difference of "+number+" and "+number2+" is "+answer+".")    
        elif operator=="*":
            answer=number*number2
            number=str(number)
            number2=str(number2)
            answer=str(answer)
            print("The product of "+number+" and "+number2+" is "+answer+".")
        elif operator=="/":
            answer=number/number2
            number=str(number)
            number2=str(number2)
            answer=str(answer)
            print("The quotient of "+number+" and "+number2+" is "+answer+".")    
        elif operator=="^":
            answer=number**number2
            number=str(number)
            number2=str(number2)
            answer=str(answer)
            print(number+" raised to the "+number2+" is "+answer+".")
        elif operator=="rt":
            answer=number**(1/number2)
            number=str(number)
            number2=str(number2)
            answer=str(answer)
            print("The "+number2+" root of "+number+" is "+answer+".")
        elif operator=="nlog":
            answer=math.log(number)
            number=str(number)
            answer=str(answer)
            print("The natural logarithm of "+number+" is "+answer+".")
        elif operator=="log":
            answer=math.log(number,number2)
            number=str(number)
            number2=str(number2)
            answer=str(answer)
            print("The logarithm of "+number+" in base "+number2+" is "+answer+".")
        elif operator=="rem":
            answer=number%number2
            number=str(number)
            number2=str(number2)
            answer=str(answer)
            print("The remainder of "+number+" divided by "+number2+" is "+answer+".")
        elif operator=="perm":
            answer=math.perm(number,number2)
            number=str(number)
            number2=str(number2)
            answer=str(answer)
            print("There are "+answer+" different ways to put "+number2+ " items out of "+number+" total items when order matters.")
        elif operator=="com":
            answer=math.comb(number, number2)
            number=str(number)
            number2=str(number2)
            answer=str(answer)
            print("There are "+answer+" different ways to put "+number2+ " items out of "+number+" total items when order doesn't matter.")
        elif operator=="abs":
            answer=math.fabs(number)
            number=str(number)
            answer=str(answer)
            print("The absolute value of "+number+" is "+answer+".")
        elif operator=="fact":
            answer=math.factorial(number)
            number=str(number)
            answer=str(answer)
            print("The factorial of "+number+" is "+answer+".")
        elif operator=="cos":
            answer=math.cos(number)
            convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
            if convert in list5:
                answer=(answer/math.pi)*180
                number=str(number)
                answer=str(answer)
                print("The cosine of "+number+" is "+answer+".")
            elif convert in list6:
                answer=(answer/math.pi)
                number=str(number)
                answer=str(answer)
                print("The cosine of "+number+" is "+answer+" pi.")
            else:
                print("Term not recognized. Please try again.")
                continue
        elif operator=="sin":
            answer=math.sin(number)
            convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
            if convert in list5:
                answer=(answer/math.pi)*180
                number=str(number)
                answer=str(answer)
                print("The sine of "+number+" is "+answer+".")
            elif convert in list6:
                answer=(answer/math.pi)
                number=str(number)
                answer=str(answer)
                print("The sine of "+number+" is "+answer+" pi.")
            else:
                print("Term not recognized. Please try again.")
                continue
        elif operator=="tan":
            answer=math.tan(number)
            convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
            if convert in list5:
                answer=(answer/math.pi)*180
                number=str(number)
                answer=str(answer)
                print("The tangent of "+number+" is "+answer+".")
            elif convert in list6:
                answer=(answer/math.pi)
                number=str(number)
                answer=str(answer)
                print("The tangent of "+number+" is "+answer+" pi.")
            else:
                print("Term not recognized. Please try again.")
                continue
        elif operator=="acos":
            answer=math.acos(number)
            convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
            if convert in list5:
                answer=(answer/math.pi)*180
                number=str(number)
                answer=str(answer)
                print("The arc cosine of "+number+" is "+answer+".")
            elif convert in list6:
                answer=(answer/math.pi)
                number=str(number)
                answer=str(answer)
                print("The arc cosine of "+number+" is "+answer+" pi.")
            else:
                print("Term not recognized. Please try again.")
                continue
        elif operator=="asin":
            answer=math.asin(number)
            convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
            if convert in list5:
                answer=(answer/math.pi)*180
                number=str(number)
                answer=str(answer)
                print("The arc sine of "+number+" is "+answer+".")
            elif convert in list6:
                answer=(answer/math.pi)
                number=str(number)
                answer=str(answer)
                print("The arc sine of "+number+" is "+answer+" pi.")
            else:
                print("Term not recognized. Please try again.")
                continue
        elif operator=="atan":
            answer=math.atan(number)
            convert=input("If you would like your answer in degrees, please enter Yes. Otherwise, please enter No. ")
            if convert in list5:
                answer=(answer/math.pi)*180
                number=str(number)
                answer=str(answer)
                print("The arc tangent of "+number+" is "+answer+".")
            elif convert in list6:
                answer=(answer/math.pi)
                number=str(number)
                answer=str(answer)
                print("The arc tangent of "+number+" is "+answer+" pi.")
            else:
                print("Term not recognized. Please try again.")
                continue
        elif operator=="rad":
            answer=(number/180)
            number=str(number)
            answer=str(answer)
            print(number+" degrees is "+answer+" pi radians.")
        elif operator=="deg":
            answer=(number/math.pi)*180
            number=(number/math.pi)
            number=str(number)
            answer=str(answer)
            print(number+" pi radians is "+answer+" degrees.")




