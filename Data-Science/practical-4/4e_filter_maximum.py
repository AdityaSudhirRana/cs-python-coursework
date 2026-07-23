import numpy as np

print("S105 - Aditya Rana")

arr = np.array([15,42,67,23,67,10,55])

m = np.max(arr)

print("Original Array:", arr)

print("Maximum Value:", m)

print("Filtered Array:", arr[arr==m])
