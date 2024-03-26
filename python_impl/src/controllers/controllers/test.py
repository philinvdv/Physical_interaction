import rclpy
import numpy as np
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration
import threading
import time


class ExampleTraj(Node):

    def __init__(self):

        super().__init__('minimal_publisher')

        self._HOME = [np.deg2rad(0), np.deg2rad(0),
                      np.deg2rad(0), np.deg2rad(0), 0.0]
        self._beginning = self.get_clock().now()
        self._publisher = self.create_publisher(JointTrajectory, 'joint_cmds', 10)
        timer_period = 0.04  # seconds
        self._points_published = 100

        self._timer = self.create_timer(timer_period, self.timer_callback)
        self._trajectory = [[132, 85, 0], [172, 3.6, 0], [132, 85, 0], [0, 85, 132],
                            [0, 0, 175]]  # [[132,85,0],[0,0,230]]
        self._trajectory_point = 0
        self._clamp = 0.0
        self._trajectory_angles = [self._HOME]
        for i in self._trajectory:
            self._trajectory_angles.append(self.IK(i))
        # print('self angles', self._trajectory_angles[0][0])

    def timer_callback(self):

        now = self.get_clock().now()
        msg = JointTrajectory()
        msg.header.stamp = now.to_msg()

        dt = (now - self._beginning).nanoseconds * (1e-9)

        angles = self._trajectory_angles[self._trajectory_point + 1]
        old_angles = self._trajectory_angles[self._trajectory_point]
        print('angles', angles)
        print('old angles', old_angles)
        # angles=[ [0,1], np.deg2rad(-30), np.deg2rad(-30), np.deg2rad(-90)]
        print('angles', np.rad2deg(angles[0]), np.rad2deg(angles[1]), np.rad2deg(angles[2]), np.rad2deg(angles[3]))
        if self._points_published == 100:
            point = JointTrajectoryPoint()
            # print(point)

            point.positions = [
                self._HOME[0],
                self._HOME[1],  # Assuming you want to modify the position of the second joint as well
                self._HOME[2],  # Keeping the position of the third joint unchanged
                self._HOME[3],  # Keeping the position of the fourth joint unchanged
                0.0  # Keeping the position of the fifth joint unchanged
            ]

            msg.points = [point]
            self._publisher.publish(msg)
            self._points_published = 0
            time.sleep(1.5)
            self._beginning = self.get_clock().now()

        elif self._points_published == 0:
            # First point
            point = JointTrajectoryPoint()

            # print(angles)
            point.positions = [self._HOME[0] + old_angles[0] + (-old_angles[0] + angles[0]) * dt * 000.1,
                               self._HOME[1] + old_angles[1] + (-old_angles[1] + angles[1]) * dt * 000.1,
                               self._HOME[2] + old_angles[2] + (-old_angles[2] + angles[2]) * dt * 000.1,
                               self._HOME[3] + old_angles[3] + (-old_angles[3] + angles[3]) * dt * 000.1,
                               self._clamp]
            # point.time_from_start.sec = 100
            print('current point', point.positions)
            # time.sleep(2)
            a1 = 0
            a2 = 0
            a3 = 0
            a4 = 0
            if abs(point.positions[0] - angles[0]) <= 0.1:
                # time.sleep(2)
                # self._turn_time=dt
                point.positions[0] = angles[0]
                a1 = 1
            if abs(point.positions[1] - angles[1]) <= 0.1:
                # time.sleep(2)
                # self._turn_time=dt
                point.positions[1] = angles[1]
                a2 = 1
            if abs(point.positions[2] - angles[2]) <= 0.1:
                # time.sleep(2)
                # self._turn_time=dt
                point.positions[2] = angles[2]
                a3 = 1
            if abs(point.positions[3] - angles[3]) <= 0.1:
                # time.sleep(2)
                # self._turn_time=dt
                point.positions[3] = angles[3]
                a4 = 1

            if a1 == a2 == a3 == a4 == 1:
                # self._points_published = 1

                self._beginning = self.get_clock().now()

                if self._trajectory_point == 0:
                    self._trajectory_point = self._trajectory_point + 1
                elif self._trajectory_point == 1:
                    self._points_published = 1
                    # time.sleep(1)
                    self._beginning = self.get_clock().now()
                elif self._trajectory_point == 2:
                    self._trajectory_point = self._trajectory_point + 1
                elif self._trajectory_point == 3:
                    self._trajectory_point = self._trajectory_point + 1
                elif self._trajectory_point == 4:
                    self._points_published = 2
                    # time.sleep(1)
                    self._beginning = self.get_clock().now()
                # if self._trajectory_point>=(len(self._trajectory)-1):

                #    self._points_published = 2
                # else:
                #    self._trajectory_point=self._trajectory_point+1

            print(a1, a2, a3, a4)
            msg.points = [point]
            self._publisher.publish(msg)

        elif self._points_published == 1:
            point = JointTrajectoryPoint()
            # print(dt)
            point.positions = [self._HOME[0] + angles[0],
                               self._HOME[1] + angles[1],
                               self._HOME[2] + angles[2],
                               self._HOME[3] + angles[3],
                               self._clamp + dt]

            print(point.positions[4], 'clamp')
            msg.points = [point]
            self._publisher.publish(msg)
            if point.positions[4] >= 0.8:
                self._points_published = 0
                self._clamp = 0.8
                self._trajectory_point = self._trajectory_point + 1
                # time.sleep(1)
                self._beginning = self.get_clock().now()
                # self._trajectory_point=self._trajectory_point+1
            # time.sleep(1.5)
        elif self._points_published == 2:
            point = JointTrajectoryPoint()
            # print(dt)
            point.positions = [self._HOME[0] + angles[0],
                               self._HOME[1] + angles[1],
                               self._HOME[2] + angles[2],
                               self._HOME[3] + angles[3],
                               self._clamp - dt]

            print(point.positions[4], 'clamp')
            msg.points = [point]
            self._publisher.publish(msg)
            if point.positions[4] <= 0.0:
                self._points_published = 3
                self._beginning = self.get_clock().now()
                # self._trajectory_point=self._trajectory_point+1
            # time.sleep(1.5)








        else:
            # Stop publishing
            self._timer.cancel()

    def IK(self, test_point):
        link_length_1 = 30
        link_length_2 = 50
        link_length_3 = 115
        link_length_4 = 132
        link_length_5 = 75
        length_joint_end = 35
        angle_joint_1_max = np.deg2rad(100)
        angle_joint_1_min = np.deg2rad(-90)
        angle_joint_2_max = np.deg2rad(38)
        angle_joint_2_min = np.deg2rad(-90)
        angle_joint_3_max = np.deg2rad(0)
        angle_joint_3_min = np.deg2rad(-150)
        angle_joint_4_max = np.deg2rad(90)
        angle_joint_4_min = np.deg2rad(-90)

        x_end = test_point[0]
        y_end = test_point[1] - link_length_1 - link_length_2
        z_end = test_point[2]

        distance = np.sqrt(x_end ** 2 + y_end ** 2 + z_end ** 2)

        if distance > link_length_1 + link_length_2 + link_length_3 + link_length_4 + link_length_5:
            print('out of reach')
            return 0

        if x_end != 0:
            angle_1 = [np.arctan2(z_end, x_end), np.pi - np.arctan2(z_end, x_end)]
        else:
            angle_1 = [np.pi / 2, -np.pi / 2]

        xz = np.sqrt(x_end ** 2 + z_end ** 2)
        orientation = np.deg2rad(-90)
        xz_5 = xz - (link_length_5 + length_joint_end) * np.cos(orientation)
        y_5 = y_end - (link_length_5 + length_joint_end) * np.sin(orientation)

        alpha = np.arccos(
            (xz_5 ** 2 + y_5 ** 2 - link_length_3 ** 2 - link_length_4 ** 2) / (2 * link_length_3 * link_length_4))
        # alpha = np.pi - alpha

        beta = np.arcsin((link_length_4 * np.sin(alpha)) / (np.sqrt(xz_5 ** 2 + y_5 ** 2)))

        elbow = 1  # -1 if down, 1 if up

        theta_1 = np.arctan2(y_5, xz_5) + beta * elbow
        print(np.rad2deg(theta_1), 'theta 1', np.rad2deg(np.arctan2(y_5, xz_5)), beta)
        theta_2 = -elbow * (np.pi - alpha) + theta_1
        theta_3 = orientation

        thetas = [theta_1, theta_2, theta_3]
        theta_1_x = theta_1
        angle_1[0] = -angle_1[0]
        theta_1 = theta_1 - np.pi / 2
        theta_2 = -(alpha - np.pi / 2)  # +angle_joint_2
        # theta_2=-(theta_2+np.pi/2)
        theta_3 = theta_3 - theta_1 - theta_2  # +np.pi/2#-np.pi/2

        return angle_1[0], theta_1, -theta_2, theta_3


def main(args=None):
    rclpy.init(args=args)

    example_traj = ExampleTraj()

    rclpy.spin(example_traj)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    example_traj.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()