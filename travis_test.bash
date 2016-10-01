#!/bin/bash -xve

cd ~/catkin_ws/src/
git clone https://github.com/ryuichiueda/raspimouse_ros.git
roslaunch raspimouse_ros travis_test.launch
