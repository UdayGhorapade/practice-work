#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#write a python progaram which will ep adding a stream of numbers inputted by 
#the user, adding stops as soon as the user presses the q key on the keyoard.


# In[2]:


sum=(0)
while(True):
    userinput=input('enter the value of price:\n')
    if (userinput!='q'):
        sum=sum + int(userinput)
        print(f"order equl so far:{sum}")
    else:
        print(f"your ill total is {sum}.Thanks for shopping with us")
        break
        


# In[ ]:




