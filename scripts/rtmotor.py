#!/usr/bin/env python
import sys
import rospy
from raspimouse_ros.srv import PutMotorFreqs
from raspimouse_ros.srv import SwitchMotor
from raspimouse_ros.msg import LeftRightFreq
from std_msgs.msg import Bool

def callback_motor_sw(message):
    enfile = '/tmp/rtmotoren0'

    try:
        with open(enfile,'w') as f:
            if message.on: print >> f, '1'
            else:          print >> f, '0'
    except:
        return False

    return True

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

def callback_put_freqs(message):
    devfile = '/tmp/rtmotor0'
    putstr = "%s %s %s" % (message.left, message.right, message.duration)
    print putstr
    with open(devfile,'w') as f:
        print >> f, putstr

    return True
        
def listner():
    rospy.init_node('rtmotor')
    sub = rospy.Subscriber('motor_raw', LeftRightFreq, callback_motor_raw)
    srv = rospy.Service('switch_motor', SwitchMotor, callback_motor_sw)
    srv = rospy.Service('put_motor_freqs', PutMotorFreqs, callback_put_freqs)
    rospy.spin()

if __name__ == '__main__':
    try:
        listner()

    except rospy.ROSInterruptException:
        pass
