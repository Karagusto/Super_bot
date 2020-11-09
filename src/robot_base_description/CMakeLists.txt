cmake_minimum_required(VERSION 3.0.2)
project(robot_base_description)


## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  robot_state_publisher
)


###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(  
  ${catkin_INCLUDE_DIRS}
)

