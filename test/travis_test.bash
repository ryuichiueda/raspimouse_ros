#!/bin/bash -xve

roslaunch raspimouse_ros raspimouse.launch &
sleep 20

#publishing
rostopic pub -1 /raspimouse/buzzer std_msgs/UInt16 -- 10
rostopic pub -1 /raspimouse/motor_raw raspimouse_ros/LeftRightFreq '123' '456'

#service call
rosservice call /raspimouse/put_motor_freqs 'left: -300
right: 200
duration: 1000'

#listening test
rostopic echo /raspimouse/lightsensors -n 1 |
diff - ./test/lightsensors_output


#output file test
echo 10 | diff - /dev/rtbuzzer0
echo -300 200 1000 | diff - /dev/rtmotor0
echo 123 | diff - /dev/rtmotor_raw_l0
echo 457 | diff - /dev/rtmotor_raw_r0
