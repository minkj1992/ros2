# setup

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

5. install dep
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

## setup with docker (🚫)
> [refs](https://roomedia.tistory.com/entry/1%EC%9D%BC%EC%B0%A8-macOS-Catalina-10155%EC%97%90-ros2-foxy-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0)

- finally I install ros2 with docker. 
```bash
$ docker pull osrf/ros:noetic-desktop-full-buster
$ brew install socat

# https://www.cyberciti.biz/faq/apple-osx-mountain-lion-mavericks-install-xquartz-server/
$ brew install --cask xquartz
$ sudo reboot
# xquartz 보안 설정 모두 열어주기
```
- host 터미널에서 아래 명령어 실행

```bash
# ip 확인 후 xhost에 추가
$ ip=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
$ xhost + $ip

# 컨테이너 생성
$ docker run -it -e DISPLAY=$ip:0 --name ros osrf/ros:noetic-desktop-full-buster
```

- 하지만 추후 네트워크 통신이 많아지는 걸 고려하면 오히려 hypervisor를 쓰는게 더 현명해 보임
- 추가로 문서 또한 리눅스 문서들이 많으므로 vm ware 사용

## setup on Host (🚫)
> **This was failed**

### Pre-Install ROS2 on mac
```bash
$ brew doctor

$ softwareupdate --all --install --force
$ sudo rm -rf /Library/Developer/CommandLineTools
$ sudo xcode-select --install
$ brew link kubernetes-cli
$ brew link python@3.9
$ echo 'export PATH="/usr/local/sbin:$PATH"' >> ~/.zshrc
```

### Install ROS2 on mac

```bash
brew install python@3.8
brew unlink python && brew link --force python@3.8
echo 'export PATH="/usr/local/opt/python@3.8/bin:$PATH"' >> ~/.zshrc
export LDFLAGS="-L/usr/local/opt/python@3.8/lib"
export PKG_CONFIG_PATH="/usr/local/opt/python@3.8/lib/pkgconfig"

brew install asio tinyxml2 tinyxml eigen pcre poco
brew install openssl && echo "export OPENSSL_ROOT_DIR=$(brew --prefix openssl)" >> ~/.zshrc
brew install qt freetype assimp sip pyqt5
brew install console_bridge log4cxx spdlog cunit graphviz

python3 -m pip install pygraphviz pydot catkin_pkg empy ifcfg lark-parser lxml netifaces numpy pyparsing pyyaml setuptools argcomplete

pip3 install -U colcon-common-extensions

# OpenCV는 필수는 아닙니다. 설치시 시간이 엄청 오래 걸리니 고민해보세요.
brew install opencv
```

### Download ROS Foxy Binary
```bash
# https://github.com/ros2/ros2/releases

mkdir -p ~/ros2_foxy
cd ~/ros2_foxy
tar xf ~/Downloads/ros2-foxy-20211013-macos-amd64.tar.bz2
```

### Check installed
```bash
$ . ~/ros2_foxy/ros2-osx/local_setup.zsh
```

### Error
```
 $ . ~/ros2_foxy/ros2-osx/local_setup.zsh
[connext_cmake_module] Warning: The location at which Connext was found when the workspace was built [[/Applications/rti_connext_dds-5.3.1]] does not point to a valid directory, and the NDDSHOME environment variable has not been set. Support for Connext will not be available.
```

- `csrutil disable`로 시도해보았지만 실패
- ros2 바이너리 버전을 낮춰서 시도해보았지만 역시 실패
- big sur과 맞지 않는 source code에러가 있는 듯하다.

### refs 
- [공식](https://docs.ros.org/en/foxy/Installation/macOS-Install-Binary.html)
- [how-to-install-ros2-foxy-on-macos](https://snowdeer.github.io/ros2/2020/09/15/how-to-install-ros2-foxy-on-macos/)
- [building-ros2-on-macos-big-sur-m1](http://mamykin.com/posts/building-ros2-on-macos-big-sur-m1/)
