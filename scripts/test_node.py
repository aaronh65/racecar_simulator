#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose, PoseStamped
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

def goalCallback(msg):
    goal = msg
    origin = Pose()
    origin.position.x = 0.0
    origin.position.y = 0.0
    origin.position.z = 0.0
    pose_publisher.publish(origin)
    print('published to origin')


if __name__ == '__main__':
    rospy.init_node('test_node')
    rospy.Subscriber('scan', LaserScan, scanCallback)
    rospy.Subscriber('move_base_simple/goal', PoseStamped, goalCallback)
    ack_publisher = rospy.Publisher('/drive', AckermannDriveStamped, queue_size=1)
    pose_publisher = rospy.Publisher('/pose', Pose, queue_size=1)
    while not rospy.is_shutdown():
        rospy.spin()
