cmake_minimum_required(VERSION 3.5)
project(maison_connectee)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

install(
  DIRECTORY maison_connectee
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
