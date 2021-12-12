# Ros2

## Terminology
- Data Distribution Service (DDS)
- Real-Time Publish Subscribe (RTPS)
- The Object Management Group (OMG)
- OMG Interface Description Language (IDL)
- Quality of Service (QoS)

## ros2 vs ros1
- rtos
  - Real Time OS (time critical os)
- multi node in single process


## DDS

DDS는 데이터를 여러곳에 전송하기 위한 서비스로, OMG 표준 pub/sub 네트워크 미들웨어입니다. real-time, scalable.

- UDP/TCP 기반에서 동작
- p2p 통신 방식으로 master 부재
- DDS 데이터 버스
- Ros2는 default middleware로 dds를 사용.


## QoS
QoS는 네트워크 상에 흐르는 데이터의 중요도를 분류하여, 이를 기반으로 우선순위를 부여하는 능력을 뜻합니다.

ROS에서의 QoS는 "The right data at the right time at the right place"를 구현하기 위해 사용되는 기술이다.





## Package
> with Turtlesim

## Node and Message
> https://docs.ros.org/en/foxy/Tutorials/Understanding-ROS2-Nodes.html



## Topic
> https://docs.ros.org/en/foxy/Tutorials/Topics/Understanding-ROS2-Topics.html


- act as a bus for nodes to exchange message
- pub/sub model


## Service

- based on a call(request)-and-response model (diff with topic)
![](https://docs.ros.org/en/foxy/_images/Service-MultipleServiceClient.gif)

- service type
  - request message type -> response message type

## Action
```
__13.2. 액션 서버 및 클라이언트
__13.3. 노드 정보(ros2 node info)
__13.4. 액션 목록(ros2 action list -t)
__13.5. 액션 정보(ros2 action info)
__13.6. 액션 목표(action goal) 전달
```

## Interface
```
__14.2. 메시지 인터페이스(Message interface, msg)
__14.3. 서비스 인터페이스(Service interface, srv)
__14.4. 액션 인터페이스(Action interface, action)
```

## Parameter
```
__16.2. 파라미터 목록 확인(ros2 param list)
__16.3. 파라미터 내용 확인(ros2 param describe)
__16.4. 파라미터 읽기(ros2 param get)
__16.5. 파라미터 쓰기(ros2 param set)
__16.6. 파라미터 저장(ros2 param dump)
__16.7. 파라미터 삭제(ros2 param delete)
```

## RQt

## 표준단위, 좌표표현, 시간
## File system
## Build
## Launch system
## Logging
## Intra-process communication
## Component
```
__5.1. 정적 링킹과 동적 링킹
__5.2. 동적 로딩과 ROS 2 Component
```

## Lifecycle
## Security
## Real-time
