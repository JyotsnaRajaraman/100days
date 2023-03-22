#!/usr/bin/env python
# coding: utf-8

# # Data Visualization Project for Kaggle trial
# 
# ### Some Useful tips
# 
# %lsmagic - to see all bash and other magic commands\n
# %inlinematplotlib  - run if you want to be able to display matplotlib graphs inline\n
# %%HTML - converts the cell to render HTML (use to embed videos/display some website content)
# %%timeit - times some python code that you may write and gives avg time
#  
# Use File -> Download as to pick the format in which you would like the file to be presented/shared

# ## Working with the Human Stress Detection in and through Sleep Data from Kaggle
# [Find more details here](https://www.kaggle.com/datasets/laavanya/human-stress-detection-in-and-through-sleep)
# #### README (for the data)
# 
# ##### Columns: 
# 1. snoring range of the user
# 2. respiration rate
# 3. body temperature
# 4. limb movement rate
# 5. blood oxygen levels
# 6. eye movement
# 7. number of hours of sleep
# 8. heart rate
# 9. Stress Levels (0- low/normal, 1 – medium low, 2- medium, 3-medium high, 4 -high) 
# 
# Considering today’s lifestyle, people just sleep forgetting the benefits sleep provides to the human body. Smart-Yoga Pillow (SaYoPillow) is proposed to help in understanding the relationship between stress and sleep and to fully materialize the idea of “Smart-Sleeping” by proposing an edge device. An edge processor with a model analyzing the physiological changes that occur during sleep along with the sleeping habits is proposed. Based on these changes during sleep, stress prediction for the following day is proposed. The secure transfer of the analyzed stress data along with the average physiological changes to the IoT cloud for storage is implemented. A secure transfer of any data from the cloud to any third-party applications is also proposed. A user interface is provided allowing the user to control the data accessibility and visibility. SaYoPillow is novel, with security features as well as consideration of sleeping habits for stress reduction, with an accuracy of up to 96%.
# In SayoPillow.csv, you will see the relationship between the parameters- snoring range of the user, respiration rate, body temperature, limb movement rate, blood oxygen levels, eye movement, number of hours of sleep, heart rate and Stress Levels (0- low/normal, 1 – medium low, 2- medium, 3-medium high, 4 -high) 
# 
# #### Sources:
# 1.	L. Rachakonda, A. K. Bapatla, S. P. Mohanty, and E. Kougianos, “SaYoPillow: Blockchain-Integrated Privacy-Assured IoMT Framework for Stress Management Considering Sleeping Habits”, IEEE Transactions on Consumer Electronics (TCE), Vol. 67, No. 1, Feb 2021, pp. 20-29.
# 2.	L. Rachakonda, S. P. Mohanty, E. Kougianos, K. Karunakaran, and M. Ganapathiraju, “Smart-Pillow: An IoT based Device for Stress Detection Considering Sleeping Habits”, in Proceedings of the 4th IEEE International Symposium on Smart Electronic Systems (iSES), 2018, pp. 161--166. 

# In[2]:


print("hello")


# In[7]:


# Importing the libraries
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

"Libraries Imported"


# In[18]:


#Load the data
data = pd.read_csv("StressSleepData.csv")
data.head()


# In[21]:


# Change col names to make it more obvious

new_column_names = ["snoringrate", "respiration", "bodytemp", "limbmovement", "bloodoxygenlevel", "eyemovement", "hoursasleep", "heartrate", "stresslevel"]
data.columns = new_column_names
data.head()


# In[14]:


#Lets do some basic data analysis
#Checking for null values in the dataset
data.isnull().values.sum()


# In[16]:


#Checking for duplicate rows
data.duplicated()


# In[22]:


#What are the different data types
data.dtypes


# In[25]:


# Get a general understanding of the dataset
data.describe()


# ### Notable Analysis from the above description
# 
# 1. Average Stress Level is 2
# 2. On average people spend 3.7 hours asleep(?)

# In[36]:


# Now let us plot some graphs to understand the relation between the different parameters and stress level

stressdata = data.groupby(data["stresslevel"])
cols = ["snoringrate", "respiration", "bodytemp", "limbmovement", "bloodoxygenlevel", "eyemovement", "hoursasleep", "heartrate"]
stressdata[cols].mean().plot()

plt.title("Stress Levels Measured by Sleeping Hours")
plt.xlabel("Stress Levels")
plt.ylabel("Other parameters")
plt.show()


# There is clearly a linear relation between the stress levels and number of hours - it is evident that the number of hours and stress levels are inversely proportional to each other
# Let us separate the parameters into increasing and decreasing categories and compare

# In[41]:


stressdata = data.groupby(data["stresslevel"])
increasingcols = ["snoringrate", "respiration",  "limbmovement", "eyemovement",  "heartrate"]
decreasingcols = ["hoursasleep", "bodytemp", "bloodoxygenlevel"]
stressdata[increasingcols].mean().plot()
stressdata[decreasingcols].mean().plot()

plt.title("Stress Levels Measured by Sleeping Hours")
plt.xlabel("Stress Levels")
plt.ylabel("Other parameters")
plt.show()


# Lets take the most obvious cause for stress - hours of sleep and look at how it affects stress

# In[65]:


stressdata = data.groupby(data["stresslevel"]).mean()
stressdata.head()


# In[64]:


sns.barplot(data = data, x="stresslevel", y="hoursasleep")

