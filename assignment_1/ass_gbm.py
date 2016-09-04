
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



total_data = 26000
total_cols = 61
y_cols = 60
train_data_last = ((total_data)/2)  
#We first split available training data into validation and training data.
train_data=df.ix[0:train_data_last,]
validate_data=df.ix[train_data_last + 1:,]


# In[42]:

#importing sklearn library.
from sklearn import linear_model

#create a linear regression model
lr=linear_model.LinearRegression()
trainx=train_data.ix[:,2:total_cols-2]
trainy=train_data.ix[:,y_cols]

#fit the linear model.
lr.fit(trainx,trainy)
#access the coeffcients using 
print("w values for the linear model",lr.coef_)

testx=validate_data.ix[:,2:total_cols-2]
testy=validate_data.ix[:,y_cols]
ypredicted=lr.predict(testx)
predicted_values=pd.DataFrame(ypredicted)



for i in range(0,10):
	print(validate_data.ix[train_data_last + 1+i,0], testy.ix[train_data_last + 1 + i], predicted_values.ix[i,0])

score = 0
print("score - ",score)
for i in range(0,total_data - train_data_last - 1):
	score += abs(predicted_values.ix[i,0] - testy.ix[train_data_last + 1 + i])

print("score - ",score/(total_data - train_data_last))


# final_test  = pd.read_csv('test_data.csv', header=0)
# test_finalx=final_test.ix[:,2:total_cols-2]
# yfinalpredicted=lr.predict(test_finalx)
# ans_row_size = yfinalpredicted.size

# ans=np.zeros((ans_row_size,2))
# for i in range(0, ans_row_size):
# 	ans[i,0]=i

# ans[:,1] = yfinalpredicted

# np.savetxt("final_output.csv", ans.astype(int),fmt = '%d', delimiter = ',')





