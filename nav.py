#!/usr/bin/env python3

import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
import tf_transformations
from hilbertcurve.hilbertcurve import HilbertCurve

class FullCoverageNavigator:
    """
    @class FullCoverageNavigator
    @brief Class for navigating a robot to achieve full coverage using a Hilbert curve.
    """

    def __init__(self):
        """
        @brief Constructor method for FullCoverageNavigator class.
        """
        self.nav = BasicNavigator()
        self.map_resolution = 0.05  # Resolution of the occupancy grid map (meters per cell)
        self.hilbert_curve_order = 3  # Order of Hilbert curve
        self.waypoints = []

    def generate_waypoints(self):
        """
        @brief Generates waypoints along a Hilbert curve within the specified cell size.
        """
        # Define the size of the cell (in meters)
        cell_size = 5.5
    
        # Define the resolution of the Hilbert curve (number of points along one dimension)
        curve_resolution = 10  # Adjust as needed
    
        # Create a Hilbert curve
        hilbert_curve = HilbertCurve(self.hilbert_curve_order, 2)
    
        # Generate waypoints along the Hilbert curve within one cell
        for i in range(curve_resolution ** 2):
            # Convert 1D Hilbert index to 2D coordinates within the cell
            x_hilbert, y_hilbert = hilbert_curve.point_from_distance(i)
        
            # Convert coordinates within the cell to real-world coordinates
            x = (x_hilbert / (curve_resolution - 1)) * cell_size
            y = (y_hilbert / (curve_resolution - 1)) * cell_size
        
            # Create PoseStamped message for the waypoint
            waypoint = self.create_pose_stamped(x, y, 0.0)
            self.waypoints.append(waypoint)


    def create_pose_stamped(self, position_x, position_y, orientation_z):
        """
        @brief Creates a PoseStamped message with the specified position and orientation.
        
        @param position_x: X-coordinate of the position.
        @param position_y: Y-coordinate of the position.
        @param orientation_z: Z-coordinate of the orientation.
        @return PoseStamped message.
        """
        q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, orientation_z)
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.nav.get_clock().now().to_msg()
        pose.pose.position.x = position_x
        pose.pose.position.y = position_y
        pose.pose.position.z = 0.0
        pose.pose.orientation.x = q_x
        pose.pose.orientation.y = q_y
        pose.pose.orientation.z = q_z
        pose.pose.orientation.w = q_w
        return pose

    def main(self):
        """
        @brief Main method for executing the navigation task.
        """
        self.generate_waypoints()

        # Set initial pose
        initial_pose = self.create_pose_stamped(0.0, 0.0, 0.0)
        self.nav.setInitialPose(initial_pose)

        # Wait for Nav2 to be active
        self.nav.waitUntilNav2Active()

        # Follow waypoints
        self.nav.followWaypoints(self.waypoints)

        # Wait until task is complete
        while not self.nav.isTaskComplete():
            pass

        print("Navigation task complete!")

if __name__ == '__main__':
    rclpy.init()
    navigator = FullCoverageNavigator()
    navigator.main()
    rclpy.shutdown()