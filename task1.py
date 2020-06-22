#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats


# In[3]:


# Generate randomly samples
x = np.random.randint(0,9,1000)
y = np.random.randint(0,9,1000)
# Mean calculation
mx = x.mean()
my = y.mean()
# std
stdx = x.std()
stdy = y.std()
#cov matrix
convxy = np.cov(x,y)
print(convxy)
# cov efficient
coefxy = np.corrcoef(x,y)
print(coefxy)


# In[5]:


# Verification
covx = np.mean((x-x.mean()) ** 2)
covy = np.mean((y-y.mean()) ** 2)
print(covx)
print(covy)
covxy = np.mean((x-x.mean())*(y-y.mean()))
print(covxy)


# In[16]:


# 二项分布
# 抽了20次硬币/抽中正面，每次概率为0.4
n = 20
p = 0.4
k = np.arange(0,40)
binomial = stats.binom.pmf(k,n,p)
print (binomial)
plt.plot(k,binomial,'o-')
plt.title('binomial:n=%i,p=%.2f'%(n,p),fontsize=10)
plt.xlabel('Test time')
plt.ylabel('Success Prabability')
plt.show()


# In[ ]:




