#!/bin/bash -xve

roslaunch raspimouse_ros raspimouse.launch &
sleep 20

rostopic echo /raspimouse/lightsensors -n 1 |
diff - ./test/lightsensors_output
