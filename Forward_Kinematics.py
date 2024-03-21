import numpy as np

def matrix_multiply(mat1, mat2):
    result = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            result[i][j] = sum(mat1[i][k] * mat2[k][j] for k in range(4))
    return result

# Example matrices
L_1 = 11.5
L_2 = 13.2
L_3 = 11

theta_1 = 0
theta_2 = 0
theta_3 = 0
theta_4 = 0

Transf_0_to_1 = [
    [np.cos(theta_1), -np.sin(theta_1),0, 0],
    [np.sin(theta_1), np.cos(theta_1), 0, 0],
    [0, 0, 1, 8],
    [0, 0, 0, 1]
]

Transf_1_to_2 = [
    [np.cos(theta_2), 0, np.sin(theta_2), -L_1 * np.cos(theta_2)],
    [0, 1, 0, 0],
    [-np.sin(theta_2), 0, np.cos(theta_2), L_1 * np.sin(theta_2)],
    [0, 0, 0, 1]
]

Transf_2_to_3 = [
    [np.cos(theta_3), 0, np.sin(theta_3), L_2 * np.cos(theta_3)],
    [0, 1, 0, 0],
    [-np.sin(theta_3), 0, np.cos(theta_3), L_2 * np.sin(theta_3)],
    [0, 0, 0, 1]
]

Transf_3_to_EE = [
    [np.cos(theta_4), 0, np.sin(theta_4), L_3 * np.cos(theta_4)],
    [0, 1, 0, 0],
    [-np.sin(theta_4), 0, np.cos(theta_4), L_3 * np.sin(theta_4)],
    [0, 0, 0, 1]
]

# Perform matrix multiplication, Euler Relative Axes
matrix_1 = matrix_multiply(Transf_0_to_1, Transf_1_to_2)
matrix_2 = matrix_multiply(matrix_1, Transf_2_to_3)
Transformation_final = matrix_multiply(matrix_2, Transf_3_to_EE)

# Print the result
for row in Transformation_final:
    print(row)
