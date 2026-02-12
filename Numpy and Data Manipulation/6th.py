import numpy as np 

arr1 = np.array([30,40,50,20])
arr2 = np.array([3,5,6,7])

print(np.concatenate([arr1,arr2]))  
print(np.hstack([arr1,arr2]))
print (np.vstack([arr1,arr2]))