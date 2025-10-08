cmake_minimum_required(VERSION 3.8)
project(bal_ca0_proba)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

set(ament_dependencies
  rclpy
  std_msgs
  geometry_msgs
)

 add_executable(trig_wave_publisher/src/trig_publisher.py)
 ament_target_dependencies(trig_wave_publisher rclpy std_msgs)

add_executable(trig_wave_subscriber/src/trig_subscriber.py)
 ament_target_dependencies(trig_wave_subscriber rclpy std_msgs)

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME})

install(TARGETS

trig_wave_publisher
trig_wave_subscriber

DESTINATION lib/${PROJECT_NAME})

ament_package()