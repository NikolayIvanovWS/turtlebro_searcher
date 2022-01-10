#!/usr/bin/env python3

from turtlebro_patrol.srv import PatrolPointCallback, PatrolPointCallbackRequest, PatrolPointCallbackResponse 
from turtlebro_searcher.srv import ArucoDetect, ArucoDetectResponse, ArucoDetectRequest
from std_msgs.msg import String
import rospy

pub = rospy.Publisher('aruco_marker', String, queue_size=10)


def handle_request(req:PatrolPointCallbackRequest):

    aruco_result = aruco_detect.call(ArucoDetectRequest())
    
    if aruco_result.id > 0:
        pub.publish("I am detecting a marker:"  + " " + str(aruco_result.id))
    else : 
        pub.publish("Marker not detected")    

    return PatrolPointCallbackResponse(1, "Search end")


rospy.init_node('searcher_point_service')
s = rospy.Service('turtlebro_searcher', PatrolPointCallback, handle_request)
aruco_detect = rospy.ServiceProxy('aruco_detect', ArucoDetect)
rospy.spin()
