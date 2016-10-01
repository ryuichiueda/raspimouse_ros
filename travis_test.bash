#!/bin/bash -xve

roslaunch raspimouse_ros raspimouse.launch &

sleep 20

rosrun raspimouse_ros check_driver_io.py
