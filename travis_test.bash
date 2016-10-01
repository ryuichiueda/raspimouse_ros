#!/bin/bash -xve

git clone https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu16.04_server.git
cd ./ros_setup_scripts_Ubuntu16.04_server
bash ./step0.bash
bash ./step1.bash

source ~/.bashrc
mkdir -p ~/catkin_ws/src/
cd !$
catkin_create_pkg raspimouse_ros std_msgs rospy
cd ~/catkin_ws
catkin_make
cd ~/catkin_ws/src/
git clone https://github.com/ryuichiueda/raspimouse_ros.git
roslaunch raspimouse_ros raspimouse.launch
