#!/usr/bin/env python

import sys, time
import rospy
from raspimouse_ros.srv import *
from raspimouse_ros.msg import *
from std_msgs.msg import UInt16

def switch_motors(onoff):
    rospy.wait_for_service('/raspimouse/switch_motors')
    try:
        p = rospy.ServiceProxy('/raspimouse/switch_motors', SwitchMotors)
        res = p(onoff)
        return res.accepted
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
    else:
        return False

def raw_control(left_hz,right_hz):
    pub = rospy.Publisher('/raspimouse/motor_raw', LeftRightFreq, queue_size=10)

    if not rospy.is_shutdown():
        d = LeftRightFreq()
        d.left = left_hz
        d.right = right_hz
        pub.publish(d)

def buzzer(hz):
    pub = rospy.Publisher('/raspimouse/buzzer', UInt16, queue_size=10)

    if not rospy.is_shutdown():
        pub.publish(hz)
        print "a"

def lightsensor_callback(data):
    print "lightsensors:", data.left_forward, data.left_side, data.right_side, data.right_forward

def switch_callback(data):
    print "switches:",data.front, data.center, data.rear

def sensors():
    subls = rospy.Subscriber('/raspimouse/lightsensors', LightSensorValues, lightsensor_callback)
    subsw = rospy.Subscriber('/raspimouse/switches', Switches, switch_callback)


def pos_control(left_hz,right_hz,time_ms):
    rospy.wait_for_service('/raspimouse/put_motor_freqs')
    try:
        p = rospy.ServiceProxy('/raspimouse/put_motor_freqs', PutMotorFreqs)
        res = p(left_hz,right_hz,time_ms)
        return res.accepted
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
    else:
        return False

if __name__ == "__main__":
    rospy.init_node('operation_checker', anonymous=True)

    ### buzzer test ###
    print >> sys.stderr, "test of the buzzer"
    buzzer(1000)
    time.sleep(2.0)
    buzzer(0)

    sys.exit(0)

    ### motor_raw test ###
    print >> sys.stderr, "test of raw control of the motors"
    if not switch_motors(True):
        print "[check failed]: motors are not empowered"

    raw_control(0,0)
    time.sleep(0.5)
    raw_control(-300,300)
    time.sleep(0.5)
    raw_control(0,0)
    time.sleep(0.5)
    raw_control(300,-300)
    time.sleep(0.5)
    raw_control(0,0)

    ### motor_pos test ###
    print >> sys.stderr, "test of position control of the motors"
    pos_control(300,300,1000)
    pos_control(-300,-300,1000)

    if not switch_motors(False):
        print "[check failed]: motors are not turned off"

    ### lightsensor test ###
    print >> sys.stderr, "test of sensors"
    sensors()
    time.sleep(10.0)


