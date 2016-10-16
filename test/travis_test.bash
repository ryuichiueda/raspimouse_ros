#!/bin/bash -xve

roslaunch raspimouse_ros raspimouse.launch &
sleep 20

#publishing
rostopic pub -1 /buzzer std_msgs/UInt16 -- 10
rostopic pub -1 /motor_raw raspimouse_ros/MotorFreqs '123' '456'

#service call
rosservice call /put_motor_freqs 'left: -300
right: 200
duration: 1000'
rosservice call /switch_motors "'on': true"

#listening test
rostopic echo /lightsensors -n 1 > /tmp/test.lightsensors
rostopic echo /switches -n 1 > /tmp/test.switches

#output file test
diff /tmp/test.lightsensors ./test/lightsensors_output
diff /tmp/test.switches ./test/switches_output
echo 10 | diff - /dev/rtbuzzer0
echo -300 200 1000 | diff - /dev/rtmotor0
echo 123 | diff - /dev/rtmotor_raw_l0
echo 456 | diff - /dev/rtmotor_raw_r0
echo 1 | diff - /dev/rtmotoren0

#switch state transition test
echo 0 | sudo tee /dev/rtswitch0 && sleep 1
echo 1 | sudo tee /dev/rtswitch0 && sleep 1
rostopic echo /switches -n 1 | grep 'ready'

echo 0 | sudo tee /dev/rtswitch0 && sleep 1
echo 1 | sudo tee /dev/rtswitch0 && sleep 1
rostopic echo /switches -n 1 | grep 'run'

echo 0 | sudo tee /dev/rtswitch0 && sleep 1
echo 1 | sudo tee /dev/rtswitch0 && sleep 1
rostopic echo /switches -n 1 | grep 'neutral'
