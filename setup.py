from setuptools import setup

package_name = 'bal_ca0_proba'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/launch_example1.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='abel',
    maintainer_email='abel@example.com',
    description='Publikal szinusz es koszinusz jelet',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'trig_publisher = bal_ca0_proba.trig_publisher:main',
            'trig_subscriber = bal_ca0_proba.trig_subscriber:main',
        ],
    },
)
