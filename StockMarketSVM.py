# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 13:34:57 2022

@author: PIJHUSH
"""

import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

#Get the stock data
df = quandl.get("WIKI/FB")
print(df.head())

#Get the adj close price
df = df[['Adj. Close']]
print(df.head())

#A variable for predicting 'n' days out into the future.
forecast_out = 30
#Create another column (the target or dependent variable) shifted 'n' unit up
df['Prediction'] = df[['Adj. Close']].shift(-1)
#Or we can write
df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)
#Print the new data set
print(df.head())
print(df.tail())

#Create the independent dataset
#Convert the data frame into numpy array
X = np.array(df.drop(['Prediction'],1))
#Remove the last 'n' rows 
X = X[:-forecast_out]
print(X)

#Create the dependent data set (y) 
# Convert the data set to a numpy array (All of the values including the NAN's)
y = np.array(df['Prediction'])
#Get all of the y values except the last 'n' rows
y = y[:-forecast_out]
print(y)


#Split the data into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# Create and train the svm (Regresser)
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_rbf.fit(x_train, y_train)

#Testing model: score return the coefficient of determination R^2 of the prediction
#The best possible score is 1.0
svm_confidence = svr_rbf.score(x_test, y_test)
print("SVM confidence: ", svm_confidence)

#Create and train the linear regression model
lr = LinearRegression()
#Train the model
lr.fit(x_train, y_train)

#Testing model: score return the coefficient of determination R^2 of the prediction
#The best possible score is 1.0
lr_confidence = lr.score(x_test, y_test)
print("LR confidence: ", lr_confidence)


#Set x_forecast equal to the last 30 rows of the original data set from Adj close column

x_forecast = np.array(df.drop(['Prediction'],1))[-forecast_out:]
print(x_forecast)

#Print linear regression model prediction for the next 'n' days
lr_predcition = lr.predict(x_forecast)
print(lr_predcition)


#Print svm model prediction for the next 'n' days
svm_predcition = svr_rbf.predict(x_forecast)
print(svm_predcition)



#Set working directory path 
import os
path="C:/Users/PIJHUSH/Desktop/John/Codes/main"
os.chdir(path)

#Get the working directory path
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))

