# Create package and Build

## 1. before start
```bash
# YOU SHOULD RUN THIS SCRIPT, IF YOU NOT
$ source /opt/ros/foxy/setup.bash
$ source /home/leoo/shared/ros2-sandbox/install/setup.bash
$ source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
```

## 2. create package
### 2.1. python
```bash
$ cd src
$ ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy
```

- `ament_python`
  - pure python packages and tells the build tools to use a setuptools workflow
- `rclpy`(ROS Client Library for Python)

### 2.2. c++
```
$ cd src
$ ros2 pkg create my_cpp_pkg --build-type ament_cmake --dependencies rclcpp
```

## 3. colcon build
```bash
$ colcon build # build every packages
$ colcon build --packages-select my_py_pkg
```

## 4. run compiled file
```bash
# e.g (pwd=ros2-sandbox)
$ ./install/my_py_pkg/lib/my_py_pkg/py_node
```
