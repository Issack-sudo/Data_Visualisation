import numpy as np
arr=np.arange(0,12)
print(arr)


#print(arr[0:5])
#print(arr[2:6])
arr[0:5]=20
print(arr)

#important
arr2=arr[0:6]


arr2[:]=29 #all element are modified

#print(arr2)
print(arr)

#creating new array copy

arrcop=arr.copy()
