import numpy as np

arr_1 = np.array([1,2,3])
arr_2  = np.arange(1,4)*2

print(arr_1)
print(arr_2)
print(np.dot(arr_1,arr_2))
print(np.inner(arr_1,arr_2))
print(np.outer(arr_1,arr_2))
print(np.linalg.norm(arr_1))


print(np.cross(arr_1,arr_2))