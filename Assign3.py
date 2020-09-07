import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv('FiveYearData.csv')
print(df)

df1=df.reset_index().pivot_table( index='continent', columns='year',values='lifeExp')
print(df1)
plt.suptitle('HeatMap Plot')
sns.heatmap(df1,annot=True,).get_figure().savefig('heatmap5.png')
