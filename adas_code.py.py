
# coding: utf-8

# In[1]:

import numpy as np
def read_data(infile):
    stats = np.loadtxt('infile',delimiter=',',unpack=True,dtype='int')
    number = stats[0]
    data = stats[1]
    return data


# In[ ]:



