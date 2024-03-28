import numpy as np

def IK(test_point):
    link_length_1 = 60
    link_length_2 = 20
    link_length_3 = 95
    link_length_4 = 105
    link_length_5 = 60
    length_joint_end = 30
    angle_joint_1_max = np.deg2rad(100)
    angle_joint_1_min = np.deg2rad(-90)
    angle_joint_2_max = np.deg2rad(38)
    angle_joint_2_min = np.deg2rad(-90)
    angle_joint_3_max = np.deg2rad(60)  # -90
    angle_joint_3_min = np.deg2rad(-90)  # 60
    angle_joint_4_max = np.deg2rad(90)
    angle_joint_4_min = np.deg2rad(-90)

    x_end = test_point[0]
    y_end = test_point[1] - link_length_1 - link_length_2
    z_end = test_point[2]

    distance = np.sqrt(x_end * 2 + y_end2 + z_end * 2)
    sums = link_length_1 + link_length_2 + link_length_3 + link_length_4 + link_length_5
    print(distance, sums)
    if distance > link_length_1 + link_length_2 + link_length_3 + link_length_4 + link_length_5:
        print('out of reach')
        return 0

    if x_end != 0:
        angle_1 = [np.arctan2(z_end, x_end), np.pi - np.arctan2(z_end, x_end)]
    else:
        angle_1 = [np.pi / 2, -np.pi / 2]
    if test_point == [100, 100, 100]:
        angle_1 = [-np.pi / 4, 0]
    elif test_point == [0, 300, 0]:
        angle_1 = [0, 0]
    for i in np.linspace(-np.pi, np.pi, 360):
        xz = np.sqrt(x_end * 2 + z_end * 2)
        orientation = i
        xz_5 = xz - (link_length_5 + length_joint_end) * np.cos(orientation)
        y_5 = y_end - (link_length_5 + length_joint_end) * np.sin(orientation)

        alpha = np.arccos((xz_5 * 2 + y_52 - link_length_32 - link_length_4 * 2) / (2 * link_length_3 * link_length_4))
        # alpha = np.pi - alpha
        print('alpha', (xz_5 * 2 + y_52 - link_length_32 - link_length_4 * 2) / (2 * link_length_3 * link_length_4))
        beta = np.arcsin((link_length_4 * np.sin(alpha)) / (np.sqrt(xz_5 * 2 + y_5 * 2)))

        elbow = 1  # -1 if down, 1 if up

        theta_1 = np.arctan2(y_5, xz_5) + beta * elbow
        # print(np.rad2deg(theta_1),'theta 1', np.rad2deg(np.arctan2(y_5, xz_5)), beta)
        theta_2 = -elbow * (np.pi - alpha) + theta_1
        theta_3 = orientation

        thetas = [theta_1, theta_2, theta_3]
        theta_1_x = theta_1
        angle_1[0] = -angle_1[0]
        theta_1 = theta_1 - np.pi / 2
        theta_2 = -(alpha - np.pi / 2)  # +angle_joint_2
        # theta_2=-(theta_2+np.pi/2)

        theta_3 = theta_3 - theta_1 - theta_2
        theta_2 = -theta_2  # +np.pi/2#-np.pi/2
        if angle_joint_2_min <= theta_1 <= angle_joint_2_max and angle_joint_3_min <= theta_2 <= angle_joint_3_max and angle_joint_4_min <= theta_3 <= angle_joint_4_max:
            print('angles rad', [angle_1[0], theta_1, theta_2, theta_3])
            print('angles deg', np.rad2deg(theta_1), np.rad2deg(theta_2), np.rad2deg(theta_3))

            print(x_end, y_end, z_end)

    return angle_1[0], theta_1, theta_2, theta_3


# IK([100,100,100])
# IK([0,300,0])
IK([200, 300, 100])