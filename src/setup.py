from setuptools import setup

package_name = 'bal_ca0_kisbeadando'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['bal_ca0_kisbeadando/launch_example1.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Te',
    maintainer_email='te@pelda.hu',
    description='Négyszögjel generáló ROS2 node',
    license='MIT',
    entry_points={
        'console_scripts': [
            'square_wave_publisher = bal_ca0_kisbeadando.square_wave_publisher:main',
        ],
    },
)
