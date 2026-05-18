cmake_minimum_required(VERSION 3.0.2)
project(exam_drone_pkg)

find_package(catkin REQUIRED COMPONENTS
  actionlib
  actionlib_msgs
  rospy
  std_msgs
  geometry_msgs
  message_generation
)

add_action_files(
  FILES
  ArdroneMove.action
)

generate_messages(
  DEPENDENCIES
  actionlib_msgs
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS actionlib actionlib_msgs rospy std_msgs geometry_msgs message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  src/ardrone_action_server.py
  src/ardrone_action_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
