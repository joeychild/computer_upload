import numpy as np
import csv
from csv import DictReader
from datetime import datetime
import smtplib
import time
from selenium import webdriver
import matplotlib.pyplot as plt
from datetime import date
#For Prediction
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
#For Stock Data
from iexfinance.stocks import Stock
import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd
from datetime import date
from dateutil.rrule import rrule, DAILY
from datetime import timedelta
import plotly.express as px
import plotly.graph_objects as go

start = datetime(2017, 1, 1)
end = datetime.now()
dt=datetime.now()
days=50

stock="AAPL"
#Outputting the Historical data into a .csv for later use
yf.pdr_override()
df = pdr.get_data_yahoo(stock, start=start, end=end)
csv_name = (stock+'.csv')
df.to_csv(csv_name)
df['prediction'] = df['Adj Close'].shift(-1)
df.dropna(inplace=True)
forecast_time = int(days)

X = np.array(df.drop(['prediction'], 1))
Y = np.array(df['prediction'])
X = preprocessing.scale(X)
X_prediction = X[-forecast_time:]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5)

#Performing the Regression on the training data
clf = LinearRegression()
clf.fit(X_train, Y_train)
prediction = (clf.predict(X_prediction))
print(prediction)

#Making a list for the prediction
dates = []

for dt in rrule(DAILY, dtstart=end, until=end+timedelta(days=days)):
    dates.append(dt.strftime("%Y-%m-%d"))
row1=(dates)
row2=(prediction)
rows=list(zip(row1,row2))

#Creating a .csv file for the prediction data
(stock+' Predictions.csv')

#Add prediction data
with open(stock+' Predictions.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    wr.writerow(['Date','Predicted Price'])
    for item in rows:
        wr.writerow(item)

#Plotting everything in
time = (end - start).days
Dates = []
AdjCloses = []
(stock+' Material.csv')
AAPLdata = pd.read_csv(stock+'.csv', skiprows=1)
AAPLdata.to_csv('Raw Data.csv')
with open('Raw Data.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
for item in data:
    Date=item[0]
    AdjClose=item[4]
    Dates.append(Date)
    AdjClose = float(AdjClose)
    AdjCloses.append(AdjClose)
Rows = list(zip(Dates, AdjCloses))
with open('AAPL Material.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for item in Rows:
        wr.writerow(item)

df = pd.read_csv('AAPL Material.csv')
df2 = pd.read_csv('AAPL Predictions.csv')
fig = go.Figure()
fig = px.line(df2,x = 'Date', y = 'Predicted Price', title='Future Stock Predictions of Apple')
fig2 = px.line(df, x = 'Date', y = 'Adjusted Close', title = 'Adjusted Close Prices of Apple')


fig.show()
fig2.show()



