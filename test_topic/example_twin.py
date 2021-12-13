#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from threading import Thread

def callback(msg):
    rospy.loginfo('%s',msg.data)

def publish():
    pub = rospy.Publisher('twin',String,queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        str = 'hello twin : %s ' % rospy.get_time()
        pub.publish(str)
        rate.sleep()
        rospy.Subscriber('twin',String,callback=callback)
        rospy.spin()
def subscrib():
    rospy.Subscriber('twin',String,callback=callback)
    rospy.spin()


if __name__=='__main__':
    rospy.init_node('sample_node')
    # pub = Thread(target=publish,args=())
    # sub = Thread(target=subscrib,args=())
    # pub.start()
    # sub.start()
    # pub.join()
    # sub.join()
    
    

