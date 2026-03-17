import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Start Gazebo Server
        ExecuteProcess(
            cmd=['gazebo', '--server'],
            output='screen'
        ),
        # Start Gazebo Client
        ExecuteProcess(
            cmd=['gazebo', '--client'],
            output='screen'
        ),
        # Factory Controller Node
        Node(
            package='factory_controller',
            executable='factory_controller',
            name='factory_controller',
            parameters=[{
                'conveyor_speed': 0.5,  # Set the desired conveyor speed
                'paused': False         # Set to True for paused mode
            }],
            output='screen'
        ),
        # Bottleneck Detector Node
        Node(
            package='bottleneck_detector',
            executable='bottleneck_detector',
            name='bottleneck_detector',
            output='screen'
        ),
        # Bottle Spawner Node
        Node(
            package='bottle_spawner',
            executable='bottle_spawner',
            name='bottle_spawner',
            parameters=[{
                'spawn_rate': 1.0  # Set the desired spawn rate
            }],
            output='screen'
        ),
    ])
