from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='bal_ca0_proba',
            executable='trig_wave_publisher',
            output='screen'
        ),
        Node(
            package='bal_ca0_proba',
            executable='trig_wave_subscriber',
            output='screen'
        ),
    ])

