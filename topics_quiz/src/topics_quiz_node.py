#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

echipa = "AC-DC"

cmd = Twist()
pub = None

def my_callback(msg):
    length = len(msg.ranges)

    front_idx = length // 2
    right_idx = 0
    left_idx = length - 1

    front_dist = msg.ranges[front_idx]
    right_dist = msg.ranges[right_idx]
    left_dist = msg.ranges[left_idx]

    cmd.linear.x = 0.0
    cmd.angular.z = 0.0

    if front_dist < 1.0:
        cmd.angular.z = 0.5
    elif right_dist < 1.0:
        cmd.angular.z = 0.5
    elif left_dist < 1.0:
        cmd.angular.z = -0.5
    else:
        cmd.linear.x = 0.3

    pub.publish(cmd)

rospy.init_node('topics_quiz_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber('/scan', LaserScan, my_callback)
rospy.spin()
