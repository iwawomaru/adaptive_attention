#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty
import time

if __name__=="__main__":

    rospy.wait_for_service("/raspi_cam/camera/start_capture")
    try:
        rospy.ServiceProxy("/raspi_cam/camera/start_capture", Empty)()
        print "Sercice call success"
    except:
        print "Sercice call failed"
