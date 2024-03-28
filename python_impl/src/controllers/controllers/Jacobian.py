import numpy as np
from Workspace import *

def Jacobian(theta_1, theta_2, theta_3, theta_4):
    L_1 = link_length_1
    L_2 = link_length_2
    L_3 = link_length_3
    L_4 = link_length_4
    L_5 = link_length_5

    J_11 = -(L_5 * np.sin(theta_1) * np.cos(theta_2) * np.cos(theta_3) * np.cos(theta_4) - L_5 * np.sin(theta_1) * np.sin(theta_2) * np.sin(theta_3) * np.cos(theta_4) - L_5 * np.sin(theta_1) * np.cos(theta_2) * np.cos(theta_3) * np.sin(theta_4) - L_5 * np.sin(theta_1) * np.sin(theta_2) * np.cos(theta_3) * np.sin(theta_4) + \
        L_4 * np.sin(theta_1) * np.cos(theta_2) * np.cos(theta_3) - L_4 * np.sin(theta_1) * np.sin(theta_2) * np.sin(theta_3) +\
        L_3 * np.sin(theta_1) * np.cos(theta_2))

    J_12 = -(L_5 * (np.cos(theta_1) * np.sin(theta_2) * np.cos(theta_3) * np.cos(theta_4) + np.cos(theta_1) * np.cos(theta_2) * np.sin(theta_3) * np.cos(theta_4) - np.cos(theta_1) * np.sin(theta_2) * np.cos(theta_3) * np.sin(theta_4) + np.cos(theta_1) * np.cos(theta_2) * np.cos(theta_3) * np.sin(theta_4)) +\
        L_4 * (np.cos(theta_1) * np.sin(theta_2) * np.cos(theta_3) + np.cos(theta_1) * np.cos(theta_2) * np.sin(theta_3)) +\
        L_3 * np.cos(theta_1) * np.sin(theta_2))

    J_13 = -(L_5 * (np.cos(theta_1) * np.cos(theta_2) * np.sin(theta_3) * np.cos(theta_4) + np.cos(theta_1) * np.sin(theta_2) * np.cos(theta_3) * np.cos(theta_4) - np.cos(theta_1) * np.cos(theta_2) * np.sin(theta_3) * np.cos(theta_4) - np.cos(theta_1) * np.sin(theta_2) * np.sin(theta_3) * np.sin(theta_4)) +\
        L_4 * (np.cos(theta_1) * np.cos(theta_2) * np.sin(theta_3) + np.cos(theta_1) * np.sin(theta_2) * np.cos(theta_3)))

    J_14 = -(L_5 * (np.cos(theta_1) * np.cos(theta_2) * np.cos(theta_3) * np.sin(theta_4) - np.cos(theta_1) * np.sin(theta_2) * np.sin(theta_3) * np.sin(theta_4) + np.cos(theta_1) * np.cos(theta_2) * np.cos(theta_3) * np.cos(theta_4) + np.cos(theta_1) * np.sin(theta_2) * np.cos(theta_3) * np.cos(theta_4)))

    J_21 = -(L_5 * (-np.cos(theta_1) * np.cos(theta_2) * np.cos(theta_3) * np.cos(theta_4) + np.cos(theta_1) * np.sin(theta_2) * np.sin(theta_3) * np.cos(theta_4) + np.cos(theta_1) * np.cos(theta_2) * np.sin(theta_3) * np.sin(theta_4) + np.cos(theta_1) * np.sin(theta_2) * np.cos(theta_3) * np.sin(theta_4)) +\
        L_4 * np.cos(theta_1) * (-np.cos(theta_2) * np.cos(theta_3) + np.sin(theta_2) * np.sin(theta_3)) +\
        L_3 * -np.cos(theta_1) * np.cos(theta_2))

    J_22 = -(L_5 * np.sin(theta_1) * (np.sin(theta_2) * np.cos(theta_3) * np.cos(theta_4) + np.cos(theta_2) * np.sin(theta_3) * np.cos(theta_4) - np.sin(theta_2) * np.sin(theta_3) * np.sin(theta_4) + np.cos(theta_2) * np.cos(theta_3) * np.sin(theta_4)) +\
        L_4 * np.sin(theta_1) * (np.sin(theta_2) * np.cos(theta_3) + np.cos(theta_2) * np.sin(theta_3)) +\
        L_3 * np.sin(theta_1) * np.sin(theta_2))

    J_23 = -(L_5 * np.sin(theta_1) * (np.cos(theta_2) * np.sin(theta_3) * np.cos(theta_4) + np.sin(theta_2) * np.cos(theta_3) * np.cos(theta_4) + np.cos(theta_2) * np.cos(theta_3) * np.sin(theta_4) - np.sin(theta_2) * np.sin(theta_3) * np.sin(theta_4)) +\
        L_4 * np.sin(theta_1) * (np.cos(theta_2) * np.sin(theta_3) + np.sin(theta_2) * np.cos(theta_3)))

    J_24 = -( L_5 * np.sin(theta_1) * (np.cos(theta_2) * np.cos(theta_3) * np.sin(theta_4) - np.sin(theta_2) * np.sin(theta_3) * np.sin(theta_4) + np.cos(theta_2) * np.sin(theta_3) * np.cos(theta_4) + np.sin(theta_2) * np.cos(theta_3) * np.cos(theta_4)))

    J_31 = 0

    J_32 = L_5 * (np.cos(theta_2) * np.cos(theta_3) * np.cos(theta_4) - np.sin(theta_2) * np.sin(theta_3) * np.cos(theta_4) - np.cos(theta_2) * np.sin(theta_3) * np.sin(theta_4) - np.sin(theta_2) * np.cos(theta_3) * np.sin(theta_4)) +\
        L_4 * np.cos(theta_2) * np.cos(theta_3) - L_4 * np.sin(theta_2) * np.sin(theta_3) +\
        L_3 * np.cos(theta_2)

    J_33 = L_5 * (-np.sin(theta_2) * np.sin(theta_3) * np.cos(theta_4) + np.cos(theta_2) * np.cos(theta_3) * np.cos(theta_4) - np.sin(theta_2) * np.cos(theta_3) * np.sin(theta_4)- np.cos(theta_2) * np.sin(theta_3) * np.sin(theta_4)) +\
        L_4 * (-np.sin(theta_2) * np.sin(theta_3) + np.cos(theta_2) * np.cos(theta_3))

    J_34 = L_5 * (np.cos(theta_2) * np.cos(theta_3) * np.cos(theta_4) - np.sin(theta_2) * np.sin(theta_3) * np.cos(theta_4) - np.cos(theta_2) * np.sin(theta_3) * np.sin(theta_4) - np.sin(theta_2) * np.cos(theta_3) * np.sin(theta_4))

    omega_1_b = [[0],[0],[1]]
    omega_2_b = [[-np.sin(theta_1)], [np.cos(theta_1)], 0]
    omega_3_b = [[-np.sin(theta_1)], [np.cos(theta_1)], 0]
    omega_4_b = [[-np.sin(theta_1)], [np.cos(theta_1)], 0]

    J = np.array([[J_11, J_12, J_13, J_14],
         [J_21, J_22, J_23, J_24],
         [J_31, J_32, J_33, J_34],
         [0, -np.sin(theta_1), -np.sin(theta_1), -np.sin(theta_1)],
         [0, np.cos(theta_1), np.cos(theta_1), np.cos(theta_1)],
         [1, 0, 0, 0]])

    return J

def Inverse_Jacobian(J): #J is not inversible, so use Moore–Penrose inverse,
    J_inverse_sub1 = np.matmul(np.transpose(J),J)
    J_inverse_sub2 = np.linalg.inv(J_inverse_sub1)
    J_inverse = np.matmul(J_inverse_sub2, np.transpose(J))

    return J_inverse

J = Jacobian(np.pi, np.pi/2, np.pi/4, np.pi/3)
print('this is the jacobian',J)

v = np.array([[3],[0],[0],[0],[0],[0]])
q = np.matmul(Inverse_Jacobian(J),v)

#print(q)