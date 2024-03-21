import numpy as np
from matplotlib import pyplot as plt
from Workspace import *

def IK(test_point):
    print('INVERSE KINEMATICS')
    x_end=test_point[0]
    y_end=test_point[1]-link_length_1-link_length_2
    z_end=test_point[2]
    #print(x_end)
    #print(y_end)
    #print(z_end)
    distance=np.sqrt(x_end**2+y_end**2+z_end**2)
    print(distance,'distance', link_length_3, 'link3',link_length_4,'link4')
    if distance>link_length_1+link_length_2+link_length_3+link_length_4+link_length_5:
        print('out of reach')
        return 0

    if x_end!=0:
        angle_1=[np.arctan2(z_end,x_end),np.pi-np.arctan2(z_end,x_end)]
    if x_end==0:
        angle_1=[np.pi/2, -np.pi/2]
    print(angle_1[0]*180/np.pi, 'base angle')
    #print(angle_1[1] * 180/np.pi)
    xz=np.sqrt(x_end**2+z_end**2)
    orientation =0
    xz_5=xz-(link_length_5+length_joint_end)*np.cos(orientation)
    y_5=y_end-(link_length_5+length_joint_end)*np.sin(orientation)
    print(y_5,'y_5')
    print(xz_5,'xz_5')
    #print('alpha input',(xz_5**2+y_5**2- link_length_3**2-link_length_4**2)/(2*link_length_3*link_length_4))
    alpha=np.arccos((xz_5**2+y_5**2- link_length_3**2-link_length_4**2)/(2*link_length_3*link_length_4))
    alpha=np.pi-alpha
    #alpha = np.arccos((link_length_3 ** 2 + link_length_4 ** 2 - xz_5 ** 2 - y_5 ** 2) / (2 * link_length_3 * link_length_4))
    #print((link_length_4*np.sin(alpha))/(np.sqrt(xz_5**2+y_5**2)), 'beta input')
    beta= np.arcsin((link_length_4*np.sin(alpha))/(np.sqrt(xz_5**2+y_5**2)))
    print('alpha',np.rad2deg(alpha),'beta',np.rad2deg(beta))

    elbow=1   ###-1 if down 1 if up


    theta_1= np.arctan2(y_5,xz_5)+beta*elbow
    theta_2 = -elbow*(np.pi-alpha)+theta_1
    theta_3=orientation
    print(np.rad2deg(theta_1), 'theta 1 in deg')
    print(np.rad2deg(theta_2), 'theta 2 in deg')
    print(np.rad2deg(theta_3), 'theta 3 in deg')
    thetas=[theta_1,theta_2,theta_3]
    Plotter_2D(thetas)
    return angle_1,theta_1, theta_2, theta_3



def Plotter_2D(thetas):
    lengths=[link_length_3,link_length_4,link_length_5+length_joint_end]
    x=0
    y=0

    # Plotting


    for length, angle in zip(lengths, thetas):
        # Convert angle to radians
        angle_rad = angle#np.radians(angle)

        x_new = x + length * np.cos(angle_rad)
        y_new = y + length * np.sin(angle_rad)

        # Plot line
        plt.plot([x, x_new], [y, y_new], marker='o')

        # Update position
        x=x_new
        y=y_new

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.axis('equal')
    plt.show()
    return 0






def inverse_plotter(angles):
    angle_joint_1=-angles[0][0]
    angle_joint_2=angles[1]-np.pi/2
    angle_joint_3=angles[2]-np.pi/2-angle_joint_2#+angle_joint_2
    angle_joint_4=angles[3]-angles[2]#+angle_joint_3

    print('angle join 1', np.rad2deg(angle_joint_1))
    print('angle join 2', np.rad2deg(angle_joint_2))
    print('angle join 3', np.rad2deg(angle_joint_3))
    print('angle join 4', np.rad2deg(angle_joint_4))
    if angle_joint_1_min <= angle_joint_1 <= angle_joint_1_max:
        print('angle 1 feasible')
    else:
        print('Angle 1 is not feasible')

    if angle_joint_2_min <= angle_joint_2 <= angle_joint_2_max:
        print('Angle 2 is feasible')
    else:
        print('Angle 2 is not feasible')


    if angle_joint_3_min <= angle_joint_3 <= angle_joint_3_max:
        print('Angle 3 is feasible')
    else:
        print('Angle 3 is not feasible')


    if angle_joint_4_min <= angle_joint_4 <= angle_joint_4_max:
        print('Angle 4 is feasible')
    else:
        print('Angle 4 is not feasible')








    start_point = [0, 0, 0]

    # joint_location_3 =

    joint_location_1 = [0, link_length_1, 0]

    Rotational_1 = [[np.cos(angle_joint_1), 0, np.sin(angle_joint_1)], [0, 1, 0],
                    [-np.sin(angle_joint_1), 0, np.cos(angle_joint_1)]]
    joint_location_2_1 = np.dot(Rotational_1, [0, link_length_2, 0])
    joint_location_2 = [i + j for i, j in zip(joint_location_1, joint_location_2_1)]

    Rotational_2 = [[np.cos(angle_joint_2), -np.sin(angle_joint_2), 0],
                    [np.sin(angle_joint_2), np.cos(angle_joint_2), 0], [0, 0, 1]]
    joint_location_3_2 = np.dot(np.dot(Rotational_1, Rotational_2), [0, link_length_3, 0])
    joint_location_3 = [i + j for i, j in zip(joint_location_2, joint_location_3_2)]

    Rotational_3 = [[np.cos(angle_joint_3), -np.sin(angle_joint_3), 0],
                    [np.sin(angle_joint_3), np.cos(angle_joint_3), 0], [0, 0, 1]]
    joint_location_4_3 = np.dot(np.dot(Rotational_1, np.dot(Rotational_2, Rotational_3)), [0, link_length_4, 0])
    joint_location_4 = [i + j for i, j in zip(joint_location_3, joint_location_4_3)]

    Rotational_4 = [[np.cos(angle_joint_4), -np.sin(angle_joint_4), 0],
                    [np.sin(angle_joint_4), np.cos(angle_joint_4), 0], [0, 0, 1]]
    joint_location_5_4 = np.dot(np.dot(Rotational_1, np.dot(Rotational_2, np.dot(Rotational_3, Rotational_4))),
                                [0, link_length_5, 0])
    joint_location_5 = [i + j for i, j in zip(joint_location_4, joint_location_5_4)]

    end_point_end_4 = np.dot(np.dot(Rotational_1, np.dot(Rotational_2, np.dot(Rotational_3, Rotational_4))),
                             [0, length_joint_end, 0])
    end_point = [i + j for i, j in zip(joint_location_5, end_point_end_4)]

    print(joint_location_1, 'joint 1')
    print(joint_location_2, 'joint 2')
    print(joint_location_3, 'joint 3')
    print(joint_location_4, 'joint 4')
    print(joint_location_5, 'joint 5')
    print(end_point, 'end_point')
    points = [
        start_point,
        joint_location_1,
        joint_location_2,
        joint_location_3,
        joint_location_4,
        joint_location_5,
        end_point
    ]

    plotter(points)
    return 0
