#! /usr/bin/env python3

import rospy
import actionlib
from exam_drone_pkg.msg import ArdroneMoveAction, ArdroneMoveFeedback, ArdroneMoveResult
from std_msgs.msg import Empty

class ArdroneMoveServer(object):
    _feedback = ArdroneMoveFeedback()
    _result = ArdroneMoveResult()

    def __init__(self):
        self.takeoff_pub = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=1)
        self.land_pub = rospy.Publisher('/ardrone/land', Empty, queue_size=1)
        self._as = actionlib.SimpleActionServer("ardrone_move", ArdroneMoveAction, self.goal_callback, False)
        self._as.start()

    def goal_callback(self, goal):
        command = goal.command.upper()
        
        if command == "TAKEOFF":
            self.takeoff_pub.publish(Empty())
            for i in range(3):
                self._feedback.status = "take off"
                self._as.publish_feedback(self._feedback)
                rospy.sleep(1.0)
            self._as.set_succeeded(self._result)
            
        elif command == "LAND":
            self.land_pub.publish(Empty())
            for i in range(3):
                self._feedback.status = "landing"
                self._as.publish_feedback(self._feedback)
                rospy.sleep(1.0)
            self._as.set_succeeded(self._result)
            
        else:
            self._as.set_aborted(self._result)

if __name__ == '__main__':
    rospy.init_node('ardrone_action_server_node')
    ArdroneMoveServer()
    rospy.spin()
