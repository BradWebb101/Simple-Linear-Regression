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
asx200 = pd.read_csv('^AXJO.csv', usecols=['Date','Adj Close'], parse_dates=['Date'], index_col=('Date'))
cba = pd.read_csv('CBA.AX.csv', usecols=['Date','Adj Close'], parse_dates=['Date'], index_col=('Date'))
bhp = pd.read_csv('CBA.AX.csv', usecols=['Date','Adj Close'], parse_dates=['Date'], index_col=('Date'))
risk_free = pd.read_csv('f02d.csv')
risk_free = risk_free.iloc[10:,[0,5]]

risk_free.columns = ['Date','10yr_bond']
risk_free['Date'] = pd.to_datetime(risk_free['Date'])
risk_free.set_index('Date',inplace=True)
risk_free['10yr_bond'] = risk_free['10yr_bond'].astype(float)
risk_free = risk_free.loc['2013-06-03':'2019-01-14']

#Creating an price array
df = pd.DataFrame()
df['CBA Stock Price'] = cba['Adj Close']
df['ASX Index Price'] = asx200['Adj Close']
df = df.loc['2013-06-03':'2019-01-14']

#Plot Price Data using Matplotlib
fig = plt.figure()
fig, axes = plt.subplots(nrows=2, ncols=1)

axes[0].plot(df['CBA Stock Price'])
axes[1].plot(df['ASX Index Price'])

#Adding in Risk Free data
df['Daily Risk Free Return'] = risk_free['10yr_bond'] / 100 / 365
df = df.fillna(method='bfill')

#Adding in return data to array
df['CBA Log Return'] = np.log(df['CBA Stock Price']) - np.log(df['CBA Stock Price'].shift(1))
df['ASX Log Index Return'] = np.log(df['ASX Index Price']) - np.log(df['ASX Index Price'].shift(1))

#Adding in Excess return
df['CBA Log Excess'] = df['CBA Log Return'] - df['Daily Risk Free Return']
df['ASX Log Index Excess'] = df['ASX Log Index Return'] - df['Daily Risk Free Return']
df = df.dropna()

#Pairplot of return data
sns.pairplot(df,vars=['CBA Log Return','ASX Log Index Excess'])

#Visualising Linerarity with matplotlib
fig1 = plt.figure()

fig, axes = plt.subplots(nrows=2, ncols=1)

axes[0].plot(df['CBA Log Return'])
axes[1].plot(df['ASX Log Index Excess'])

#Linear Regression 
reg_matrix = np.matrix(df[['CBA Log Excess','ASX Log Index Excess']])
X, y = reg_matrix[:,0], reg_matrix[:,1]

mdl = LinearRegression().fit(X,y)
 
m = mdl.coef_[0]
b = mdl.intercept_
 
print('Formula: y = {1} + {0}x + e'.format(m, b))
 
 
 

