
# coding: utf-8

# In[14]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([1,3,5,np.nan,6,8,1])
s


# In[15]:


dates = pd.date_range('20130101', periods=5)
dates


# In[16]:

df = pd.DataFrame(np.random.randn(5,5), index=dates, columns=list('ABCDE'))
df


# In[17]:

df2 = pd.DataFrame({ 'A' : 1.,
    'B' : pd.Timestamp('20130102'),
  'C' : pd.Series(2,index=list(range(4)),dtype='float32'),
  'D' : np.array([3] * 4,dtype='int32'),
   'E' : pd.Categorical(["test","train","test","train"]),
    'F' : 'foo' })
df2


# In[18]:

df2.dtypes


# In[19]:

df.head(3)


# In[20]:

df.tail(3)


# In[21]:

df.index


# In[22]:

df.columns


# In[23]:

df.values


# In[24]:

df.describe()


# In[25]:

df.T


# In[29]:

df.sort_index(axis=1, ascending=False)


# In[28]:

df.sort_values(by='B')


# # Selection
# Note While standard Python / Numpy expressions for selecting and setting are intuitive and come in handy for interactive work, for production code, we recommend the optimized pandas data access methods, .at, .iat, .loc, .iloc and .ix.
# See the indexing documentation Indexing and Selecting Data and MultiIndex / Advanced Indexing

# In[32]:

df['A']


# In[33]:

df[0:3]


# In[34]:

df['20130102':'20130104']


# In[35]:

df.loc[dates[0]]


# In[36]:

df.loc[:,['A','B']]


# In[37]:

df.loc['20130102':'20130104',['A','B']]


# In[38]:

df.loc['20130102',['A','B']]


# In[41]:

df.loc[dates[0],'A']


# In[42]:

df.at[dates[0],'A']


# In[43]:

df.iloc[3]


# In[44]:

df.iloc[3:5,0:2]


# In[45]:

df.iloc[[1,2,4],[0,2]]


# In[46]:

df.iloc[1:3,:]


# In[47]:

df.iloc[:,1:3]


# In[48]:

df.iloc[1,1]


# In[49]:

df.iat[1,1]


# In[50]:

df[df.A > 0]


# In[51]:

df[df > 0]


# In[54]:

df2 = df.copy()
df2['E'] = ['one','two','three','four','three']
df2


# In[55]:

df2[df2['E'].isin(['two','four'])]


# # Setting
# Setting a new column automatically aligns the data by the indexes

# In[59]:

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
s1


# In[61]:

df['F'] = s1
df


# In[63]:

df.at[dates[0],'A'] = 0
df


# In[64]:

df.iat[0,1] = 0
df


# In[65]:

df.loc[:,'D'] = np.array([5] * len(df))
df


# In[66]:

df2 = df.copy()
df2[df2 > 0] = -df2
df2


# # Missing Data
# pandas primarily uses the value np.nan to represent missing data. It is by default not included in computations. See the Missing Data section
# 
# Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data.

# In[67]:

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1


# In[73]:

df1.loc[dates[0]:dates[1],'E'] = np.nan
df1


# In[79]:

df1.dropna(how='any')


# In[78]:

df1.fillna(value=9)


# In[77]:

pd.isnull(df1)


# # Operations
# See the Basic section on Binary Ops

# In[83]:

df


# In[80]:

df.mean()


# In[81]:

df.mean(1)


# In[87]:

s = pd.Series([1,3,5,np.nan,6], index=dates).shift(2)
s


# In[88]:

df.sub(s, axis='index')
df


# # Apply
# 
# Applying functions to the data

# In[89]:

df.apply(np.cumsum)


# In[90]:

df.apply(lambda x: x.max() - x.min())


# # Histogramming
# 
# See more at Histogramming and Discretization

# In[97]:

s = pd.Series(np.random.randint(0, 7, size=10))
s


# In[98]:

s.value_counts()


# # String Methods
# 
# Series is equipped with a set of string processing methods in the str attribute that make it easy to operate on each element of the array, as in the code snippet below. Note that pattern-matching in str generally uses regular expressions by default (and in some cases always uses them). See more at Vectorized String Methods.

# In[100]:

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s


# In[102]:

s.str.lower()


# In[107]:

df = pd.DataFrame(np.random.randn(10, 4))
df


# In[109]:

pieces = [df[:3], df[3:7], df[7:]]
pieces


# In[110]:

pd.concat(pieces)


# In[118]:

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
left


# In[119]:

right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
right


# In[120]:

pd.merge(left, right, on='key')


# In[122]:

df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
df


# In[124]:

s = df.iloc[3]
s


# In[125]:

df.append(s, ignore_index=True)


# # Grouping
# By “group by” we are referring to a process involving one or more of the following steps
# 
# * Splitting the data into groups based on some criteria
# * Applying a function to each group independently
# * Combining the results into a data structure

# In[127]:

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
df


# In[131]:

df.groupby('A').sum()


# In[133]:

df.groupby(['B','A']).sum()


# # Reshaping
# See the sections on Hierarchical Indexing and Reshaping.

# In[136]:

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
tuples


# In[138]:

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
index


# In[139]:

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df


# In[140]:

df2 = df[:4]
df2


# In[141]:

stacked = df2.stack()
stacked


# In[142]:

stacked.unstack()


# In[143]:

stacked.unstack(1)


# In[144]:

stacked.unstack(0)


# In[146]:

df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                   'B' : ['A', 'B', 'C'] * 4,
                   'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D' : np.random.randn(12),
                   'E' : np.random.randn(12)})
df


# In[147]:

pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])


# # Time Series
# pandas has simple, powerful, and efficient functionality for performing resampling operations during frequency conversion (e.g., converting secondly data into 5-minutely data). This is extremely common in, but not limited to, financial applications. See the Time Series section

# In[149]:

rng = pd.date_range('1/1/2012', periods=100, freq='S')
rng


# In[150]:

ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts


# In[152]:

ts.resample('1Min').sum()


# In[153]:

rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
rng


# In[154]:

ts = pd.Series(np.random.randn(len(rng)), rng)
ts


# In[156]:

ts_utc = ts.tz_localize('UTC')
ts_utc


# In[157]:

ts_utc.tz_convert('US/Eastern')


# In[158]:

rng = pd.date_range('1/1/2012', periods=5, freq='M')
rng


# In[159]:

ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts


# In[160]:

ps = ts.to_period()
ps


# In[161]:

ps.to_timestamp()


# In[163]:

prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
prng


# In[164]:

ts = pd.Series(np.random.randn(len(prng)), prng)
ts


# In[166]:

ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
ts.index


# In[167]:

ts.head()


# In[ ]:



