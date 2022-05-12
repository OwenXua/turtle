#include <ros/ros.h>
#include <tf/transform_broadcaster.h>

int main(int argc, char **argv)
{
    ros::init(argc, argv, "new_frame");
    ros::NodeHandle nh;

    tf::TransformBroadcaster br;
    tf::Transform transform;

    ros::Rate rate(10);
    while (nh.ok()){
        transform.setOrigin(tf::Vector3(0, 2, 0));
        transform.setRotation(tf::Quaternion(0, 0, 0, 1));
        br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "turtle1", "carrot"));
        rate.sleep();
    }

    return 0;
}
