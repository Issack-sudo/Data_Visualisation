import numpy as np
#saving single array
arr=np.arange(10)
print(arr)

np.save('saved_array',arr)
#New file is ceated-saved_array.npy

new_array=np.load('saved_array.npy')
print(new_array)

#save multiple arrays
array_1=np.arange(25)
array_2=np.arange(30)

np.savez('saved_archive.npz',x=array_1,y=array_2)
load_archive=np.load('saved_archive.npz')
print('load_archive[x]is')
print(load_archive['x'])

print('load_archive[y]is')
print(load_archive['y'])

#save to txtfile

np.savetxt('notepadfile.txt',array_1,delimiter=',')

#loading of txtfile
load_txt_file=np.loadtxt('notepadfile.txt',delimiter=',')
print('load_txt_fille is')
print(load_txt_file)

