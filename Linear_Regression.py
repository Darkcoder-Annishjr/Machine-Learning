#IMPORTING ALL THE PYTHON LIBRARIES THAT WE GONNA USE FOR LINEAR REGRESSION

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split  #importing this to train and test the accuracy 
from sklearn.linear_model import LinearRegression as lr

# IMPORTING THE DATA 
df = pd.read_csv("")

# CLEANING THE DATA (Duplicates, Null Values) 
df.isna.sum()

df.duplicated()

df.drop_duplicates()

# VIEW INFO OF THE DATA (Shape, Data_Type, Descriptive Statistics)
df.shape

df.info()

df.describe()

# TO VISUALIZE THE DATA
plt.scatter()
plt.xlabel("")
plt.ylabel("")

# FITTING THE LINEAR REGRESSION
lr = LinearRegression()

lr.fit()








