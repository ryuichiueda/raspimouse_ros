#!/bin/bash -xve

git clone https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu16.04_server.git
cd ./ros_setup_scripts_Ubuntu16.04_server
bash ./step0.bash
bash ./step1.bash

source ~/.bashrc
mkdir -p ~/catkin_ws/src/
cd ~/catkin_ws/src
catkin_create_pkg raspimouse_ros std_msgs rospy --rosdistro kinetic
cd ~/catkin_ws
catkin_make
cd ~/catkin_ws/src/
git clone https://github.com/ryuichiueda/raspimouse_ros.git
roslaunch raspimouse_ros travis_test.launch
