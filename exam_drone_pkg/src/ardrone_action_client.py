#! /usr/bin/env python3

import rospy
import actionlib
from exam_drone_pkg.msg import ArdroneMoveAction, ArdroneMoveGoal

def feedback_callback(feedback):
    rospy.loginfo(feedback.status)

def ardrone_client():
    client = actionlib.SimpleActionClient('ardrone_move', ArdroneMoveAction)
    client.wait_for_server()
    
    while not rospy.is_shutdown():
        user_input = input("Enter command (takeoff/land) or 'exit' to quit: ").strip().lower()
        
        if user_input == 'exit':
            break
        
        goal = ArdroneMoveGoal(command=user_input)
        client.send_goal(goal, feedback_cb=feedback_callback)
        client.wait_for_result()

if __name__ == '__main__':
    try:
        rospy.init_node('ardrone_action_client_node')
        ardrone_client()
    except rospy.ROSInterruptException:
        pass
