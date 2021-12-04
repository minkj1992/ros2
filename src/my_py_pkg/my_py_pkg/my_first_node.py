#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self, node_name):
        super().__init__(node_name)
        
        self._counter = 0
        self.logger = self.get_logger()

        self.create_timer(timer_period_sec=0.5, callback=self.timer_callback)

    def greeting(self):
        self.logger.info(f"Hello ROS2")

    def timer_callback(self):
        self._counter += 1
        self.logger.info(f"CURRNET COUNT is {self._counter}")


def main(args=None):
    rclpy.init(args=args)
    node = MyNode("my_node")
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()