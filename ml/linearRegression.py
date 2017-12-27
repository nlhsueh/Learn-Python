#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Salary_Data.csv')

X = dataset.iloc[:, :-1].values #除了最後一個 colunmn 的所有值
y = dataset.iloc[:, 1].values #最後一個 column

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Feature Scaling

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the Training set results
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Training set')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')

# Visualising the Test set results
plt.subplot(1,2,2)
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_test, regressor.predict(X_test), color = 'blue')
plt.title('Test set')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.savefig('images/regressionSalary.png')