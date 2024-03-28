import numpy as np
from Workspace import *

# L_1 = link_length_1
# L_2 = link_length_2
# L_3 = link_length_3
# L_4 = link_length_4
# L_5 = link_length_5
#
# point_x = 100
# point_y = 100
# point_z = 100
#
# count = 0
# for theta_1 in range(np.deg2rad(-90), np.deg2rad(100)+0.1,0.1):
#     for theta_2 in range(np.deg2rad(-50), np.deg2rad(90)+0.1,0.1):
#         for theta_3 in range(np.deg2rad(-70), np.deg2rad(90)+0.1, 0.1):
#             for theta_4 in range(np.deg2rad(-90), np.deg2rad(90)+0.1,0.1):
#                 x_ref = L_3 * np.cos(theta_2) + L_4 * np.cos(theta_2 + theta_3) + L_5 * np.cos(theta_2 + theta_3 + theta_4)
#                 x = x_ref * np.cos(theta_1)
#                 y = x_ref * np.sin(theta_1)
#                 z = L_1 + L_2 + L_3 * np.cos(theta_2) + L_4 * np.cos(theta_2 + theta_3) + L_5 * np.cos(theta_2 + theta_3 + theta_4)
#                 count = count + 1
#                 print(count)
#                 if abs(x - point_x) <= 0.5:
#                     print('x',x)
#                 elif abs(y-point_y) <= 0.5:
#                     print('y',y)
#                 elif abs(z-point_z) <= 0.5:
#                     print('z',z)
#

import numpy as np

L_1 = link_length_1
L_2 = link_length_2
L_3 = link_length_3
L_4 = link_length_4
L_5 = link_length_5

point_x = 0
point_y = 0
point_z = L_1 +L_2+L_3+L_4+L_5

tolerance = 50
position_found = False

for theta_1 in np.arange(np.deg2rad(-100), np.deg2rad(90) + 0.1, 0.1):
    for theta_2 in np.arange(np.deg2rad(38), np.deg2rad(180) + 0.1, 0.1):
        for theta_3 in np.arange(np.deg2rad(90), np.deg2rad(240) + 0.1, 0.1):
            for theta_4 in np.arange(np.deg2rad(90), np.deg2rad(270) + 0.1, 0.1):
                x_ref = L_3 * np.cos(theta_2) + L_4 * np.cos(theta_2 + theta_3) + L_5 * np.cos(
                    theta_2 + theta_3 + theta_4)
                x = x_ref * np.cos(theta_1)
                y = x_ref * np.sin(theta_1)
                z = L_1 + L_2 + L_3 * np.cos(theta_2) + L_4 * np.cos(theta_2 + theta_3) + L_5 * np.cos(
                    theta_2 + theta_3 + theta_4)

                if abs(x - point_x) <= tolerance and abs(y - point_y) <= tolerance and abs(z - point_z) <= tolerance:
                    print(f"Found position within tolerance: x={x}, y={y}, z={z}")
                    position_found = True
                    break  # Exit the loop once the position within tolerance is found
            else:
                continue  # Continue to the next iteration of the inner loop if position not found
            break  # Exit the inner loop if position within tolerance is found
        else:
            continue  # Continue to the next iteration of the middle loop if position not found
        break  # Exit the middle loop if position within tolerance is found
    else:
        continue  # Continue to the next iteration of the outer loop if position not found
    break  # Exit the outer loop if position within tolerance is found

if not position_found:
    print("No valid position found within the tolerance range.")