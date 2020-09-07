import numpy as np
import pandas as pd
from pandas import Series,DataFrame

url="https://en.wikipedia.org/wiki/Pivot_table"
df_list=pd.io.html.read_html(url)
df=df_list[0]

print(df)

df1=df.pivot('Date of sale','Sales person','Total price')
print(df1)