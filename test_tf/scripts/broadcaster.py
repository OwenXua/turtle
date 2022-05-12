#!/usr/bin/env python3
import rospy
import tf
from turtlesim.msg import Pose

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")

if __name__ == "__main__":
    rospy.init_node("turtle_tf_broadcaster")
    turtlename = rospy.get_param("~turtle")
    rospy.Subscriber(turtlename + "/pose",
                     Pose,
                     handle_turtle_pose,
                     turtlename)
    rospy.spin()
