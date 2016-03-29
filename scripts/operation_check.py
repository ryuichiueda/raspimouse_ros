#!/usr/bin/env python

import sys, time
import rospy
from raspimouse_ros.srv import *
from raspimouse_ros.msg import *

def switch_motors(onoff):
    rospy.wait_for_service('/raspimouse/switch_motors')
    try:
        p = rospy.ServiceProxy('/raspimouse/switch_motors', SwitchMotors)
        res = p(onoff)
        return res.accepted
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
    else:
        False

def raw_control(left_hz,right_hz):
    pub = rospy.Publisher('/raspimouse/motor_raw', LeftRightFreq, queue_size=10)
    rospy.init_node('operation_checker', anonymous=True)

    if not rospy.is_shutdown():
        d = LeftRightFreq()
        d.left = left_hz
        d.right = right_hz
        pub.publish(d)
        print d

if __name__ == "__main__":
    if not switch_motors(True):
        print "[check failed]: motors are not empowered"

    raw_control(300,-300)
    time.sleep(0.5)
    raw_control(0,0)
    time.sleep(0.5)
    raw_control(-300,300)
    time.sleep(0.5)
    raw_control(0,0)

    if not switch_motors(False):
        print "[check failed]: motors are not turned off"

        #except rospy.ROSInterruptException:
        #    pass
        #else:
        #    print >> sys.stderr, "error"
