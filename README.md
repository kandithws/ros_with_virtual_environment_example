# ros_with_virtual_environment_example
-------

An example to use python virtualenv
(which is recommended to use in many libraries/frameworks installation
, i.e. [TensorFlow](https://www.tensorflow.org/install/install_linux#InstallingVirtualenv),
 [Flask](http://flask.pocoo.org/docs/0.12/installation/),
 etc.. )
with rospy-nodes, which required to use default python interpreter
-- specifically for `roslaunch`.

## Prerequisites
 - ROS in your python environment
 - Your virtual environment with the same python version with ROS

 **Activate your virtual environment (your-venv)
 and install additional ROS-dependency**
~~~
$ source your-venv/bin/activate
(your-venv)$ pip install pip --upgrade
(your-venv)$ pip install -U rosdep rosinstall_generator wstool rosinstall
(your-venv)$ pip install --upgrade setuptools
 ~~~

## Example

**`rosrun` Example**
~~~
$ rosrun simple_publisher talker.py --venv /path/to/your-venv
~~~
**`roslaunch` Example**
~~~
$ cp -r your-venv ~/path/to/ros_virtual_env/your-venv/
$ roslaunch simple_publisher example_venv.launch
~~~

