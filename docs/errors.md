# Errors
> Lists up the errors that have been encountered.


## VirtualBox 공유폴더 권한 오류

```bash
# on virtualbox
$ sudo adduser $USER vboxsf
```

## VirtualBox가 너무 느리다.
- 디스플레이, cpu 적지 않게 할당했는데도, vm이 조금 느리다.(눈에 보일정도의 반응속도) mount가 원인이려나.
- 아직 미해결

## colcon build symlink error

```bash
$ colcon build --packages-select my_py_pkg --symlink-install
[Errno 1] Operation not permitted: '/home/leoo/shared/ros2-sandbox/src/my_py_pkg/setup.py' -> '/home/leoo/shared/ros2-sandbox/build/my_py_pkg/setup.py'
```

- virtualbox 때문에 문제가 되는 것 같은데, 아직 미해결
