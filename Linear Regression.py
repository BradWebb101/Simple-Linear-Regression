#!/usr/bin/env python
# coding: utf-8

# In[107]:


#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


# In[108]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[109]:


#Defining Variables from CSV Data
df1 = pd.read_csv('BHP.csv')
df2 = pd.read_csv('CBA.csv')
df3 = pd.read_csv('WES.csv')
df4 = pd.read_csv('TLS.csv')
df5 = pd.read_csv('AXJO.csv')


# In[110]:


#Removing data not required
bhp = df1['Adj Close']
cba = df2['Adj Close']
wes = df3['Adj Close']
tls = df4['Adj Close']
xjo = df5['Adj Close']


# In[111]:


#Creating Array for required variables
frames = [bhp, cba, wes, tls,xjo]
array = pd.concat(frames,axis=1)
array.columns = ['BHP','CBA','WES','TLS','XJO']


# In[112]:


#Checking data is correct
array.head(5)


# In[123]:


#Removing Nan from data from
array.fillna(method='bfill')


# In[124]:


#Plotting Price data using subplots 
fig, axes = plt.subplots(2,2)
print('Changing Layouts')
plt.tight_layout()
print('Preparing Graphs')
axes[0,0].plot(date,bhp)
axes[0,0].set_title('BHP Daily Price Data')
axes[0,1].plot(date,cba)
axes[0,1].set_title('CBA Daily Price Data')
axes[1,0].plot(date,wes)
axes[1,0].set_title('WES Daily Price Data')
axes[1,1].plot(date,tls)
axes[1,1].set_title('TLS Daily Price Data')
print('Complete')


# In[125]:


sns.pairplot(array)


# In[126]:


#Calculating Log Return Data 
array['BHP_log_returns'] = np.log(array.BHP / array.BHP.shift())
array['CBA_log_returns'] = np.log(array.CBA / array.CBA.shift())
array['WES_log_returns'] = np.log(array.WES / array.WES.shift())
array['TLS_log_returns'] = np.log(array.TLS / array.TLS.shift())
array['XJO_log_returns'] = np.log(array.XJO / array.XJO.shift())


# In[ ]:


#Assigning the variables to the array
BHP_log_returns = array['BHP_log_returns'][1:]
CBA_log_returns = array['CBA_log_returns'][1:]
WES_log_returns = array['WES_log_returns'][1:]
TLS_log_returns = array['TLS_log_returns'][1:]
XJO_log_returns = array['XJO_log_returns'][1:]


# In[127]:


#Plotting Price data using subplots 
fig1, axes = plt.subplots(2,2)
print('Changing Layouts')
plt.tight_layout
print('Preparing Graphs')
axes[0,0].plot(date,BHP_log_returns)
axes[0,0].set_title('BHP Daily Log Returns')
axes[0,1].plot(date,CBA_log_returns)
axes[0,1].set_title('CBA Daily Log Returns')
axes[1,0].plot(date,WES_log_returns)
axes[1,0].set_title('WES Daily Log Returns')
axes[1,1].plot(date,TLS_log_returns)
axes[1,1].set_title('TLS Daily Log Returns')
print('Complete')


# In[128]:


#Removing price data from array
array.drop('BHP',axis=1,inplace=True)
array.drop('CBA',axis=1,inplace=True)
array.drop('WES',axis=1,inplace=True)
array.drop('TLS',axis=1,inplace=True)
array.drop('XJO',axis=1,inplace=True)


# In[129]:


#Checking all data looks good
array.head(5)


# In[135]:


#Removing NaN value created from retrn data
array.drop([0],inplace=True)


# In[136]:


array.fillna(value='0')


# In[137]:


sns.pairplot(array)


# In[ ]:




