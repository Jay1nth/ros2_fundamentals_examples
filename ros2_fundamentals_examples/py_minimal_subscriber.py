#! /usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MinimalPySubscriber(Node):
  def __init__(self):
    super().__init__('minimal_py_subscriber')

    self.publisher_1 = self.create_subscription(
      String,
      'py_example_topic',
      self.listener_callback,
      10
    )
  
  def listener_callback(self,msg):
    self.get_logger().info(f'i heard: "{msg.data}"')


def main(args=None):
  rclpy.init(args=args)

  minimal_py_subscriber = MinimalPySubscriber()
  
  rclpy.spin(minimal_py_subscriber)
  
  minimal_py_subscriber.destroy_node()

  rclpy.shutdown()

if __name__ == '__main__':
   main()
  