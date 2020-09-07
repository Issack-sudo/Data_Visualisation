import pandas as pd
import numpy as np
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

#manual create a KDE by summin  ht gaussian ditrbution
ds=randn(100)
#sns.rugplot(ds)
#plt.hist(ds,alpha=0.5)
#plt.savefig('image1.png')


#x_axis=np.linspace(ds.min()-1,ds.max()+1,50)

#bandwi
#bandwith=((4*ds.std()**5)/(3*len(ds)))**0.2
#kernels=[]
#for point in ds:
#  kernel=stats.norm(point,bandwith).pdf(x_axis)
#  kernels.append(kernel)
#
#   kernel=kernel/kernel.max()
#   kernel=kernel*0.6

#   plt.plot(x_axis,kernel,alpha=0.5,color="red")

#plt.savefig('image21.png')

#kde=np.sum(kernels,axis=0)
#kde_fig=plt.plot(x_axis,kde,color='green')
#sns.rugplot(ds)
plt.suptitle('KDE Plot')
#plt.savefig('image32.png')


#using seaborn
kdefig=sns.kdeplot(ds)
fig=kdefig.get_figure()
fig.savefig('image40.png')