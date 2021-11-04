#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
from warnings import filterwarnings
filterwarnings("ignore")


# In[9]:


#Get the data
uber = pd.read_csv('uberdrive.csv.xls')


# In[10]:


uber


# # Q1. Show the last 10 records of the dataset

# In[6]:


uber.tail(10)


# # Q2.Show the first 10 Records of the dataset 

# In[7]:


uber.head(10)


# # Q3.Show the dimension(number of rows and Column of the dataset)

# In[9]:


#There are two command or attribute to show the dimesion is shape and index

uber.shape


# In[12]:


uber.index


# # Q4.Show the size(Total number of elements) of the dataset

# In[13]:


uber.size


# # Q5. Display the information about all the variables of the dataset.
# What can you infer from the output ?

# # Hint: Information includes- Total number of columns, variable data-types, number of null values in a variable and usage

# In[14]:


uber.info()


# # Q6. Check for missing values or Null values
# 
# #note:output should contain omly one boolen value

# In[16]:


uber.isnull().sum().any()


# # Q7.How many missing values or null values are present in the entire dataset

# In[27]:


uber.isnull().sum().sum()


# # Q8. Get the summary of the original data
# Hint: Sumaary includes Count,Mean,25%,50%,75% and max

# In[23]:


uber.describe(include = 'all')


# # Q9.Drop the missing values and store the data in new dataframe name it uber1 

# In[14]:


uber1 = uber.dropna()
print(uber1.isnull().values.any())
print(uber1.shape)


# # Q10.Check all the information of the dataframe uber1
# Hint: Information includes- Total number of columns, variable data-types, number of null values in a variable and usage

# In[15]:


uber1.info()


# # Q11. Get the unique start locations

# In[17]:


print(uber1['START*'].unique())


# # Q12. What is the total number of unique start locations

# In[11]:


print(uber['START*'].nunique())


# # Q13. What is the total number of unique stop locations

# In[13]:


print(uber['STOP*'].nunique())


# # Q14.Display all Uber trips that has starting point as San Francisco
# 
# NOTE : Use the original dataframes without dropping the 'NA' values

# In[9]:


uber.head(3)


# # Q14. Display all Uber trips that has the starting point as San Francisco.
# 
# #Note: Use the original dataframe without dropping the 'NA' values.

# In[22]:


uber_Start_San_Francisco = uber[uber['START*']== 'San Francisco']
uber_Start_San_Francisco


# # Q15.What is the most popular starting point for the Uber drivers? 
# Note: Use the original dataframe without dropping the 'NA' values.
# Hint:Popular means the place that is visited the most

# In[24]:


uber['START*'].value_counts().head(5)


# # Q16. What is the most popular dropping point for the Uber drivers? 
# Note: Use the original dataframe without dropping the 'NA' values.
# Hint: Popular means the place that is visited the most

# In[25]:


uber['STOP*'].value_counts().head(5)


# # Q17. What is the most frequent route taken by Uber drivers ?
# Note: This question is based on the new dataframe with no 'na' values.
# Hint-Print the most frequent route taken by Uber drivers (Route= combination of START & END points present
# in the Data set).

# In[27]:


uber1.groupby(['START*','STOP*'])['MILES*'].size().sort_values(ascending=
False).head()


# # Q18. Display all types of purposes for the trip in an array. (2 points)
# Note: This question is based on the new dataframe with no 'NA' values.

# In[36]:


print(np.array(uber1['PURPOSE*'].dropna().unique()))


# In[32]:


uber1.head(3)


# # Q19. Plot a bar graph of Purpose vs Miles(Distance). What can you infer from the plot
# Note: Use the original dataframe without dropping the 'NA' values.
# Hint:You have to plot total/sum miles per purpose

# In[37]:


uber.head(4)


# In[39]:


plt.figure(figsize = (15,7))
sns.barplot(x= uber['PURPOSE*'], y = uber['MILES*'],estimator = np.sum,data = uber,ci = None)
plt.show()


# # The graph is showing the purpose of the trip over the distance(Miles*)

# # Q20. Display a dataframe of Purpose and the total distance travelled for that particular Purpose.
# 
# Note: Use the original dataframe without dropping "NA" values

# In[48]:


uber.groupby('PURPOSE*').sum()['MILES*'].sort_values(ascending = False)


# # Q21. Generate a plot showing count of trips vs category of trips. What can you infer from the plot

# In[50]:


uber['CATEGORY*'].value_counts()


# In[ ]:




