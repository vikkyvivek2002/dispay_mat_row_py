import numpy as np

arr = np.array([[[11, 11, 9, 9],
                 [11, 0, 2, 0]],
                [[10, 14, 9, 14],
                 [0, 1, 11, 11]]])
print('Array Shape: ',arr.shape)

row = arr[0, :, 1]
print('Desired Row of Elements: ', row)
