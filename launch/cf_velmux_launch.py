import os
import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
import launch_ros.actions

def generate_launch_description():
    
    # load crazyflies
    crazyflies_yaml = os.path.join(
        get_package_share_directory('mrs_crazyflies_exp'),
        'config',
        'crazyflies_mrs.yaml')

    with open(crazyflies_yaml, 'r') as ymlfile:
        crazyflies = yaml.safe_load(ymlfile)

    server_params = crazyflies
    
    

    launch_description = []
    launch_description.append(
        IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('crazyflie'), 'launch'),
            '/launch.py']),
        launch_arguments={
            'crazyflies_yaml_file':os.path.join(get_package_share_directory('mrs_crazyflies_exp'),'config','crazyflies_mrs.yaml'),
            'backend': 'cflib',
            'gui': 'False',
            'teleop': 'False',
            'mocap': 'False',
            'rviz' : 'True',
            }.items())),
    
    # launch_description.append(
    #     Node(
    #         package='mrs_crazyflies_exp',
    #         executable='TransformWorld2Odom.py',
    #         name='TransformWorld2Odom',
    #         output='screen'
    #     ))
        
        # Add vel_mux nodes dynamically based on the number parameter
    for i in range(1, int(os.environ.get('NUM_ROBOTS', '3')) + 1):
        namespace = f'cf_{i}'
        vel_mux_node = Node(
            package='crazyflie',
            executable='vel_mux.py',
            name=f'vel_mux{i}',
            output='screen',
            namespace=namespace,
            parameters=[
                {"hover_height": 0.5},
                {"incoming_twist_topic": "cmd_vel"},
                {"robot_prefix": f"/{namespace}"}
            ]
        )
        launch_description.append(vel_mux_node)
    
    return LaunchDescription(launch_description)
