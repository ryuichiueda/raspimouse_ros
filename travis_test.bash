#!/bin/bash -xve

git clone https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu14.04_server.git
cd ./ros_setup_scripts_Ubuntu14.04_server
bash ./step0.bash
bash ./step1.bash

source ~/.bashrc
mkdir -p ~/catkin_ws/src/
cd ~/catkin_ws/src
PATH=$PATH:/opt/ros/indigo/bin/
catkin_init_workspace
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
cd ~/catkin_ws/src/
git clone https://github.com/ryuichiueda/raspimouse_ros.git
roslaunch raspimouse_ros travis_test.launch
