#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16

def callback(message):
    devfile = '/dev/rtbuzzer0'
    try:
        with open(devfile,'w') as f:
            print >> f, message.data
    except:
        rospy.logerr("cannot open " + devfile)
        

def listner():
    rospy.init_node('buzzer')
    sub = rospy.Subscriber('buzzer', UInt16, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listner()

    except rospy.ROSInterruptException:
        pass
