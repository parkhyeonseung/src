#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from threading import Thread

def callback1(msg):
    global str1
    rospy.loginfo('%s' % msg.data)
    str1 = 'connect : %s ' % msg.data
    


def callback2(msg):
    global str2
    rospy.loginfo('%s' % msg.data)
    str2 = 'connect : %s ' % msg.data

def pub():
    pub1 = rospy.Publisher('A1',String,queue_size=10)
    pub2 = rospy.Publisher('A2',String,queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.Subscriber('pub_B1',String,callback=callback1)
        rospy.Subscriber('pub_B2',String,callback=callback2)
        pub1.publish(str1)
        pub2.publish(str2)
        rate.sleep()
        

if __name__=='__main__':
    str1 = ''
    str2 = ''
    rospy.init_node('CONNECT')
    pub()