#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def update_pose(self, data):
    pose = data
    pose.x = round(pose.x, 4)
    pose.y = round(pose.y, 4)

if __name__=='__main__':
    rospy.init_node('pub_B1')
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose, update_pose)
    msg = Twist()
    rate = rospy.Rate(10)
