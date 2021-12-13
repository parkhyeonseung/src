#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def fun_callback(msg):
    rospy.loginfo('%s',msg.data)
    pass

if __name__=='__main__':
    rospy.init_node('A1')
    rospy.Subscriber('A1',String,callback=fun_callback)
    rospy.spin()
    pass