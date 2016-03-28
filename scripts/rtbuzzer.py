#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16

def callback(message):
    devfile = '/tmp/rtbuzzer0'
    #rospy.loginfo("Buzzer %d", message.data)
    with open(devfile,'w') as f:
        print >> f, message.data
        

def listner():
    rospy.init_node('buzzer')
    sub = rospy.Subscriber('buzzer', UInt16, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listner()

    except rospy.ROSInterruptException:
        pass
