import numpy as np

matrix1 = np.array([[3, 4], 
                   [6, 2]])

transpose = np.transpose(matrix1)

print(transpose)

# finding the inverse of matrices

matrix2 = np.array([[[2, 4, 6], [1, 3, 5], [8, 0, 1]]])

inverse = np.linalg.inv(matrix2)



print("Inverse of a matrix is: \n", inverse)

# finding the determinant of a matrix

matrix3 = np.array([[2, 4, 6], 
                   [1, 3, 5], 
                   [0, 7, 9]])

determinant = np.linalg.det(matrix3)


print("Determinant is: \n", determinant)
