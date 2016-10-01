#!/bin/bash -xve

git clone https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu14.04_server.git
cd ./ros_setup_scripts_Ubuntu14.04_server
bash ./step0.bash
bash ./step1.bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
source /opt/ros/indigo/setup.bash
catkin_init_workspace
cd ~/catkin_ws
pip install catkin_pkg
catkin_make
