import numpy as np
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Series

df=sns.load_dataset('diamonds').sample(frac=1).head(100)
print(df)

sns.lmplot('price','carat',df).savefig('1.png')

#modify(
sns.lmplot('price','carat',df,scatter_kws={'marker':'o','color':'green'},line_kws={'color':'red','linewidth':1}).savefig('2.png')

#higher_order trend line
sns.lmplot('price','carat',df,order=5,scatter_kws={'marker':'o','color':'green'},line_kws={'color':'red','linewidth':1}).savefig('3.png')

#scatter plot without trend line
sns.lmplot('price','carat',df,fit_reg=False).savefig('4.png')


#heu argument
sns.lmplot('price','carat',df,hue='cut',markers=['^','*','.',',','s']).savefig('5.png')

sns.lmplot('price','carat',df,hue='cut').savefig('6.png')

#local regression
#sns.lmplot('price','carat',df,lowess=True).savefig('7.png')

#regplot
sns.regplot('price','carat',df).get_figure().savefig('8.png')

#sub plots
image,(plt1,plt2)=plt.subplots(1,2,sharey=True)
sns.regplot('price','carat',df,ax=plt1).get_figure().savefig('9.png')
sns.boxplot(df['carat'],df['depth'],color='green',ax=plt2).get_figure().savefig('9.png')