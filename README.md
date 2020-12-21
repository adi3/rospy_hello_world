# rospy_hello_world
Simple ROS project in python with snapcraft config

..set up...
- download this to ~/catkin_ws
- chmod +x src/hello_world/nodes/talker.py

..to test..
- catkin_make
- source devel/setup.bash
- roscore
- rosrun hello_world talker.py

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
