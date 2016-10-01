#!/bin/bash -xve

#add dummy files
echo 1 2 3 4 | sudo tee /dev/rtlightsensor0
echo 1 | sudo tee /dev/rtswitch{0,1,2}
sudo touch /dev/rtmotor0 /dev/rtmotoren0 /dev/rtmotor_raw_{l,r}0 /dev/rtbuzzer0
sudo chmod 666 /dev/rtmotor0 /dev/rtmotoren0 /dev/rtmotor_raw_{l,r}0 /dev/rtbuzzer0

#required packages
pip install catkin_pkg
pip install empy
pip install pyyaml
pip install rospkg

#ros install
git clone https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu14.04_server.git
cd ./ros_setup_scripts_Ubuntu14.04_server
bash ./step0.bash
bash ./step1.bash

#catkin setup
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
source /opt/ros/indigo/setup.bash
catkin_init_workspace
cd ~/catkin_ws
catkin_make

#download own package
cd ~/catkin_ws/src/
#rsync -av $HOME/raspimouse_ros ~/catkin_ws/src/raspimouse_ros/
rsync -av /home/travis/build/*/raspimouse_ros ~/catkin_ws/src/raspimouse_ros/
cd ~/catkin_ws
catkin_make
