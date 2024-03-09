#!/usr/bin/env python

## Simple hello world demo that publishes a message to
## the 'broadcaster' topic

import rospy
from std_msgs.msg import String

topic='broadcast'
message='Hello from AWS'

def broadcast():
    """
    creates a publisher for a given topic, publishes a message at a specified rate,
    and runs indefinitely until shutdown is detected.

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
