# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oRUxHD8WEvMNOErLF3YutfA_7GZ6_8o7

**Importing Libraries**
"""

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  
import seaborn as sns

"""**Importing Data**"""

dataset= pd.read_csv("boston_train.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

test_dataset= pd.read_csv("boston_test.csv")
x_test = dataset.iloc[:, :-1].values
y_test = dataset.iloc[:, -1].values

dataset.head()

dataset.info()

dataset.describe()

dataset.shape

dataset= dataset.drop('ID', axis=1)

dataset.plot.scatter('rm', 'medv')
#We can see from here that there is a linear relationship between

sns.heatmap(dataset.corr())

sns.pairplot(dataset, vars = ['lstat', 'ptratio', 'indus', 'tax', 'crim', 'nox', 'rad', 'age', 'medv'])

sns.pairplot(dataset, vars = ['rm', 'zn', 'black', 'dis', 'chas','medv'])

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(x,y)

predictions = lm.predict(x_test)

plt.scatter(y_test,predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')

from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))