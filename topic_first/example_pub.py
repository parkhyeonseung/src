#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def fun():
    pass

if __name__=='__main__':
    rospy.init_node('sample_pub')
    pub = rospy.Publisher('hello',String,queue_size=10)
    # sub = rospy.Subscriber()
    rate = rospy.Rate(10)

    while True :
        str = 'hello_pub : %s' % rospy.get_time()
        # rospy.loginfo(str)
        pub.publish(str)
        rate.sleep()
    pass