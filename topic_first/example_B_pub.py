#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

if __name__=='__main__':
    rospy.init_node('pub_B1')
    pub = rospy.Publisher('pub_B1',String,queue_size=10)
    rate = rospy.Rate(10)

    while True :
        str = 'im pub_b1'
        pub.publish(str)
        rate.sleep()
    pass