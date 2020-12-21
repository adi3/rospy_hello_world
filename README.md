# rospy_hello_world
Simple ROS project in python with snapcraft config

## Setup

1. Download this repository to your catkin workspace

  ```
  cd ~/catkin_ws
  git clone https://github.com/adi3/rospy_hello_world
  ```
  
2. Mark python node as executable

  ```
  chmod +x src/hello_world/nodes/broadcast.py
  ```

## Test run

1. Build project

  ```
  catkin_make
  source devel/setup.bash
  ```
  
2. Execute with rosrun

  ```
  roscore
  rosrun hello_world broadcast.py
  ```
  Node should start printing messages to terminal @ 10Hz
  
3. Execute with roslaunch
  
  ```
  roslaunch hello_world broadcast.launch
  ```
  Node should start printing messages to terminal @ 10Hz

..to snap..
sudo apt update
sudo apt remove lxd-client -y
sudo snap install lxd
lxd init --auto
snap install snapcraft --classic
cd ~/catkin_ws
snapcraft --use-lxd

..after snapping...
- sudo snap install --devmode <snap_name>
