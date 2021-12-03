# ROS2 Foxy
> https://www.udemy.com/course/ros2-for-beginners


## setup os env
- [setup success (✅)](./docs/setup_success.md)
  - virtualbox + ubuntu 20.04 lts
- [setup failed (🚫)](./docs/setup_failed.md)
  1. docker
  2. host (mac)

## setup code env
```bash
# ros2-sandbox on vmware
$ colcon build
$ echo 'source /home/leoo/shared/ros2-sandbox/install/setup.bash' >> ~/.bashrc
```
- sudo ros2를 하니 command not found가 나왔다. 만약 sudo를 써야 한다면,

```bash
$ sudo echo 'source /opt/ros/foxy/setup.bash' >> /root/.bashrc && sudo reboot
```

- host디렉토리를 mount 해버리니, .bashrc에서 commad가 permission denied되었다. 그러므로 매번 vmware에서는 sudo -i를 해주고, /root 디렉토리에 symlink를 생성해주자(편리함)s

```bash
$ sudo -i
# 생성하지 않았다면 
$ ln -s /home/leoo/shared/ros2-sandbox ros2-sandbox
$ cd ros2-sandbox
```

## python package
### before
```bash
# YOU SHOULD RUN THIS SCRIPT, IF YOU NOT
$ source /opt/ros/foxy/setup.bash
$ source /home/leoo/shared/ros2-sandbox/install/setup.bash
$ source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
```

### create python package ros2
```bash
$ cd src
$ ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy
```

- `ament_python`
  - pure python packages and tells the build tools to use a setuptools workflow
- `rclpy`(ROS Client Library for Python)

### build
```bash
$ colcon build # build every packages
$ colcon build --packages-select my_py_pkg
```


