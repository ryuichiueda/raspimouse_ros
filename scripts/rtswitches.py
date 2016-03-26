#!/usr/bin/env python
import sys
import rospy
from raspimouse_ros.msg import Switches

def talker():
    devfile = '/tmp/rtswitch'

    rospy.init_node('switches')
    pub = rospy.Publisher('switches', Switches, queue_size=10)
    rate = rospy.Rate(10)

    d = Switches()
    while not rospy.is_shutdown():
        with open(devfile + '0','r') as f:
            d.front = True if '1' in f.readline() else False
        with open(devfile + '1','r') as f:
            d.center = True if '1' in f.readline() else False
        with open(devfile + '2','r') as f:
            d.rear = True if '1' in f.readline() else False

        pub.publish(d)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()

    except rospy.ROSInterruptException:
        pass
