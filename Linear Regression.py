# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 17:05:14 2019

@author: bradw
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
from sklearn.linear_model import LinearRegression

style.use('ggplot')

#Importing and cleaning the data
asx200 = pd.read_csv('AXJO.csv', usecols=['Date','Adj Close'], parse_dates=['Date'], index_col=('Date'))
cba = pd.read_csv('CBA.csv', usecols=['Date','Adj Close'], parse_dates=['Date'], index_col=('Date'))
bhp = pd.read_csv('BHP.csv', usecols=['Date','Adj Close'], parse_dates=['Date'], index_col=('Date'))
tls = pd.read_csv('TLS.csv', usecols=['Date','Adj Close'], parse_dates=['Date'], index_col=('Date'))
wes = pd.read_csv('WES.csv', usecols=['Date','Adj Close'], parse_dates=['Date'], index_col=('Date'))
risk_free = pd.read_excel('f02d.xls')
risk_free = risk_free.iloc[10:,[0,5]]

risk_free.columns = ['Date','10yr_bond']
risk_free['Date'] = pd.to_datetime(risk_free['Date'])
risk_free.set_index('Date',inplace=True)
risk_free['10yr_bond'] = risk_free['10yr_bond'].astype(float)
risk_free = risk_free.loc['2013-06-03':'2019-01-14']

#Creating an price array
df = pd.DataFrame()
df['CBA Stock Price'] = cba['Adj Close']
df['BHP Stock Price'] = bhp['Adj Close']
df['TLS Stock Price'] = tls['Adj Close']
df['WES Stock Price'] = wes['Adj Close']
df['ASX Index Price'] = asx200['Adj Close']
df = df.loc['2013-06-03':'2019-01-14']

#Plot Price Data using Matplotlib
fig = plt.figure()
fig, axes = plt.subplots(nrows=2, ncols=2)

axes[0,0].plot(df['CBA Stock Price'])
axes[0,1].plot(df['BHP Stock Price'])
axes[1,0].plot(df['TLS Stock Price'])
axes[1,1].plot(df['WES Stock Price'])

#Adding in Risk Free data
df['Daily Risk Free Return'] = risk_free['10yr_bond'] / 100 / 365
df = df.fillna(method='bfill')

#Adding in return data to array
df['CBA Log Return'] = np.log(df['CBA Stock Price']) - np.log(df['CBA Stock Price'].shift(1))
df['BHP Log Return'] = np.log(df['BHP Stock Price']) - np.log(df['BHP Stock Price'].shift(1))
df['TLS Log Return'] = np.log(df['TLS Stock Price']) - np.log(df['TLS Stock Price'].shift(1))
df['WES Log Return'] = np.log(df['WES Stock Price']) - np.log(df['WES Stock Price'].shift(1))
df['ASX Log Index Return'] = np.log(df['ASX Index Price']) - np.log(df['ASX Index Price'].shift(1))

#Adding in Excess return
df['CBA Log Excess'] = df['CBA Log Return'] - df['Daily Risk Free Return']
df['BHP Log Excess'] = df['BHP Log Return'] - df['Daily Risk Free Return']
df['TLS Log Excess'] = df['TLS Log Return'] - df['Daily Risk Free Return']
df['WES Log Excess'] = df['WES Log Return'] - df['Daily Risk Free Return']
df['ASX Log Index Excess'] = df['ASX Log Index Return'] - df['Daily Risk Free Return']
df = df.dropna()

#Pairplot of return data
sns.pairplot(df,vars=['CBA Log Return', 'BHP Log Return', 'TLS Log Return', 'WES Log Return', 'ASX Log Index Excess'])

#Visualising Linerarity with matplotlib
fig1 = plt.figure()

fig, axes = plt.subplots(nrows=2, ncols=2)

axes[0,0].plot(df['CBA Log Return'])
axes[0,1].plot(df['BHP Log Return'])
axes[1,0].plot(df['TLS Log Return'])
axes[1,1].plot(df['WES Log Return'])


#Linear Regression 
CBA_y = df[['CBA Log Excess']]
BHP_y = df[['BHP Log Excess']]
TLS_y = df[['TLS Log Excess']]
WES_y = df[['WES Log Excess']]
X = df[['ASX Log Index Excess']]

#Calculating Beta from sample
CBA_beta = LinearRegression().fit(CBA_y,X)
BHP_beta = LinearRegression().fit(BHP_y,X)
TLS_beta = LinearRegression().fit(TLS_y,X)
WES_beta = LinearRegression().fit(WES_y,X)



#Displaying calculated beta
CBA_m = CBA_beta.coef_[0]
CBA_b = CBA_beta.intercept_
 
print('CBA Linear regression')
print('Formula: y = {1} + {0}x + e'.format(CBA_m, CBA_b))

BHP_m = BHP_beta.coef_[0]
BHP_b = BHP_beta.intercept_
 
print('BHP Linear regression')
print('Formula: y = {1} + {0}x + e'.format(BHP_m, BHP_b))

TLS_m = TLS_beta.coef_[0]
TLS_b = TLS_beta.intercept_
 
print('TLS Linear regression')
print('Formula: y = {1} + {0}x + e'.format(TLS_m, TLS_b))

WES_m = WES_beta.coef_[0]
WES_b = WES_beta.intercept_
 
print('TLS Linear regression')
print('Formula: y = {1} + {0}x + e'.format(WES_m, WES_b))

