#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String


class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("robot_news_station")
        # msg_type, topic: str, qos_profile: Union[QoSProfile, int],
        # ros convention for variable: <keyword>_
        self.publisher_ = self.create_publisher(msg_type=String,
                                                topic="robot_news",
                                                qos_profile=10)
        self.timer_ = self.create_timer(0.5, self.publish_news)

        self.robot_name = "C3PO"
        self._greeting()

    def _greeting(self):
        self.get_logger().info("Robot News has been started.")

    def publish_news(self):
        msg = String(
            data=f"Hi, this is {self.robot_name} from the robot news station.")
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
