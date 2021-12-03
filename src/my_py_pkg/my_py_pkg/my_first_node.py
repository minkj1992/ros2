#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

def main(args=None):
    node = Node()
    rclpy.init(args=args)
    rclpy.spin()
    rclpy.shutdown()


if __name__ == "__main__":
    main()