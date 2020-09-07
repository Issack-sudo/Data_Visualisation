import numpy as np
import matplotlib.pyplot as plt

axes_values=np.arange(-100,100,10)
dx,dy=np.meshgrid(axes_values,axes_values)

# print('dx')
# print(dx)
#
# print('dy')
# print(dy)

function=2*dx+3*dy
function2=np.cos(dx)+np.cos(dy)

print(function)

#plt.imshow(function)
#plt.title('Function of plot 2*dx+3*dy')
plt.imshow(function2)
plt.title('Function of plot')
plt.colorbar()
plt.savefig('myfig2.png')