
# coding: utf-8

# # Getting started with Python for data science challenges.

# ## Why python ?
# * Because of its rich libraries. [this does not mean others dont have ]
# * You can use Python when your data analysis tasks need to be integrated with web apps.
# * Growing user base.
# 
# There are few disadvantages of Python if you compare it with contenders like R. To qoute one, R's visulization libraries
# are better but Python's visualization libraries like Seaborn are filling up this gap.
# 
# So it's upto you on which one you would go for. 

# ## Getting started with the tutorial.
# * We will be using Kaggle's <a href="https://www.kaggle.com/c/titanic">titanic challenge</a> as a reference for the tutorial. 
# * We will go over
#     * How to read data.
#     * Basics of Numpy and Pandas.
#     * How to use basic models defined in Sci-Kit learn library.
#     
# 

# ## Reading Data using Pandas.
# 

# In[33]:

# import required library
import pandas as pd # now you can refer to pandas library as 'pd' from here on.
import numpy as np

df = pd.read_csv('train_data.csv', header=0)
df.head(5)

#We first split available training data into validation and training data.
train_data=df.ix[0:500,]
validate_data=df.ix[500:,]


# In[42]:

#importing sklearn library.
from sklearn import linear_model

#create a linear regression model
lr=linear_model.LinearRegression()
trainx=train_data.ix[:,2:59]
trainy=train_data.ix[:,60]

#fit the linear model.
lr.fit(trainx,trainy)
#access the coeffcients using 
print("w values for the linear model",lr.coef_)

testx=validate_data.ix[:,2:]
testy=validate_data.ix[:,60]
ypredicted=lr.predict(testx)
predicted_values=pd.DataFrame(ypredicted)

def fun1(x):
    if x>0.5:
        return 1
    else:
        return 0

predicted_labels = predicted_values[0].apply(fun1)

print(predicted_labels.head())
print(testy.head())

