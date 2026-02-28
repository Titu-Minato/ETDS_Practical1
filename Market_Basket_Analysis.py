#!/usr/bin/env python
# coding: utf-8

# In[27]:


from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import numpy as np
from apyori import apriori


# In[3]:


# Sample dataset (Transaction data)
dataset = [
    ['milk', 'bread', 'butter'],
    ['bread', 'butter', 'jam'],
    ['milk', 'bread', 'jam'],
    ['milk', 'bread', 'butter', 'jam'],
    ['butter', 'jam']
]


# In[4]:


print(dataset)


# In[5]:


# Step 1: Preprocessing the data
te = TransactionEncoder() # Initialize Transaction Encoder
te_ary = te.fit(dataset).transform(dataset) # Transform the dataset into a binary matrix
df = pd.DataFrame(te_ary, columns=te.columns_)  # Convert to a pandas DataFrame


# In[10]:


# Step 2: Generate frequent itemsets using Apriori algorithm
# `min_support` is the threshold for itemset frequency (e.g., 60%)
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)


# In[12]:


from mlxtend.frequent_patterns import apriori, association_rules
# Step 3: Generate association rules
# Calculate num_itemsets (total number of unique items)
num_itemsets = len(frequent_itemsets.itemsets[0])

# Now include num_itemsets in the association_rules call
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7, num_itemsets=num_itemsets)
     


# In[13]:


# Output results
print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(rules)


# In[14]:


frequent_itemsets


# In[15]:


rules


# In[16]:


df = pd.read_csv('Market_Basket_Optimisation.csv',header=None)


# In[17]:


df.head()


# In[18]:


df.isna().sum()


# In[19]:


## Data Cleaning step

# replacing empty value with 0.
df.fillna(0,inplace=True)


# In[20]:


df.head()


# In[21]:



# Data Pre-processing step

# for using aprori , need to convert data in list format..
# transaction = [['apple','almonds'],['apple'],['banana','apple']]....

transactions = []

for i in range(0,len(df)):
    transactions.append([str(df.values[i,j]) for j in range(0,20) if str(df.values[i,j])!='0'])


# In[22]:


transactions[0]


# In[23]:


transactions[1]


# In[28]:


# Call apriori function which requires minimum support, confidance and lift, min length is combination of item default is 2".
rules = apriori(transactions, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2)

## min_support = 0.003 -> means selecting items with min support of 0.3%
## min_confidance = 0.2 -> means min confidance of 20%
## min_lift = 3
## min_length = 2 -> means no. of items in the transaction should be 2


# In[29]:


#it generates a set of rules in a generator file...
rules


# In[30]:


# all rules need to be converted in a list..
Results = list(rules)
Results


# In[31]:


# convert result in a dataframe for further operation...
df_results = pd.DataFrame(Results)


# In[32]:


# as we see "order_statistics" , is itself a list so need to be converted in proper format..
df_results.head()


# In[33]:


# keep support in a separate data frame so we can use later..
support = df_results.support


# In[34]:


'''
convert orderstatistic in a proper format.
order statistic has lhs => rhs as well rhs => lhs
we can choose any one for convience.
Let's choose first one which is 'df_results['ordered_statistics'][i][0]'
'''

#all four empty list which will contain lhs, rhs, confidance and lift respectively.
first_values = []
second_values = []
third_values = []
fourth_value = []

# loop number of rows time and append 1 by 1 value in a separate list..
# first and second element was frozenset which need to be converted in list..
for i in range(df_results.shape[0]):
    single_list = df_results['ordered_statistics'][i][0]
    first_values.append(list(single_list[0]))
    second_values.append(list(single_list[1]))
    third_values.append(single_list[2])
    fourth_value.append(single_list[3])


# In[35]:


# convert all four list into dataframe for further operation..
lhs = pd.DataFrame(first_values)
rhs = pd.DataFrame(second_values)

confidance=pd.DataFrame(third_values,columns=['Confidance'])

lift=pd.DataFrame(fourth_value,columns=['lift'])


# In[36]:


# concat all list together in a single dataframe
df_final = pd.concat([lhs,rhs,support,confidance,lift], axis=1)
df_final


# In[37]:


'''
 we have some of place only 1 item in lhs and some place 3 or more so we need to a proper
 represenation for User to understand.
 replacing none with ' ' and combining three column's in 1
 example : coffee,none,none is converted to coffee, ,
'''
df_final.fillna(value=' ', inplace=True)
df_final.head()


# In[38]:


#set column name
df_final.columns = ['lhs',1,'rhs',2,3,'support','confidence','lift']
df_final.head()


# In[39]:


# add all three column to lhs itemset only
df_final['lhs'] = df_final['lhs'] + str(", ") + df_final[1]

df_final['rhs'] = df_final['rhs']+str(", ")+df_final[2] + str(", ") + df_final[3]


# In[40]:


df_final.head()


# In[41]:


#drop columns 1,2 and 3 because now we already appended to lhs column.

df_final.drop(columns=[1,2,3],inplace=True)


# In[42]:


#this is final output. You can sort based on the support lift and confidence..
df_final.head()


# In[43]:


## Showing top 10 items, based on lift.  Sorting in desc order
df_final.sort_values('lift', ascending=False).head(10)


# In[ ]:




