#!/bin/bash

rostopic pub -1 /music/goal raspimouse_ros/MusicActionGoal -- '{goal: {freqs: [ 349,392,440,466,523,587,622,698,784,0 ], durations: [0.6,0.3,0.3,0.2,0.2,0.2,0.2,0.2,3.0,1.0] }}' &

sleep 2
rostopic pub -1 /music/cancel actionlib_msgs/GoalID -- '{}'
