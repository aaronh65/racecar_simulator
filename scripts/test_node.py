#!/usr/bin/env python
import rospy
from ackermann_msgs.msg import AckermannDriveStamped
from sensor_msgs.msg import LaserScan

def scanCallback(msg):
    if min(msg.ranges) > 1.0:
        ack_msg = AckermannDriveStamped()
        ack_msg.header.stamp = rospy.Time.now()
        ack_msg.header.frame_id = 'publish_drive_test'
        ack_msg.drive.steering_angle = 0.0
        ack_msg.drive.speed = 1.0
        ack_publisher.publish(ack_msg)
    else:
        ack_msg = AckermannDriveStamped()
        ack_msg.header.stamp = rospy.Time.now()
        ack_msg.header.frame_id = 'publish_drive_test'
        ack_msg.drive.steering_angle = 0.0
        ack_msg.drive.speed = 0.0
        ack_publisher.publish(ack_msg)


if __name__ == '__main__':
    rospy.init_node('test_node')
    rospy.Subscriber('scan', LaserScan, scanCallback)
    ack_publisher = rospy.Publisher('/drive', AckermannDriveStamped, queue_size=1)
    while not rospy.is_shutdown():
        rospy.spin()
