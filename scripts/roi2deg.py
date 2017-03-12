#!/usr/bin/env python

import rospy
from sensor_msgs.msg import RegionOfInterest
from std_msgs.msg import Int16

import numpy as np

class Roi2Deg(object):

    def __init__(self):
        rospy.init_node('roi2deg', anonymous=True)
        rospy.Subscriber("roi", RegionOfInterest, self.callback)
        image_height = rospy.get_param("/IMAGE_HEIGHT")
        image_width = rospy.get_param("/IMAGE_WIDTH")
        print "(width, height) = (%d, %d)" % (image_width, image_height)

        self.pub = rospy.Publisher("deg_control", Int16, queue_size=1)

    def callback(self, data):
        print "-----------------"
        rospy.loginfo(rospy.get_caller_id()+"\n")
        rospy.loginfo("x_offset :"+str(data.x_offset)+"\n")
        rospy.loginfo("y_offset :"+str(data.y_offset)+"\n")
        rospy.loginfo("height :"+str(data.height)+"\n")
        rospy.loginfo("width :"+str(data.width)+"\n")

        self.pub.publish(1 if np.random.randint(2) == 0 else -1)
    

if __name__=="__main__":
    r2d = Roi2Deg()
    rospy.spin()        
