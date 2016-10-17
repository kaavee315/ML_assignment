
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
from sklearn.cross_validation import train_test_split
import random


# In[42]:


df = pd.read_csv('train.csv', header=0)

train_data, validate_data = train_test_split(df, test_size = 0.3)

ans[:,1] = yfinalpredicted
f = open ('output.csv','w')
f.write('id,shares\n')
# print >> f, 'id,shares\n'
np.savetxt(f, ans.astype(int),fmt = '%d', delimiter = ',')
f.close()




