import numpy as np


print(np.array([1,2,3,4]))

mat_arr = np.array([[20,34,67],[24,56,87]], dtype= np.float64)

print(mat_arr.ndim)
print(mat_arr.dtype)

#find revenues of first month of second quarter
print(mat_arr[1,0])
print(mat_arr[0,-1])
print(mat_arr.itemsize)

#update
mat_arr[1,2] = 45
print(mat_arr)