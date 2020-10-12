# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist, Pose, Point, Quaternion, PoseStamped, PoseWithCovariance, TransformStamped
from nav_msgs.msg import Odometry
from tf2_msgs.msg import TFMessage


class MinimalSubscriber(Node):

    def __init__(self):
        print('__init__ start')

        super().__init__('minimal_subscriber')
        # self.subscription = self.create_subscription(
        #     Odometry,
        #     '/odom',
        #     self.listener_callback_odom,
        #     10)

        self.subscription = self.create_subscription(
            TFMessage,
            '/tf',
            self.listener_callback_tf,
            10)

        print('__init__ end')

    def listener_callback_odom(self, msg):
        print(msg.pose.pose.position, msg.pose.pose.orientation)

    def listener_callback_tf(self, msg):
        print(msg.pose.pose.position, msg.pose.pose.orientation)


def main(args=None):
    print('main start')

    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
