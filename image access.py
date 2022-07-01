#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the library
import cv2


# In[2]:


#getting the image from system
# The image has to be stored at same location as file
#By default it reads image in BGR format
image = cv2.imread('desktop\nature.jpg')


# In[3]:


#To read image in grayscale format 
image_gray = cv2.imread('nature.jpg',cv2.IMREAD_GRAYSCALE)


# In[4]:


#To read images as it is (With alha mask or something else)
image_as = cv2.imread('nature.jpg',cv2.IMREAD_UNCHANGED)


# In[7]:


#To display the image
cv2.imshow('window name', image)
cv2.imshow('Grayscale image', image_gray)
cv2.imshow('Unchanged iamge', image_as)


# In[6]:


#Now we have to hold above created windows other wise program will end
#The parameter passed is Time in milliseconds
cv2.waitKey(5000)
cv2.destroyAllWindows()


# In[ ]:




