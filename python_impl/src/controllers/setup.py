from setuptools import find_packages, setup

package_name = 'controllers'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='anton',
    maintainer_email='a.bredenbeck@tudelft.nl',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'example_traj = controllers.example_traj:main',
            'main = controllers.main:main',
            'Drawing= controllers.Drawing:main',
            'Dropping= controllers.Dropping:main',
            'Constant = controllers.Constant_V:main',
            'Pointer = controllers.Pointer:main'
        ],
    }

)