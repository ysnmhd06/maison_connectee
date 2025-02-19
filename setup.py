from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'maison_connectee'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/templates', glob('maison_connectee/templates/*.html')),  # Copie tous les fichiers HTML
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yassin',
    maintainer_email='yassin@todo.todo',
    description='Package ROS2 pour la gestion d’une maison connectée',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'web = maison_connectee.web:main',
        ],
    },
)
