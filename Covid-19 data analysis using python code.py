#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# # Covid-19 data analysis

# In[9]:


data=pd.read_csv(r"C:\Users\EMON\Downloads\Covid-19 data2.csv.csv")
data.head()


# In[12]:


data.count()


# In[16]:


data.isnull().sum()


# In[17]:


sns.heatmap(data.isnull())
plt.show()


# # Now,show confirmed,Deaths and recovered cases in each region

# In[18]:


data.head(2)


# In[21]:


data.groupby('Region').sum().head(20)


# In[25]:


data.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(20)


# data.groupby('Region')['Recovered'].sum().sort_values(ascending=False).head(20)

# In[30]:


data.groupby('Region')['Recovered'].sum().sort_values(ascending=False).head(20)


# # Remove all the records where Confirmed Cases are less than 10

# In[32]:


data.head(2)


# In[37]:


data=data[data.Confirmed<10]
data.head(20)


# # In which region maximum number of Confirmed cases were recorded?

# In[38]:


data.head(2)


# In[49]:


data.groupby('Region').Confirmed.sum().sort_values(ascending=False).head(20)


# # In which region minimum number of Deaths cases were recorded?

# In[41]:


data.head(2)


# In[47]:


data.groupby('Region').Deaths.sum().sort_values(ascending=True).head(50)


# # How many confirmed,Deaths and Recovered cases were reported from Canada till 29 April 2020?

# In[50]:


data.head(2)


# In[59]:


data[data.Region=='Canada']


# # Sort the entire data wrt number of Confirmed cases in ascending order

# In[61]:


data.head(2)


# In[70]:


data.sort_values(by=['Confirmed'],ascending=True).head(50)


# # Sort the entire data wrt number of Recovered cases in descending order

# In[76]:


data.sort_values(by=['Recovered'])


# In[ ]:




