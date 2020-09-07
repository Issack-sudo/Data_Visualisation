import numpy as np
import pandas as pd
from pandas import Series,DataFrame
dframe=pd.read_csv('demo.csv')
print(dframe)

dframe=pd.read_csv('demo.csv',header=None)
print(dframe)
#use readtable
dframe2=pd.read_csv('demo.csv',sep=',',header=None)
print(dframe2)

#parrtial rows importing
print(pd.read_csv('demo.csv',nrows=2,header=None))

#dump
dframe2.to_csv('outputCSV.csv', sep='!')

#select specific column
dframe.to_csv('dataoutput.csv', columns=[0,1])