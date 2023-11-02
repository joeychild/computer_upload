#Import the libraries
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
from yahoo_fin import stock_info as si
import time
list1=["Yes","yes","Y","y"]
list2=["No","no","N","n"]

def stock_history():

    plt.style.use('fivethirtyeight')

    ticker1=input("Please enter the ticker: ")
    year1=input("Please enter the starting year as YYYY: ")
    month1=input("Please enter the starting month as MM: ")
    day1=input("Please enter the starting day as DD: ")
    year2=input("Please enter the ending year as YYYY. If you want the current date, press Enter: ")
    month2=input("Please enter the ending month as MM. If you want the current date, press Enter: ")
    day2=input("Please enter the ending day as DD. If you want the current date, press Enter: ")
    
    ticker1=ticker1.upper()

    starting_date=year1+"-"+month1+"-"+day1
    if year2=="":
        end_date=date.today()
    else:
        end_date=year2+"-"+month2+"-"+day2

    #Get the stock quote 
    df = web.DataReader(ticker1, data_source='yahoo', start=starting_date, end=end_date)

    #Show the data 
    df
    df.shape

    #Visualize the closing price history
    plt.figure(figsize=(16,8))
    plt.title('Close Price History of '+ticker1)
    plt.plot(df['Close'])
    plt.xlabel('Date',fontsize=18)
    plt.ylabel('Close Price USD ($)',fontsize=18)
    plt.show()
def live_price():

    ticker1=input("Please enter a ticker: ")
    ticker1=ticker1.upper()
    stock_price=str(round(si.get_live_price(ticker1),2))
    print("The current stock price of "+ticker1+" is $"+stock_price+".")


while True:
    yes_or_no=input("Would you like to see the live price? ")
    if yes_or_no in list1:
        print("Redirecting...")
        time.sleep(1.5)
        live_price()
    elif yes_or_no in list2:
        print("Okay.")
        time.sleep(1)
    else:
        print("Term not recognized. Rebooting...")
        continue
    yes_or_no=input("Would you like to see the stock history? ")
    if yes_or_no in list1:
        print("Redirecting...")
        time.sleep(1.5)
        stock_history()
    elif yes_or_no in list2:
        print("Okay.")
        time.sleep(1)
    else:
        print("Term not recognized. Rebooting...")
        continue
    yes_or_no=input("Would you like to see the future predictions? ")
    if yes_or_no in list1:
        print("Redirecting...")
        time.sleep(1.5)
        predictions()
    elif yes_or_no in list2:
        print("Okay.")
        time.sleep(1)
    else:
        print("Term not recognized. Rebooting...")
        continue
    yes_or_no=input("Would you like to quit? ")
    if yes_or_no in list1:
        print("Okay. See you later!")
        time.sleep(2)
        break
    elif yes_or_no in list2:
        print("Okay.")
        time.sleep(1)
        continue
    else:
        print("Term not recognized. Rebooting...")
        continue
quit()
    

