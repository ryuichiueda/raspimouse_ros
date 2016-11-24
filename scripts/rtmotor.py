#!/usr/bin/env python
import sys,math
import rospy
from raspimouse_ros.srv import PutMotorFreqs
from raspimouse_ros.srv import SwitchMotors
from raspimouse_ros.msg import MotorFreqs
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

def callback_motor_sw(message):
    enfile = '/dev/rtmotoren0'

    try: 
        with open(enfile,'w') as f:
            if message.on: print >> f, '1'
            else:          print >> f, '0'
    except:
        rospy.logerr("cannot write to " + enfile)
        return False

    return True

def callback_motor_raw(message):
    lfile = '/dev/rtmotor_raw_l0'
    rfile = '/dev/rtmotor_raw_r0'

    try:
        lf = open(lfile,'w')
        rf = open(rfile,'w')
        print >> lf, str(message.left)
        print >> rf, str(message.right)
    except:
        rospy.logerr("cannot write to rtmotor_raw_*")

    lf.close()
    rf.close()

def callback_cmd_vel(message):
    lfile = '/dev/rtmotor_raw_l0'
    rfile = '/dev/rtmotor_raw_r0'

    #for forwarding
    forward_hz = 80000.0*message.linear.x/(9*math.pi)
    #for rotation
    rot_hz = 400.0*message.angular.z/math.pi
    try:
        lf = open(lfile,'w')
        rf = open(rfile,'w')
        lf.write(str(int(round(forward_hz - rot_hz))) + '\n')
        rf.write(str(int(round(forward_hz + rot_hz))) + '\n')
    except:
        rospy.logerr("cannot write to rtmotor_raw_*")

    lf.close()
    rf.close()

def callback_put_freqs(message):
    devfile = '/dev/rtmotor0'

    try:
        with open(devfile,'w') as f:
            print >> f, "%s %s %s" % (message.left, message.right, message.duration)
    except:
        rospy.logerr("cannot write to " + devfile)
        return False

    return True
        
if __name__ == '__main__':
    rospy.init_node('rtmotor')
    sub = rospy.Subscriber('motor_raw', MotorFreqs, callback_motor_raw)
    sub = rospy.Subscriber('cmd_vel', Twist, callback_cmd_vel)
    srv = rospy.Service('switch_motors', SwitchMotors, callback_motor_sw)
    srv = rospy.Service('put_motor_freqs', PutMotorFreqs, callback_put_freqs)
    rospy.spin()
