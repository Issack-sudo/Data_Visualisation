import numpy as np
import pandas as pd
from pandas import Series,DataFrame

series1=Series([100,200,300],index=['A','B','C'])
print(series1)

print(series1['A'])

print(series1[['A','B']])

#number_indexes
print(series1[0])
print(series1[0:2])

#conditional indexes
print(series1[series1>150])
print(series1[series1==300])

#usind and accessing dataframe
df1=DataFrame(np.arange(9).reshape(3,3),index=['car','bike','cycle'],columns=['A','B','C'])
print(df1)

print(df1['A'])
print(df1[['A','B']])

print(df1>5)
#ix function
print(df1.loc['bike'])
print(df1.iloc[1])
