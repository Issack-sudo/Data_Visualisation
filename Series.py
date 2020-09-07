import pandas as pd
from pandas import Series
import numpy as np

object=Series([5,10,15,20])
# print(object)

# print(object.values)
# print(object.index)

#use_numpy to series
data_array=np.array(['a','b','c'])
s=Series(data_array)
# print(s)

#custom index
s=Series(data_array,index=[100,102,103])
# print(s)
s=Series(data_array,index=['index1','index2','index3'])
# print(s)

#usingreal life ex
revenue=Series([20,80,40,35],index=['ola','uber','grab','gojeck'])
# print(revenue)

# print(revenue['ola'])
# print(revenue[revenue>=35])

#use boolean condition
# print('lyft' in revenue)
revenue_dict=revenue.to_dict()
print(revenue_dict)

#nan_values
index_2=['ola','uber','grab','gojeck','lyft']
revenue2=Series(revenue,index_2)
# print(revenue2)
#
# print(pd.isnull(revenue2))
# print(pd.notnull(revenue2))

#additional of series

print(revenue+revenue2)

#assigning names
revenue2.name='Company revenuue'
revenue2.index.name='Company Name'
print(revenue2)