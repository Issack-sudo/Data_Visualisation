import pandas as pd
import numpy as np
from pandas import Series,DataFrame
from numpy import random

B1=np.arange(25).reshape(5,5)
A1=random.randn(25).reshape(5,5)


print(B1)
print(A1)
print("output for axis-1")
print(np.concatenate([A1,B1],axis=1))
print(np.concatenate([A1,B1],axis=0))
#series

s1=Series([100,200,300],index=['A','B','C'])
s2=Series([400,500],index=['D','E'])
print(pd.concat([s1,s2]))
print(pd.concat([s1,s2],axis=1,sort=True))

#dataframes

df1=DataFrame(random.rand(4,3),columns=['A','B','C'])
df2=DataFrame(random.rand(3,3),columns=['B','D','A'])

print(pd.concat([df1,df2],sort=True))
print("pd.concat dataframe -continuos index")
print(pd.concat([df1,df2],ignore_index=True,sort=True))
print(pd.concat([df1,df2],axis=1))