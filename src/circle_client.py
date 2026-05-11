#! /usr/bin/env python3
import rospy
from exam_pkg.srv import MoveCircle, MoveCircleRequest

rospy.init_node('circle_client_node')
rospy.wait_for_service('/move_circle')
try:
    move_circle = rospy.ServiceProxy('/move_circle', MoveCircle)
    request = MoveCircleRequest()
    request.radius = 0.5
    result = move_circle(request)
except rospy.ServiceException:
    pass
