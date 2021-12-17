#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import time
import cv2
from std_srvs.srv import Empty
import numpy as np

def go(x,dis):
    put = True
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    msg = Twist()
    msg.linear.x=msg.linear.y=msg.linear.z=0.0
    msg.angular.x=msg.angular.y=msg.angular.z=0.0

    # distance = 5.44445
    distance = dis
    curr_dis = 0
    speed = 3
    time0=0
    time1=0
    
    if dis >0:
        while put:
            if x == 'x':
                msg.linear.x = distance-curr_dis
            else:
                msg.linear.y = distance-curr_dis
            time0 = time.time()
            pub.publish(msg)
            time1=time.time()
            curr_dis += speed*(time1-time0)
            if -0.01 <=distance-curr_dis <=0.01:
                break
    else:
        while put:
            if x == 'x':
                msg.linear.x = distance-curr_dis
            else:
                msg.linear.y = distance-curr_dis
            time0 = time.time()
            pub.publish(msg)
            time1=time.time()
            curr_dis -= speed*(time1-time0)
            if -0.01 <=distance-curr_dis <=0.01:
                break

def stop():
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    msg = Twist()
    msg.linear.x=msg.linear.y=msg.linear.z=0.0
    msg.angular.x=msg.angular.y=msg.angular.z=0.0
    pub.publish(msg)

# def go1(x,y):
#     pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
#     msg = Twist()
#     msg.linear.x=msg.linear.y=msg.linear.z=0.0
#     msg.angular.x=msg.angular.y=msg.angular.z=0.0
#     while True:
#         if x ==1:
#             msg.linear.x = 2.
#         elif x==0:
#             msg.linear.x= -2.
#         else :
#             msg.linear.x = 0.
#         if y==1:
#             msg.linear.y = 2.
#         elif y==0 :
#             msg.linear.y = -2.
#         else :
#             msg.linear.y = 0.
#         pub.publish(msg)
#         msg.linear.x=msg.linear.y=msg.linear.z=0.0

def turn(c):
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    msg = Twist()
    msg.linear.x=msg.linear.y=msg.linear.z=0.0
    msg.angular.x=msg.angular.y=msg.angular.z=0.0
    if c ==0:
        msg.angular.z = np.pi/2.
    else:
        msg.angular.z = -np.pi/2.
    pub.publish(msg)

if __name__=='__main__':
    rospy.init_node('simturtle_publisher')
    rospy.wait_for_service('/reset')
    reset_world = rospy.ServiceProxy('/reset', Empty)
    cv2.namedWindow('a')
    axis_x = 'x'
    axis_y = 'y'
    val = 5.44
    while True:
        key=cv2.waitKey(1)
        if key == ord('w'): 
            stop()
            go(axis_x,val)
            key = 0

        if key == ord('s'):
            stop()
            go(axis_x,-val)
            key = 0

        if key == ord('d'):
            stop()
            go(axis_y,val)

        if key == ord('a'):
            stop()
            go(axis_y,-val)

        if key == ord('z'):
            break

        if key == ord(' '):
            reset_world()
        
        if key == ord('q'):
            stop()
            turn(0)

        if key == ord('e'):
            stop()
            turn(1)

