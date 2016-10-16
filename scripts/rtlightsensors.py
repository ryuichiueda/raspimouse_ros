#!/usr/bin/env python
import sys, rospy
from raspimouse_ros.msg import LightSensorValues

if __name__ == '__main__':
    #freq = 10
    #if rospy.has_param('lightsensors_freq'):
    freq = rospy.get_param('lightsensors_freq',10)
        
    devfile = '/dev/rtlightsensor0'
    rospy.init_node('rtlightsensors')
    pub = rospy.Publisher('lightsensors', LightSensorValues, queue_size=1)
    rate = rospy.Rate(freq)

    while not rospy.is_shutdown():
        try:
            with open(devfile,'r') as f:
                data = f.readline().split()
                d = LightSensorValues()
                d.right_forward = int(data[0])
                d.right_side = int(data[1])
                d.left_side = int(data[2])
                d.left_forward = int(data[3])
                pub.publish(d)
        except:
            rospy.logerr("cannot open " + devfile)

        rate.sleep()

