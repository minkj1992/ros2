# Ros2 CLI

```bash
$ ros2 node list
$ ros2 node info

```

- rename a node in runtime
```bash
$ ros2 run my_py_pkg py_node --ros-args --remap __node:=new_name_py_node
```

- topic

```bash
$ ros2 topic echo /robot_news
```