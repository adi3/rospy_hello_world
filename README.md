# ROS Hello World
Simple ROS project in python with associated snapcraft config

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
  Node will start printing messages to the terminal @ 10Hz
  
3. Execute with roslaunch
  
  ```
  roslaunch hello_world broadcast.launch
  ```
  Node will start printing messages to the terminal @ 10Hz

## Build snap

1. Install tools
  ```
  sudo apt update
  sudo apt remove lxd-client -y
  sudo snap install lxd
  lxd init --auto
  snap install snapcraft --classic
  ```
  
2. Initate snapping
  ```
  cd ~/catkin_ws
  snapcraft --use-lxd
  ```

## Run snap

1. Find snap name
  ```
    ls *snap
  ```

2. Install snap
  ```
  sudo snap install --devmode <snap_name>
  ```

3. Execute snap
  ```
  <snap_name>.launch
  ```
  Node will start printing messages to the terminal @ 10Hz
