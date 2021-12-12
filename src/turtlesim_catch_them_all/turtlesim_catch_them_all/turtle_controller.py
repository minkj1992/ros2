#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.pose_ = None
        self.pose_subscriber_ = self.create_subscription(
            Pose,
            topic="turtle1/pose",
            callback=self.callback_turtle_pose,
            qos_profile=10,
        )
        print(" hello")

    def callback_turtle_pose(self, msg):
        self.pose_ = msg


def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
