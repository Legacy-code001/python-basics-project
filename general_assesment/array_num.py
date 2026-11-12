import numpy as np


# print(np.array([1,2,3,4]))

mat_arr = np.array([[20,34,67],[24,56,87]], dtype= np.float64)

# print(mat_arr.ndim)
# print(mat_arr.dtype)

# #find revenues of first month of second quarter
# print(mat_arr[1,0])
# print(mat_arr[0,-1])
# print(mat_arr.itemsize)

# #update
# mat_arr[1,2] = 45
# print(mat_arr)


# arr_list = np.array([
#     [12, 34, 6],
#     [14,16,32]
# ])

# print(arr_list[:,1])
# print(arr_list[1,2])
# print(arr_list[:1,1:])
# print(np.vstack((arr_list, mat_arr)))
# new_vstac = np.vstack((arr_list, mat_arr))
# print(np.hstack((arr_list, mat_arr)))
# the_split, remainder = np.split(new_vstac, 2)
# print(the_split)
# print(remainder)

val = np.array([['101', 'Sales', '3', '101', '8'],
       ['102', 'HR', '5', '102', '10'],
       ['103', 'IT', '2', '103', '9'],
       ['104', 'Sales', '8', '104', '6'],
       ['105', 'IT', '6', '105', '7'],
       ['106', 'HR', '4', '106', '8'],
       ['107', 'IT', '7', '107', '9'],
       ['108', 'Sales', '1', '108', '5'],
       ['109', 'HR', '3', '109', '7']], dtype='<U21')

print(val[:, 4])

print(np.mean(val[:,4].astype(float)))

print(np.sort(val[:, 4].astype(int)))


for v in val:
    print(v[:2])
# for v in val:
#     # print(val[:, :2])
#     print(f"employee_id: {v[0]}, happiness: {v[-1].astype(float)}")

# print(val[val[:, 1] == "HR"])

# print(val[val[:, 1] == "HR"][:, 4].astype(float))

# print(np.mean(val[val[:, 1] == "HR"][:, 4].astype(float)))
#     # print(val[:, :2])

# print(np.unique(val[:, 1]))