# chi-squared Test of Independence Karan Anita
import numpy as np
import pandas as pd
import scipy.stats as stats
np.random.seed(10)
Normal_Selfie = np.random.choice(a=["Female","Male"], p=[0.128, 0.872], size=10)
Apply_Filter = np.random.choice(a=["Female","Male"], p=[0.871, 0.129], size=10)
mscpart1 = pd.DataFrame({"Normal":Normal_Selfie, "Apply":Apply_Filter})
print(mscpart1)
stud_tab = pd.crosstab(mscpart1.Normal, mscpart1.Apply, margins=True)
stud_tab.columns = ["Female", "Male", "row_totals"]
stud_tab.index = ["Normal_Selfie", "Apply_Filter", "col_totals"]
observed = stud_tab.iloc[0:5, 0:2 ]
print(observed)
expected = np.outer(stud_tab["row_totals"][0:5], stud_tab.loc["col_totals"][0:2]) / 100
print(expected)
chi_squared_stat = (((observed-expected)**2)/expected).sum().sum()
print('Calculated : ',chi_squared_stat)
crit = stats.chi2.ppf(q=0.95, df=1)
print('Table Value : ',crit)
if chi_squared_stat>= crit: 
  print('H0 is Accepted ')
else:
  print("H0 is Rejected")