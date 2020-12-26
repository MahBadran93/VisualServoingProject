#!/usr/bin/env python
import rospy
import sys
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from move_robot import MoveRobot


class LineFollower(object):

    def __init__(self):
    
        self.bridge_object = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.camera_callback)
        self.moveRobot_object = MoveRobot()

    def camera_callback(self,data):
        
        try:
            # We select bgr8 because its the OpneCV encoding by default
            cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
            cv2.imshow("Original", cv_image)
            cv2.waitKey(1)
        except CvBridgeError as e:
            print(e)
        # crop the image     
        height, width, channels = cv_image.shape
        descentre = 160
        rows_to_watch = 20
        crop_img = cv_image[(height)/2+descentre:(height)/2+(descentre+rows_to_watch)][1:width]

        # Convert  RGB to HSV
        hsv = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)

        """
        Use ColorZilla to get the color registered by the camera
        """
        lower_yellow = np.array([20,100,100])
        upper_yellow = np.array([41,255,255])

        # Threshold the HSV image to get only needed colors
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        
        # Calculate centroid using ImageMoments
        m = cv2.moments(mask, False)
        try:
            cx, cy = m['m10']/m['m00'], m['m01']/m['m00']
        except ZeroDivisionError:
            cy, cx = height/2, width/2
        
        
        # (Bitwise AND operation) on mask and original image
        res = cv2.bitwise_and(crop_img,crop_img, mask= mask)
        
       #Visualization
        cv2.circle(res,(int(cx), int(cy)), 10,(0,0,255),-1)

        cv2.imshow("Original image", cv_image)
        cv2.imshow("HSV image ", hsv)
        cv2.imshow("Mask image", mask)
        cv2.imshow("BitwiseAnd", res)
        
        cv2.waitKey(1)
        
        
        error_x = cx - width / 2
        twist_object = Twist()
        twist_object.linear.x = 0.2
        twist_object.angular.z = -error_x / 100
        rospy.loginfo("ANGULAR VALUE SENT===>"+str(twist_object.angular.z))

        # turn 
        self.moveRobot_object.move_robot(twist_object)
        
    def clean_up(self):
        self.moveRobot_object.clean_class()
        cv2.destroyAllWindows()
        
        

def main():
    rospy.init_node('line_following_node', anonymous=True)
    rospy.loginfo("start following...")
    
    line_follower_object = LineFollower()
   
    rate = rospy.Rate(5)
    ctrl_c = False
    def shutdownhook():
        # works better than the rospy.is_shut_down()
        line_follower_object.clean_up()
        rospy.loginfo("shutdown time!")
        ctrl_c = True
    
    rospy.on_shutdown(shutdownhook)
    
    while not ctrl_c:
        rate.sleep()

    
    
if __name__ == '__main__':
    main()