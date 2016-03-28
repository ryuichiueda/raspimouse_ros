#!/usr/bin/env python
import sys
import rospy
from raspimouse_ros.msg import LeftRightFreq
from std_msgs.msg import Bool

def callback_motor_sw(message):
    enfile = '/tmp/rtmotoren0'
    with open(enfile,'w') as f:
        if message.data: print >> f, '1'
        else:            print >> f, '0'

def callback_motor_raw(message):
    lfile = '/tmp/rtmotor_raw_l0'
    rfile = '/tmp/rtmotor_raw_r0'

    try:
        lf = open(lfile,'w')
        rf = open(rfile,'w')
        print >> lf, message.left
        print >> rf, message.right
    except:
        print >> sys.stderr, "cannot write to rtmotor_raw_*" 
        sys.exit(1)
    else:
        lf.close()
        rf.close()
        
def listner():
    rospy.init_node('rtmotor')
    sub = rospy.Subscriber('motor_raw', LeftRightFreq, callback_motor_raw)
    sub = rospy.Subscriber('motor_sw', Bool, callback_motor_sw)
    rospy.spin()

if __name__ == '__main__':
    try:
        listner()

    except rospy.ROSInterruptException:
        pass
