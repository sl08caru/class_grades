
# coding: utf-8

# In[1]:

def statistics(n):
    import numpy as np
    a = np.mean(n)
    b = np.std(n)
    c = min(n)
    d = max(n)
    return a,b,c,d


# In[ ]:



