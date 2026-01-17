#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd


# In[33]:


data_titu = {
    'Region': ['North','South','East','West', 'North', 'South', 'East', 'West'],
    'Product': ['A', 'B', 'A', 'B', 'C', 'C', 'B', 'A'],
    'Sales': [150, 200, 300, 400, 250, 180, 220, 310],
    'Quantity': [10, 15, 20, 25, 12, 14, 16, 18],
}


# In[34]:


df_titu = pd.DataFrame(data_titu)
print("Dataset:\n",df)


# In[35]:


# Step 2: Grouping and Aggregation
# Aggregating Sales by Region (Sum Aggregation)
sales_by_region_titu = df_titu.groupby('Region')['Sales'].sum()
print("\nTotal Sales by Region",sales_by_region_titu)


# In[36]:


# Aggregating Sales and Quantity by Product (Mean Aggregation)
mean_by_product_titu = df_titu.groupby('Product')[['Sales','Quantity']].mean()
print("\nMean Sales and Quantity by Product",mean_by_product_titu)


# In[37]:


# Aggregating Count of Sales by Region (Count Aggregation)
count_by_region_titu = df_titu.groupby('Region')['Sales'].count()
print("\n Count of Sales Recorde by Region",count_by_region_titu)


# In[38]:


# Custom Aggregation: Calculate Min and Max Sales by Region
custom_agg_titu = df_titu.groupby('Region')['Sales'].agg(['min','max'])
print("\nCustom Aggregation (Min and Max Sales by Region):\n ",custom_agg_titu)


# In[39]:


# Step 3: Multi-Level Aggregation
# Aggregating Sales by Region and Product
multi_level_agg_titu = df_titu.groupby(['Region','Product'])['Sales'].sum()
print("\n Sales by Region and Product:\n",multi_level_agg_titu)


# In[40]:


# Step 4: Reset Index for Multi-Level Aggregation
multi_level_agg_reset_titu = multi_level_agg_titu.reset_index()
print("\n Sales by Region and Product (Resent Index):",multi_level_agg_reset_titu)


# Objective:
# 
# To understand and implement:
# 
# Time Aggregation: Aggregating data over different time periods (e.g., monthly, yearly).
# 
# Spatial Aggregation: Aggregating data by spatial attributes (e.g., by region, city).

# In[41]:


data_t2 = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'City': ['City1', 'City2', 'City3', 'City4', 'City1', 'City2', 'City3', 'City4'],
    'Product': ['A', 'B', 'A', 'B', 'C', 'C', 'B', 'A'],
    'Sales': [150, 200, 300, 400, 250, 180, 220, 310],
    'Quantity': [10, 15, 20, 25, 12, 14, 16, 18],
    'Date': pd.to_datetime(['2025-01-01', '2025-01-02', '2025-02-01', '2025-02-03',
                            '2025-03-01', '2025-03-02', '2025-04-01', '2025-04-03'])
}


# In[42]:


df_t2 = pd.DataFrame(data_t2)
print(df_t2)


# In[43]:


# -----------------------------
# Time Aggregation
# -----------------------------

# Step 2: Set Date Column as Index (optional)
df_t2.set_index('Date',inplace=True)


# In[44]:


# Aggregating Sales by Month
monthly_sales_t2 = df_t2.resample('M')['Sales'].sum()
print("\nTotal Sales by Month:\n", monthly_sales_t2)


# In[45]:


# Aggregating Sales by Quarter
quarterly_sales_t2 = df_t2.resample('Q')['Sales'].sum()
print("\nTotal Sales by Quarter:\n", quarterly_sales_t2)


# In[46]:


# Aggregating Sales by Year
yearly_sales_t2 = df_t2.resample('Y')['Sales'].sum()
print("\nTotal Sales by Year:\n", yearly_sales_t2)


# In[47]:


# Reset Index to Restore Original Structure
df_t2.reset_index(inplace = True)


# In[48]:


# -----------------------------
# Spatial Aggregation
# -----------------------------

# Step 3: Aggregating Sales by Region
sales_by_region_t2 = df_t2.groupby('Region')['Sales'].sum()
print("\n Total Sales by Region",sales_by_region_t2)


# In[49]:


# Aggregating Sales by City
sales_by_city_t2 = df_t2.groupby('City')['Sales'].sum()
print("\nTotal Sales by City:\n", sales_by_city_t2)


# In[50]:


# Aggregating Sales by Region and City
sales_by_region_city_t2 = df_t2.groupby(['Region', 'City'])['Sales'].sum()
print("\nTotal Sales by Region and City:\n", sales_by_region_city_t2)


# In[51]:


# Step 4: Export Spatial Aggregation Results
sales_by_region_city_reset_t2 = sales_by_region_city_t2.reset_index()


# In[52]:


sales_by_region_city_reset_t2.to_csv("spatial_aggregation.csv", index=False)
print("\nSpatial aggregation data saved to 'spatial_aggregation.csv'")


# In[ ]:




