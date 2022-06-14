#!/usr/bin/env python
# coding: utf-8

# In[2]:


set1 = {2,3,4.4,True,"python"}


# In[3]:


set1


# In[4]:


set2 = {1,2,3,4,1,2,1,1,4,3}


# In[9]:


set2.add(11)
set2


# In[10]:


set1.update([5,6,7])
set1


# In[11]:


set1.remove(2)
set1


# In[13]:


set1.pop()


# In[14]:


set1.clear()
set1


# In[15]:


set3 = set1.union(set2)
set3


# In[16]:


set3 = set1.intersection(set2)
set3


# In[ ]:




