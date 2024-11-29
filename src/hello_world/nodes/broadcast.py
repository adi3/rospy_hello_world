#!/usr/bin/env python

## Simple hello world demo that publishes a message to
## the 'broadcaster' topic

import rospy
from std_msgs.msg import String

topic='broadcast'
message='Hello from AWS'

def broadcast():
    """
    Publishes a message at a rate of 10 Hz to a specified topic until the ROS node
    is shut down. It uses a ROS publisher to send the message and a ROS rate to
    control the publishing frequency.

    """
    pub = rospy.Publisher(topic, String, queue_size=10)
    rospy.init_node('broadcast', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':
    try:
        broadcast()
    except rospy.ROSInterruptException:
        pass
