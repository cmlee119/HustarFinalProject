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

import time

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        # self.publisher_ = self.create_publisher(String, 'topic', 10)
        # timer_period = 0.5  # seconds
        # self.timer = self.create_timer(timer_period, self.timer_callback)
        # self.i = 0


        self.publisher_gotopose = self.create_publisher(PoseStamped, 'move_base_simple/goal', 10)
        # timer_period = 0.5  # seconds
        # self.timer = self.create_timer(timer_period, self.GoToPose)
        # self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

    def GoToPose(self, x = 3.6, y = 0, qx = 0, qy = 0, qz = 0, qw = 1):
        print('GoToPose start')
        msg = PoseStamped()
        msg.header.frame_id = 'map'
        # msg.header.stamp = self.get_clock().now()

        point = Point()
        point.x = float(x)
        point.y = float(y)
        quaternion = Quaternion()
        quaternion.x = float(qx)
        quaternion.y = float(qy)
        quaternion.z = float(qx)
        quaternion.w = float(qw)

        print(point, quaternion)

        pose = Pose()
        pose.position = point
        pose.orientation = quaternion

        msg.pose = pose
        self.publisher_gotopose.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    minimal_publisher.GoToPose(3.6, 0, 0, 0, 0, 1)
    time.sleep(1)
    minimal_publisher.GoToPose(3.6, 0, 0, 0, 0, 1)
    time.sleep(1)

    # rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
