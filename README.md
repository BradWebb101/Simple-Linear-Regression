## Simple Linear Regression

This project was to get a better understanding of data manipulation in Pandas. As I am pulling multiple data from a variety of sources (Yahoo Fiance and RBA Finance Data).

I use the excess return of the stocks (Stock return - Risk Free Rate) and regress over the excess return on the market (ASX200 - Risk Free Rate)

Problems i had were that import XLS does not recognise numbers as floats or integers which created problems in extracting the data into a data frame. 

Due to this i used a large quantity of .iloc to manipulate the data into a data frame. 

For this project i was looking at a simple CAPM linear model to understand how CBA, BHP, TLS, WES bank moves compared to the ASX200 (Market index proxy), Risk free is AU gov bond 10yr bond.

From looking at the outputs BETA seems quite low compared to what is expected. Will review the code and double check the inputs.

This code was teh first attempt at writing a code for Python, therefore it does not use any loops and is a lot of repeating commands. 

For future code i use loops where approriate to reduce the repitition of code. One positive is it is very easy to follow the code as a beginner

I used CSV's downloaded from Yahoo Finance as i am unable to find a free API for AX stocks at this time. Future project will look at building a API for yahoo finance to download data.