#!/usr/bin/env python
import sys
import rospy
from raspimouse_ros.msg import Switches

def talker():
    devfile = '/dev/rtswitch'

    rospy.init_node('rtswitches')
    pub = rospy.Publisher('switches', Switches, queue_size=10)
    rate = rospy.Rate(10)

    d = Switches()
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

        pub.publish(d)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()

    except rospy.ROSInterruptException:
        pass
