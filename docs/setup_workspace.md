# setup workspace
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
