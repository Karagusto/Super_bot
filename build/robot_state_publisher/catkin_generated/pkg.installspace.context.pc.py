# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include;/opt/ros/kinetic/share/orocos_kdl/../../include;/usr/include/eigen3;/usr/include".split(';') if "${prefix}/include;/opt/ros/kinetic/share/orocos_kdl/../../include;/usr/include/eigen3;/usr/include" != "" else []
PROJECT_CATKIN_DEPENDS = "kdl_parser;roscpp;rosconsole;rostime;sensor_msgs;tf2_ros;tf2_kdl".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lrobot_state_publisher_solver;-ljoint_state_listener;/opt/ros/kinetic/lib/liborocos-kdl.so.1.3.2".split(';') if "-lrobot_state_publisher_solver;-ljoint_state_listener;/opt/ros/kinetic/lib/liborocos-kdl.so.1.3.2" != "" else []
PROJECT_NAME = "robot_state_publisher"
PROJECT_SPACE_DIR = "/home/ricardfragoso/catkin_ws/install"
PROJECT_VERSION = "1.15.1"
