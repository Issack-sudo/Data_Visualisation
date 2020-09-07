import pandas as pd
import numpy as np
from pandas import DataFrame

df=DataFrame({'Country':['Afghanistan','Albania','Algeria'],
              'code':['93','355','213']})

print(df)

GDP_map=({'Afghanistan':'20','Albania':'12.8','Algeria':'215'})
print(GDP_map)

df['GDP']=df['Country'].map(GDP_map)

print(df)