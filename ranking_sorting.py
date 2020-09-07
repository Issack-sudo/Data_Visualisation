import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy.random import random
ser1=Series([500,1000,1500],index=['a','c','b'])
print(ser1)
#sorting by index
print(ser1.sort_index())

#sort by values
print(ser1.sort_values())
print(ser1.rank())

#ranking of series
ser2=Series(random(10))
print(ser2)

print(ser2.rank())

ser2=ser2.sort_values()
print(ser2.rank)