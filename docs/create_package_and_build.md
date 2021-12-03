# Create package and Build
<!-- TOC -->autoauto- [1. before start](#1-before-start)auto- [2. build](#2-build)auto    - [2.1. python package](#21-python-package)auto    - [2.2. c++ package](#22-c-package)auto- [3. colcon build](#3-colcon-build)autoauto<!-- /TOC -->

## 1. before start
```bash
# YOU SHOULD RUN THIS SCRIPT, IF YOU NOT
$ source /opt/ros/foxy/setup.bash
$ source /home/leoo/shared/ros2-sandbox/install/setup.bash
$ source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
```

## 2. build
### 2.1. python package
```bash
$ cd src
$ ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy
```

- `ament_python`
  - pure python packages and tells the build tools to use a setuptools workflow
- `rclpy`(ROS Client Library for Python)

### 2.2. c++ package
```
$ cd src
$ ros2 pkg create my_cpp_pkg --build-type ament_cmake --dependencies rclcpp
```

## 3. colcon build
```bash
$ colcon build # build every packages
$ colcon build --packages-select my_py_pkg
```
