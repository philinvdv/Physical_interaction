import numpy as np
from matplotlib import pyplot as plt
### Check for interference






link_length_1=30
link_length_2=50
link_length_3=115
link_length_4=132
link_length_5=75
length_joint_end=35
angle_joint_1_max=np.deg2rad(100)
angle_joint_1_min=np.deg2rad(-90)


#joint 2 rotation z -90,38
angle_joint_2_max=np.deg2rad(38)
angle_joint_2_min=np.deg2rad(-90)
#joint 3 rotation z -150, 0

angle_joint_3_max=np.deg2rad(0)
angle_joint_3_min=np.deg2rad(-150)
#joint 4 rotation z -90,90
angle_joint_4_max=np.deg2rad(90)
angle_joint_4_min=np.deg2rad(-90)
# Joint 1 rotation y -90, 100
# angle_joint_1 = np.deg2rad(0)
# angle_joint_1_max = np.deg2rad(100)
# angle_joint_1_min = np.deg2rad(-90)

# Joint 2 rotation z -90, 38
# angle_joint_2 = np.deg2rad(-90)
# angle_joint_2_max = np.deg2rad(38)
# angle_joint_2_min = np.deg2rad(-90)

# Joint 3 rotation z -150, 0
# angle_joint_3 = np.deg2rad(0)
# angle_joint_3_max = np.deg2rad(0)
# angle_joint_3_min = np.deg2rad(-150)

# Joint 4 rotation z -90, 90
# angle_joint_4 = np.deg2rad(0)
# angle_joint_4_max = np.deg2rad(90)
# angle_joint_4_min = np.deg2rad(-90)

# Uncomment the joint angles you need
# joint_angles = np.array([
#     angle_joint_1, angle_joint_1_max, angle_joint_1_min,
#     angle_joint_2, angle_joint_2_max, angle_joint_2_min,
#     angle_joint_3, angle_joint_3_max, angle_joint_3_min,
#     angle_joint_4, angle_joint_4_max, angle_joint_4_min
# ])

# Reshape the array to have three columns
# joint_angles = joint_angles.reshape((len(joint_angles) // 3, 3))

# Print the result
# print(joint_angles)

#define x,y,z x forward y up z right
def end_pointer(angle_joint_1,angle_joint_2,angle_joint_3,angle_joint_4):
    start_point =[0,0,0]

    #joint_location_3 =

    joint_location_1= [0,link_length_1,0]

    Rotational_1 = [ [ np.cos(angle_joint_1),0,np.sin(angle_joint_1)],[0, 1,0], [-np.sin(angle_joint_1),0,np.cos(angle_joint_1)]]
    joint_location_2_1=np.dot(Rotational_1,[0,link_length_2,0])
    joint_location_2= [i + j  for i, j in zip(joint_location_1, joint_location_2_1)]

    Rotational_2= [ [ np.cos(angle_joint_2),-np.sin(angle_joint_2),0], [np.sin(angle_joint_2),np.cos(angle_joint_2),0],[0, 0,1]]
    joint_location_3_2= np.dot(np.dot(Rotational_1,Rotational_2),[0,link_length_3,0])
    joint_location_3= [i + j  for i, j in zip(joint_location_2, joint_location_3_2)]

    Rotational_3= [ [ np.cos(angle_joint_3),-np.sin(angle_joint_3),0], [np.sin(angle_joint_3),np.cos(angle_joint_3),0],[0, 0,1]]
    joint_location_4_3 = np.dot(np.dot(Rotational_1,np.dot(Rotational_2, Rotational_3)),[0,link_length_4,0])
    joint_location_4= [i + j  for i, j in zip(joint_location_3, joint_location_4_3)]

    Rotational_4= [ [ np.cos(angle_joint_4),-np.sin(angle_joint_4),0], [np.sin(angle_joint_4),np.cos(angle_joint_4),0],[0, 0,1]]
    joint_location_5_4 = np.dot(np.dot(Rotational_1,np.dot(Rotational_2, np.dot(Rotational_3,Rotational_4))),[0,link_length_5,0])
    joint_location_5= [i + j  for i, j in zip(joint_location_4, joint_location_5_4)]

    end_point_end_4=np.dot(np.dot(Rotational_1,np.dot(Rotational_2, np.dot(Rotational_3,Rotational_4))),[0,length_joint_end,0])
    end_point=[i + j  for i, j in zip(joint_location_5, end_point_end_4)]

    # print(joint_location_1,'joint 1')
    # print(joint_location_2,'joint 2')
    # print(joint_location_3,'joint 3')
    # print(joint_location_4,'joint 4')
    # print(joint_location_5,'joint 5')
    # print(joint_location_5,'end_point')

    return end_point

def all_end_pointer(number):
    #joint 1 rotation y -90,100
    angle_joint_1= np.deg2rad(0)
    #angle_joint_1_max=np.deg2rad(100)
    #angle_joint_1_min=np.deg2rad(-90)
    #joint 2 rotation z -90,38
    angle_joint_2= np.deg2rad(-90)
    #angle_joint_2_max=np.deg2rad(38)
    #angle_joint_2_min=np.deg2rad(-90)
    #joint 3 rotation z -150, 0
    angle_joint_3=np.deg2rad(0)
    #angle_joint_3_max=np.deg2rad(0)
    #angle_joint_3_min=np.deg2rad(-150)
    #joint 4 rotation z -90,90
    angle_joint_4  = np.deg2rad(0)
    #angle_joint_4_max=np.deg2rad(90)
    #angle_joint_4_min=np.deg2rad(-90)
    end_points=[end_pointer(angle_joint_1,angle_joint_2,angle_joint_3,angle_joint_4)]
    end_points=[]

    for angle_joint_1 in np.linspace(angle_joint_1_min,angle_joint_1_max,number):
        print(angle_joint_1)
        for angle_joint_2 in np.linspace(angle_joint_2_min, angle_joint_2_max, number):
            for angle_joint_3 in np.linspace(angle_joint_3_min, angle_joint_3_max, number):
                for angle_joint_4 in np.linspace(angle_joint_4_min, angle_joint_4_max, number):
                    end=end_pointer(angle_joint_1,angle_joint_2,angle_joint_3,angle_joint_4)
                    print(end)
                    if end[1]>0:end_points.append(end)


    return end_points



def arm():
    print('The angle should be between',np.rad2deg(angle_joint_1_min),'and',np.rad2deg(angle_joint_1_max),'degrees')
    angle_joint_1=np.deg2rad(float(input('Angle of the rotating base in degrees')))
    print('The angle should be between', np.rad2deg(angle_joint_2_min), 'and', np.rad2deg(angle_joint_2_max), 'degrees')
    angle_joint_2 = np.deg2rad(float(input('Angle of joint 2 in degrees')))
    print('The angle should be between', np.rad2deg(angle_joint_3_min), 'and', np.rad2deg(angle_joint_3_max), 'degrees')
    angle_joint_3 = np.deg2rad(float(input('Angle of joint 3 in degrees')))
    print('The angle should be between', np.rad2deg(angle_joint_4_min), 'and', np.rad2deg(angle_joint_4_max), 'degrees')
    angle_joint_4 = np.deg2rad(float(input('Angle of joint 4 in degrees')))
    start_point =[0,0,0]

    #joint_location_3 =

    joint_location_1= [0,link_length_1,0]

    Rotational_1 = [ [ np.cos(angle_joint_1),0,np.sin(angle_joint_1)],[0, 1,0], [-np.sin(angle_joint_1),0,np.cos(angle_joint_1)]]
    joint_location_2_1=np.dot(Rotational_1,[0,link_length_2,0])
    joint_location_2= [i + j  for i, j in zip(joint_location_1, joint_location_2_1)]

    Rotational_2= [ [ np.cos(angle_joint_2),-np.sin(angle_joint_2),0], [np.sin(angle_joint_2),np.cos(angle_joint_2),0],[0, 0,1]]
    joint_location_3_2= np.dot(np.dot(Rotational_1,Rotational_2),[0,link_length_3,0])
    joint_location_3= [i + j  for i, j in zip(joint_location_2, joint_location_3_2)]

    Rotational_3= [ [ np.cos(angle_joint_3),-np.sin(angle_joint_3),0], [np.sin(angle_joint_3),np.cos(angle_joint_3),0],[0, 0,1]]
    joint_location_4_3 = np.dot(np.dot(Rotational_1,np.dot(Rotational_2, Rotational_3)),[0,link_length_4,0])
    joint_location_4= [i + j  for i, j in zip(joint_location_3, joint_location_4_3)]

    Rotational_4= [ [ np.cos(angle_joint_4),-np.sin(angle_joint_4),0], [np.sin(angle_joint_4),np.cos(angle_joint_4),0],[0, 0,1]]
    joint_location_5_4 = np.dot(np.dot(Rotational_1,np.dot(Rotational_2, np.dot(Rotational_3,Rotational_4))),[0,link_length_5,0])
    joint_location_5= [i + j  for i, j in zip(joint_location_4, joint_location_5_4)]

    end_point_end_4=np.dot(np.dot(Rotational_1,np.dot(Rotational_2, np.dot(Rotational_3,Rotational_4))),[0,length_joint_end,0])
    end_point=[i + j  for i, j in zip(joint_location_5, end_point_end_4)]

    print(joint_location_1,'joint 1')
    print(joint_location_2,'joint 2')
    print(joint_location_3,'joint 3')
    print(joint_location_4,'joint 4')
    print(joint_location_5,'joint 5')
    print(joint_location_5,'end_point')
    #link_points_1=[]
    #link_point_1=start_point
    #link_1_d=[ (j-i)/100  for i, j in zip(start_point, joint_location_1)]
    #print('link 1 d', link_1_d)
    #i=0
    #while i<7:
    #    print('i')
    #    link_point_1=[i + j  for i, j in zip(link_point_1, link_1_d)]
    #    link_points_1.append(link_point_1)
    #    i=i+1
    points = [
        start_point,
        joint_location_1,
        joint_location_2,
        joint_location_3,
        joint_location_4,
        joint_location_5,
        end_point
    ]
    return points#, link_points_1
#start_point =[0,0,0]

def plotter(end_points):

    # Extract x, y, and z coordinates from the points
    x = [point[0] for point in end_points]
    y = [point[1] for point in end_points]
    z = [point[2] for point in end_points]

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot the points
    ax.scatter(x, z, y, c='r', marker='o')
    i=0
    while i<6:
        ax.plot([x[i], x[i+1]], [z[i],z[i+1]], [y[i],y[i+1]], c='b', linestyle='-', linewidth=2)
        i=i+1


    # Set labels for the axes
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Z-axis')
    ax.set_zlabel('Y-axis')

    # Show the plot
    plt.show()
    return 0




#plotter(arm())
#plotter(all_end_pointer(10))