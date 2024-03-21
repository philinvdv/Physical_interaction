import numpy as np
from matplotlib import pyplot as plt
from Workspace import *
from InverseKinematics import *


####################
#Visualising the robot arm in 3D for user input angles
plotter(arm(0)) #0 if use [0,-90,0,0], 1 if user input
####################
###possible points in 2D for z=0
Workspace2D(20)
#####################
#Plotting possible end points, input number of iterations
plotter(all_end_pointer(6))

####################

test_point_1=[100,100,200]
test_point_2=[200,100,300]  #out of reach i think
test_point_3=[0,0,300]
test_point_4=[0,0,70]

#Inverse Kinematics, finding the angles
angles=IK(test_point_1)
print(angles,'angles')
########################################
print(end_pointer(angles[0][0],np.deg2rad(angles[1]),np.deg2rad(angles[2]),np.deg2rad(angles[3])))

####################
#PLotter for the angles from inverse kinematics
inverse_plotter(angles)


