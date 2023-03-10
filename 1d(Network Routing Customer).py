# Network Routing Customer
import sys
import os
import pandas as pd
################################################################
pd.options.mode.chained_assignment = None
################################################################
Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sInputFileName=Base+'/01-Vermeulen/02-Assess/01-EDS/02-Python/Assess-Network-RoutingCustomer.csv'
################################################################
sOutputFileName='Assess-Network-Routing-Customer.gml'
Company='01-Vermeulen'
################################################################
### Import Country Data
################################################################
sFileName=sInputFileName
print('################################')
print('Loading :',sFileName)
print('################################')
CustomerData=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
print('Loaded Country:',CustomerData.columns.values)
print('################################')
print(CustomerData.head())
print('################################')
print('### Done!! #####################')
