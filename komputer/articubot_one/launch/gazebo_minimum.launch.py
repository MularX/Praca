from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='gzserver',
            name='gzserver',
            output='screen',
            parameters=[{
                'use_sim_time': True
            }],
        ),
        Node(
            package='gazebo_ros',
            executable='gzclient',
            name='gzclient',
            output='screen',
        ),
    ])

