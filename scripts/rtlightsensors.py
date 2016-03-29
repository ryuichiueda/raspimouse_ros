#!/usr/bin/env python
import sys
import rospy
from raspimouse_ros.msg import LightSensorValues

def talker():
    devfile = '/dev/rtlightsensor0'


    rospy.init_node('lightsensors')
    pub = rospy.Publisher('lightsensors', LightSensorValues, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        with open(devfile,'r') as f:
            data = f.readline().split()
            d = LightSensorValues()
            d.right_forward = int(data[0])
            d.right_side = int(data[1])
            d.left_side = int(data[2])
            d.left_forward = int(data[3])
            pub.publish(d)
            rate.sleep()


if __name__ == '__main__':
    try:
        talker()

    except rospy.ROSInterruptException:
        pass
