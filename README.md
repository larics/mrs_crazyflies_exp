## MRS-Crazyflies-exp
This ROS2 package contains adapted configuration files and launch files from [CrazySwarm2](https://github.com/IMRCLab/crazyswarm2), that should be used in the 2nd part of the MRS Project for the experimental part.

The experimental part is run on a real crazyflies UAVs and [CrazySwarm2](https://imrclab.github.io/crazyswarm2/) package will be used.

## Reporting problems
If you encounter an error or a problem during the installation, setup or usage, please check the [Issue tab](https://github.com/larics/mrs_crazyflies_exp/issues). If there is no solution to your problem there (in closed and open issues), feel free to open a new issue. When reporting a problem, specify your operating system and method of installation, describe your problem, and include the entire output of the command that resulted in the error. This will be the quickest way to get feedback and will help other students who may encounter the same error in the future. Likewise, if you think something is missing in this README, let us know by opening an issue.

## Installation

Again and again, there are two ways you can set up your computer to run the simulation:
1. **Using Docker** (again, recommended)
2. If you **already have ROS2** installed and having hard time using docker on your laptop.

### 1) Docker installation (recommended!!!)

Clone this [repository](https://github.com/larics/mrs_crazyflies_exp):
```
git clone https://github.com/larics/mrs_crazyflies_exp
```
If you haven't done it by this phase, please, before building execute this line to enable graphical applications:

```
echo "xhost +local:docker > /dev/null" >> ~/.profile

```

Add the following line to  `~/.bashrc` and source it, or type this command in the current terminal:
```
export DOCKER_BUILDKIT=1
```
Run Dockerfile from the project root directory using the following commands:
```bash
cd mrs_crazyflies_exp

# Build the Dockerfile.
docker build -t mrs_crazyflies_exp_img .

# Run the crazysim_img2 container for the first time
./first_run.sh

# This will create docker container crazyswarm_container and position you into the container
```

For future runs, you can use the following commands:
```bash
# Start the container:
docker start -i mrs_crazyflies_exp_cont

# Open the container in another terminal, while it is already started:
docker exec -it mrs_crazyflies_exp_cont bash

# Stop the container
docker stop mrs_crazyflies_exp_cont

# Delete the container (WARNING: this will delete all data inside the container)
docker rm mrs_crazyflies_exp_cont

```
> [!NOTE]
> The ros2 workspace is located in /root/ros2_ws


### 2) Manual installation (if you already have ROS2 installed)
> We are assuming that you have ROS2 humble installed.

Please follow the instructions given on the [Bitcraze](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/#inst-comp) page to setup cfclient and  this [Crazyswarm2](https://github.com/IMRCLab/crazyswarm2) to setup ROS2 packages. Additionally check for aliases README in this repository which might come in handy.



## Topics and services

The ROS2 interface is the same as in simulation phase. Hence, velocity commands are published on `/cf_x/cmd_vel` to crazyflie cf_x. Pose can be obtained from the topic `/cf_x/pose` and velocity from `/cf_x/velocity`, just keep in mind that for this topic message type is not Twist, but a custom message [LogDataGeneric](https://github.com/IMRCLab/crazyswarm2/blob/main/crazyflie_interfaces/msg/LogDataGeneric.msg), whose field elements are defined as: [v_x, v_y, v_z] in a world frame. To take off/land you can call services  `/cf_x/takeoff`, `/cf_x/land`. Current vel_mux.py does takeoff automatically, after the first cmd_vel command, but you can call it on your own. 

## Connecting to Crazyflies
Before connecting to crazyflies you should locally on your laptop, copy file: `to_copy/99-bitcraze.rules` and `to_copy/99-lps.rules` to `/etc/udev/rules.d` directory. Please check these links on USB permissions: [crazyradio](https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/installation/usb_permissions/) and [lps](https://github.com/bitcraze/lps-tools?tab=readme-ov-file#usb-access-right-on-linux)

To connect to crazyflie you must plug in the Crazyradio flashed USB dongle into the laptop.

The general application cfclient to connect to crazyflie can be started with (this shouldn't be running while crazyswarm2 packages are launched):

```
cfclient
```

For connecting with ROS2 crazyswarm2 package follow [instructions](https://imrclab.github.io/crazyswarm2/usage.html)

## Fly the Crazyflies

> [!NOTE]
> Within MRS docker, the `mrs_crazyflies_exp` package is located in `/root/ros2_ws/src/`. All folders and files mentioned later in these instructions are located inside the package In docker, there is an alias `cd_mrs_crazyflies_exp` which changes the directory to this package.

This example showcases how to run the simulation using sessions, tmuxinator and environment variables. You do not need to use this format if you do not find it useful.

To run the example, navigate to `startup` folder in ´mrs_crazyflies_exp´ and run:
```
./start.sh
```
It will open two windows with several panes it is very similar to the one for the simulation (but without Gazebo pane), except in the second window there are examples on how to start websocket bridge to follow data online in foxglove and how to bag using mcap.

After killing the session using ctrl+b, k, there might be some ros2 nodes running in the background, please do the command: kill_ros2, which will kill all ros2 processes running, it is defined in .bash_aliases. Keep this in mind when starting next session. :)

In the file /config/crazyflies_mrs.yaml are defined real addresses for each crazyflie. Please check it if you will use cfclient.

## Working on your project

For developing your solution, you can either create a new package, or you can continue to work in this package. You can write your code in Python or C++.

The folder structure of this package is:
1. scripts - folder where you can put your own scripts
2. launch -  it contains file to launch file which starts crazyflies server, rviz and nodes for publishing velocity to crazyflies.
3. config - here is the main .yaml file for crazyflies server
4. startup - it contains the example of starting the crazyflies server and velocity nodes, alongside the control.

Feel free to add more windows or to create your own setups and sessions. :)

>[!TIP]
**Summary of configurations that need to be changed**
> - `config/crazyflies_mrs.yaml`
>   - Set enable to true/false or comment/uncomment the number of crazyflie specification blocks you want to use.
>   - Change the address if needed
> - `startup/mrs_example_setup.sh`
>   - Modify the environment variables according to your needs.
>   - `$NUM_ROB` - Number of crazyflies you want to use. Should correspond to the number of enabled crazyflies in the `crazyflies_mrs.yaml` and the number of rows in the initial positions file.
> - `startup/example.yml`
>   - You can create your own tmuxinator session files, or modify this one to your needs.
>   - You can add more panes/windows to run your own nodes/scripts.
>   - Update the file in use in `startup/start.sh` if you want to use a different session file.  

