#!/usr/bin/env python
# coding: utf-8

# # Goal :- To take valuable insights from the dataset by performing descriptive analysis

# ## Get the Data

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import_data = pd.read_csv("D:\\python docouments\\analytics_dataset\\2018-2010_import.csv")
export_data = pd.read_csv("D:\\python docouments\\analytics_dataset\\2018-2010_export.csv")


# ## Explore and Clean the Data

# In[3]:


import_data


# In[4]:


import_data.head


# In[5]:


import_data.columns


# In[6]:


import_data.shape


# In[7]:


import_data.info()


# In[8]:


import_data.describe()


# In[9]:


import_data['country'].value_counts()


# In[10]:


import_data.isnull().sum()


# In[11]:


import_data.Commodity.value_counts()


# In[12]:


import_data.groupby(['year','Commodity'])['value'].mean()


# In[13]:


import_data['value'] = import_data['value'].fillna(import_data.groupby(['year','Commodity'])['value'].transform('mean'))


# In[14]:


import_data.isnull().sum()


# In[15]:


export_data.describe()


# In[16]:


export_data.info()


# In[17]:


export_data.shape


# In[18]:


export_data['country'].value_counts()


# In[19]:


export_data.isnull().sum()


# In[20]:


export_data['value'] = export_data['value'].fillna(export_data.groupby(['year', 'Commodity'])['value'].transform('mean'))


# In[21]:


export_data.isnull().sum()


# ## Enrich the Data

# In[22]:


import_data.head()


# In[23]:


import_data['year'].unique()


# In[24]:


grouped_year = [2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010]
grouped_year.sort()
grouped_year


# In[25]:


value1 = import_data.groupby('year')['value'].sum()
value1


# In[26]:


import_value = list(value1)
import_value


# In[27]:


export_data.head()


# In[28]:


value2 = export_data.groupby('year')['value'].sum()
value2


# In[29]:


export_value = list(value2)
export_value


# In[30]:


merged_data = pd.DataFrame(list(zip(grouped_year, import_value, export_value)))
merged_data


# In[31]:


merged_data.columns = ['year', 'import_value', 'export_value']
merged_data


# In[32]:


Top_import_commodity = import_data.pivot_table(index = 'Commodity', values = 'value', aggfunc = np.sum).sort_values('value', ascending = 0).head(3)


# In[33]:


Top_export_commodity = export_data.pivot_table(index = 'Commodity', values = 'value', aggfunc = np.sum).sort_values('value', ascending = 0).head(3)


# In[34]:


import_data.columns


# In[35]:


Top_import_countries = import_data.pivot_table(index='country', values='value', aggfunc = np.sum).sort_values('value', ascending = 0).head(3)


# In[36]:


Top_import_countries


# In[37]:


Top_export_countries = export_data.pivot_table(index='country', values='value', aggfunc = np.sum).sort_values('value', ascending = 0).head(3)


# In[38]:


Top_export_countries


# ## Visualization

# In[39]:


plt.plot(merged_data['year'], merged_data['import_value'], color='blue', marker='o')
plt.title('Import Trend for the year 2010-2018', fontsize=14)
plt.xlabel('year', fontsize = 14)
plt.ylabel('Import Values', fontsize=14)
plt.grid(True)
plt.show()


# In[40]:


plt.plot(merged_data['year'], merged_data['export_value'], color='blue', marker='o')
plt.title('Export Trend for the year 2010-2018', fontsize=14)
plt.xlabel('year', fontsize = 14)
plt.ylabel('Export Values', fontsize=14)
plt.grid(True)
plt.show()


# In[41]:


plt.plot(merged_data['year'], merged_data['export_value'], marker='o', markerfacecolor='blue', markersize=10, color = 'blue', linewidth = 2)
plt.plot(merged_data['year'], merged_data['import_value'], marker='o', markerfacecolor='red', markersize=10,color = 'red', linewidth = 2)
plt.title('Export Vs Import Trend for the 2010-2018', fontsize=14)
plt.xlabel('year', fontsize = 14)
plt.ylabel('Export and Import Values', fontsize=14)
plt.grid(True)
plt.legend(['export', 'Import'])
plt.show()


# In[42]:


plt.barh(Top_import_commodity.index,Top_import_commodity['value'], 0.5, color=['green', 'blue', 'red'])
plt.xlabel('Value of Import')
plt.ylabel('Commodities')
plt.title('Top 3 Commodities based on Value of Import')
plt.show()


# In[43]:


plt.barh(Top_export_commodity.index,Top_export_commodity['value'], 0.5, color=['green', 'blue', 'red'])
plt.xlabel('Value of Export')
plt.ylabel('Commodities')
plt.title('Top 3 Commodities based on Value of Export')
plt.show()


# In[44]:


plt.bar(Top_import_countries.index, Top_import_countries['value'], width = 0.5, color=['green', 'blue', 'red'] )
plt.xlabel('Countries')
plt.ylabel('Value of Import')
plt.title('Top 3 Countries based on Value of Import')
plt.show()


# In[45]:


plt.bar(Top_export_countries.index, Top_export_countries['value'], width = 0.5, color=['green', 'blue', 'red'] )
plt.xlabel('Countries')
plt.ylabel('Value of Export')
plt.title('Top 3 Countries based on Value of Export')
plt.show()


# ## Valuable Insights from the data

#     1) Import is hightest in 2018 while at the lowest in 2010. 
#     2) Export is highest in 2018 while lowest in 2010.
#     3) India's export is always lower than import, This shows that India has faced trade deficit between year 2010 and 2018.       Although in 2010 both import and export are at their minimum value and at their maximum in 2018 but India's export has      fallen in a greater magnitude in 2015 than the imports for the same year. In 2016 when import has fallen at Rs. 4,50,000 we can see that for the same year, export is rising at an aggregate level.
#     4) India import and export mineral fuel, mineral oil and mineral based items the highest.
#     5) India's imports are highest with China, then United Arab Emirates followed by Saudhi Arab
#     6) india's exports asre highest with USA, then United Arab Emirates follwed by China
#     7) The most interesting fact is that from 2010-2018 at an aggregate level india's 1st highest import and export commodity  is mineral fuel, mineral oil and mineral.
