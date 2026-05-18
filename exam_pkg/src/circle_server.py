#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from exam_pkg.srv import MoveCircle, MoveCircleResponse
from math import pi 

nume_echipa = "AC-DC"

def my_callback(request):
    rospy.loginfo("Request pentru cerc!")
    vel = Twist()
    
    v = 0.2
    w = v / request.radius
    
    vel.linear.x = v
    vel.angular.z = w
    
    '''
    folosisem 3.14 pentru forumla razei prima data dar nu
    mergea prea bine
    apoi am importat pi din math si a mers mai ok
    '''

    timp_cerc = (2 * pi * request.radius) / v  
    
    start_time = rospy.Time.now().to_sec()
    while rospy.Time.now().to_sec() - start_time < timp_cerc:
        pub.publish(vel)
        rospy.sleep(0.1)
            
    vel.linear.x = 0
    vel.angular.z = 0
    pub.publish(vel)
    
    res = MoveCircleResponse()
    res.success = True
    return res

rospy.init_node('circle_server_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
service = rospy.Service('/move_circle', MoveCircle, my_callback)
rospy.spin()
