#!/usr/bin/env python
import sys
import rospy
from raspimouse_ros.msg import Switches

devfile = '/dev/rtswitch'

rospy.init_node('rtswitches')
pub = rospy.Publisher('switches', Switches, queue_size=10)
rate = rospy.Rate(10)

d = Switches()

d.state = 'neutral'
state_change_counter = 0

while not rospy.is_shutdown():
    try:
        with open(devfile + '0','r') as f:
            d.front = True if '0' in f.readline() else False
        with open(devfile + '1','r') as f:
            d.center = True if '0' in f.readline() else False
        with open(devfile + '2','r') as f:
            d.rear = True if '0' in f.readline() else False
    except:
        rospy.logerr("cannot open " + devfile + "[0,1,2]")

    if d.front: state_change_counter += 1

    if state_change_counter >= 5 and not d.front:
        state_change_counter = 0
        if d.state == 'neutral': d.state = 'ready' 
        elif d.state == 'ready': d.state = 'run' 
        else:                    d.state = 'neutral'

    pub.publish(d)
    rate.sleep()

