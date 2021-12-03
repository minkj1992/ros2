# setup success
> macOS Big Sur (11.6.1, 16-inch, 2019, intel) + ROS2 Foxy

최종적으로 선택한 개발 환경은 다음과 같습니다.

- 실행환경: virtualbox(ubuntu 20.04)
- mount: 현재 디렉토리
- 코드작성: host (vscode)

## setup on virtual box (✅)
> [setup mac like keyboard on virtual box](https://bradwhittington.wordpress.com/2011/04/08/copy-paste-with-cmd-c-cmd-v-virtualbox-ubuntu-os/)
1. https://mirror.kakao.com/ubuntu-releases/focal/ 에서 ubuntu 20.04 lts download
2. vmware 셋업
   1. mem: 8192MB
   2. HDD: 30 GB
   3. 키보드 / 드래그앤 드롭 Bidirectional 설정
3. iso 연결
4. ubuntu install
   1. [virtual box cmd right로 변경](https://superuser.com/a/829588)
   2. [키보드 세팅(mac like)]
```bash
    $ sudo apt-get install keyboard-configuration
    $ sudo dpkg-reconfigure keyboard-configuration
    
    # select macbook pro(intel)
    # MacIntosh
    # English
    # English (Macintosh)
    # Both Alt keys
    # No compose key
    # Terminal preference에서 copy & paste 설정
```
   3. mount host folder(소스코드) to ubuntu

```bash
# 이건 임시이며, 항상 mount시키고 싶다면, vmware에 공유 폴더 설정해주어야 한다.
$ sudo mount -t vboxsf ros2-sandbox /home/leoo/shared/ros2-sandbox/
```

1. install dep
```bash
$ sudo apt update
$ sudo apt install build-essential gcc make perl dkms
$ sudo apt update && sudo apt upgrade
$ sudo apt install terminator
$ sudo add-apt-repository universe
$ sudo apt-get update
$ sudo apt-get install python3-pip
```

6. install ros2
```bash
$ locale  # check for UTF-8

$ sudo apt update && sudo apt install locales
$ sudo locale-gen en_US en_US.UTF-8
$ sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
$ export LANG=en_US.UTF-8
$ locale  # verify settings

$ sudo apt update && sudo apt install curl gnupg2 lsb-release
$ sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
$ echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

$ sudo apt update
$ sudo apt install ros-foxy-desktop
$ echo 'source /opt/ros/foxy/setup.bash' >> ~/.bashrc
$ sudo apt install python3-argcomplete
```

## Errors

### VirtualBox 공유폴더 권한 오류

```
# on virtualbox
$ sudo adduser $USER vboxsf
```

### VirtualBox가 너무 느리다.
디스플레이, cpu 적지 않게 할당했는데도, vm이 조금 느리다.(눈에 보일정도의 반응속도) mount가 원인이려나.