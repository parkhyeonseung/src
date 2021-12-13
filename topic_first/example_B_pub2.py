#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

if __name__=='__main__':
    i=0
    rospy.init_node('pub_B2')
    pub = rospy.Publisher('pub_B2',String,queue_size=10)
    rate = rospy.Rate(10)

    while True :
        strb = 'im pub_b2 '
        pub.publish(strb+str(i))
        rate.sleep()
        i+=1
    pass