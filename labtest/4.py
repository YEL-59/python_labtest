import numpy as np
nArr2D = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])

row = nArr2D[1]
print('second row : ' , row)

rows = nArr2D[::2, ::2]
print('first and third rows :')
print(rows)

columns = nArr2D[: , 2:3]
print(' middle three columns :')
print(columns)