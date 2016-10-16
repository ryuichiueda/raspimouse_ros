#!/usr/bin/env python
import rospy
import actionlib
from std_msgs.msg import UInt16
from raspimouse_ros.msg import MusicAction, MusicResult, MusicFeedback

def put_freq(hz):
    try:
        with open('/dev/rtbuzzer0','w') as f:
            print >> f, hz 
    except:
        rospy.logerr("cannot open " + devfile)

def cb(message):
    put_freq(message.data)

def exec_music(goal):
    r = MusicResult()
    fb = MusicFeedback()
    r.finished = True
    num = len(goal.freqs)
    for i, f in enumerate(goal.freqs):
        fb.remaining_steps = num - i
        ms.publish_feedback(fb)

        if ms.is_preempt_requested():
            put_freq(0)
            r.finished = False
            ms.set_preempted(r)
            return

        put_freq(f)
        t = 1.0
        if i < len(goal.durations):
            t = goal.durations[i]

        rospy.sleep(t)

    fb.remaining_steps = 0
    ms.publish_feedback(fb)
    ms.set_succeeded(r)
    return

def mute():
    put_freq(0)

if __name__ == '__main__':
    rospy.init_node('rtbuzzer')
    sub = rospy.Subscriber('buzzer', UInt16, cb)
    ms = actionlib.SimpleActionServer('music', MusicAction, exec_music, False)
    ms.start()
    rospy.on_shutdown(mute)
    rospy.spin()
