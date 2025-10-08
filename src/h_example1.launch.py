from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='bal_ca0_proba',
            executable='trig_wave_publisher',
            name='trig_wave_node',
            output='screen',
            parameters=[{
                'frequency': 1.0,
                'amplitude': 1.0,
                'rate': 50.0
            }]
        )
    ])
