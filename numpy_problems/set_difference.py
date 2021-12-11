import numpy as np

array_1 =[0, 10, 20, 40, 60, 80]
print("Array1: ", array_1)
array_2 = [10, 30, 40, 50, 70]
print("Array2: ", array_2)
print("Unique values in array1 that are not in array2:")
print(np.setdiff1d(array_1, array_2))
