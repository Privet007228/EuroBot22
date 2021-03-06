#!/usr/bin/env python
import rospy
import serial
from std_msgs.msg import Float64
try:
    ser = serial.Serial('/dev/ttyACM0')
except:
    try:
        ser = serial.Serial('/dev/ttyACM1')
    except:
        ser = serial.Serial('/dev/ttyACM2')


rospy.init_node('navx')

pub_yaw = rospy.Publisher('yaw', Float64, queue_size=10)
while not rospy.is_shutdown():
    try:
        yaw = float(ser.readline()[2:9])
        pub_yaw.publish(yaw)
    except:
        print('Error')
