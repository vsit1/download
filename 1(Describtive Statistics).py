# Describtive Statistics
import pandas as pd
d = {'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
df = pd.DataFrame(d)
print(df)
print ("Sum",df.sum())
print ("Mean",df.mean())
print ("Standard Deviation",df.std())
print('############ Descriptive Statistics ########## ')
print ("Descriptive Statistics",df.describe())