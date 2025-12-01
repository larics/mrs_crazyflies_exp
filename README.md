## MRS-Crazyflies-exp
This ROS2 package contains adapted configuration files and launch files from [CrazySwarm2](https://github.com/IMRCLab/crazyswarm2), that should be used in the 2nd part of the MRS Project for the experimental part.

## Installation

Again, there are two ways you can set up your computer to run the simulation:
1. **Using Docker** (recommended!!!)
2. If you **already have ROS2** installed and having hard time using docker on your laptop.

### 1) Docker installation (recommended!!!)

Clone the [repository](https://github.com/larics/docker_files/tree/master/ros2/ros2-iron/crazyflies-real-world):
```
git clone https://github.com/larics/docker_files.git
```
And follow the setup instructions  on [this link](https://github.com/larics/docker_files/tree/master/ros2/ros2-jazzy/crazyflies). This docker automatically clones and builds ROS2 mrs_crazyflies_exp package.

### 2) Manual installation (if you already have ROS2 installed)
> We are assuming that you have ROS2 Jazzy installed.

Please follow the instructions given on the [Bitcraze](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/#inst-comp) page to setup cfclient and  this [Crazyswarm2](https://github.com/IMRCLab/crazyswarm2) to setup ROS2 packages. Additionally check for aliases script: [https://github.com/larics/docker_files/tree/ros-iron-cf/ros2/ros2-iron/crazyflies-real-world/to_copy](https://github.com/larics/docker_files/blob/master/ros2/ros2-jazzy/crazyflies/to_copy/aliases) and README in this repository which might come in handy.

The folder structure of this package is:
1. scripts - additional node for static transformation broadcaster from world to odom is there. 
2. launch -  it contains file to launch file which starts crazyflies server, rviz and nodes for publishing velocity to crazyflies.
3. config - here is the main yaml file for crazyflies server
4. startup - it contains the example of starting the crazyflies server and velocity nodes, alongside the control.

## Topics and services

Velocity commands are published on `/cf_x/cmd_vel` to crazyflie cf_x. Pose can be obtained from the topic `/cf_x/pose` and velocity from `/cf_x/velocity`, just keep in mind that for this topic message type is not Twist. 
To take off/land you can call services  `/cf_x/takeoff`, `/cf_x/land`. Current vel_mux.py does takeoff automatically, after the first cmd_vel command, but you can call it on your own. 


## Fly the crazyflies
> [!NOTE]
> Within MRS docker, the `mrs_crazyflies_exp` package is located in `/root/ros2_ws/src/`. All folders and files mentioned later in these instructions are located inside the package In docker, there is an alias `cd_mrs_crazyflies_exp` which changes the directory to this package.

This example showcases how to run the simulation using sessions, tmuxinator and environment variables. You do not need to use this format if you do not find it useful.

To run the example, navigate to `startup` folder and run:
```
./start.sh
```
It will open two windows with several panes it is very similar to the one for the simulation, except in the second window there are examples on how to start websocket bridge to follow data online in foxglove and how to bag using mcap.

After killing the session using ctrl+b, k, there might be some ros2 nodes running in the background, please do the command: kill_ros2, which will kill all ros2 processes running, it is defined in .bash_aliases. Keep this in mind when starting next session. :)

In the file /config/crazyflies_mrs.yaml are defined real addresses for each crazyflie. Please check it if you will use cfclient.

## Working on your project

For developing your solution, you can either create a new package, or you can continue to work in this package. You can write your code in Python or C++.

Feel free to add more windows or to create your own setups and sessions. :)


