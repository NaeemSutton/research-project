# "Exploring ROS 2 Navigation: A Hilbert Curve Approach"

## Introduction

Welcome to our research project on exploration and navigation using ROS 2! In this project, we aim to enhance the navigation capabilities of vacuum robots by implementing innovative strategies and leveraging advanced technologies. Our research focuses on integrating the Hilbert Curve algorithm for navigation alongside the ROS 2 framework, Navigation 2 (Nav2), and SLAM Toolbox. 


## Objectives

Our primary objective is to investigate the feasibility and effectiveness of implementing the Hilbert Curve algorithm for robot navigation. By utilizing this algorithm, we aim to improve room coverage, consistency, and efficiency in vacuum robot navigation.

## Hardware Setup

Our hardware setup includes:

- **Create 3 Roomba**: A versatile vacuum robot platform.
- **Raspberry Pi 4**: A powerful single-board computer for controlling the robot.
- **LiDAR Camera**: Essential for mapping and localization tasks.
- **Ubuntu 22.04**: The operating system for running ROS 2 and related software.

 <img src="https://camo.githubusercontent.com/1c5fd5dd9a040804fbbbfc1951dc11d20b60228061170e13a68ba5662ad64dca/68747470733a2f2f69726f626f74656475636174696f6e2e6769746875622e696f2f637265617465335f646f63732f6578616d706c65732f646174612f637265617465335f6c696461725f746f702e6a7067" alt="Google Logo" width="400">

## Software Components

We leverage the following software components:

- **ROS 2**: The Robot Operating System 2 provides a flexible framework for developing robot applications.
- **Navigation 2 (Nav2)**: A navigation stack offering advanced features such as dynamic reconfiguration.
- **SLAM Toolbox**: Essential for Simultaneous Localization and Mapping tasks.
- **Hilbert Curve Algorithm**: Implemented for navigation to enhance coverage and efficiency.

## Methodology

Our methodology involves the following steps:

1. **Hardware Integration**: Integrating the hardware components to create a functional robot platform.
2. **Software Development**: Developing ROS 2 nodes and packages to control the robot and implement the Hilbert Curve algorithm.
3. **Experimentation**: Conducting experiments to evaluate the performance of our navigation system in various environments.
4. **Analysis and Optimization**: Analyzing experimental results and exploring optimizations to improve navigation performance.

# Instructions for setting up ROS2, SLAM Toolbox, Navigation 2 and downloading our code.

## Overview

This guide provides step-by-step instructions on how to install and set up ROS2, SLAM Toolbox, and Navigation 2 on your system.

## Installation Steps

Follow the instructions below to install each component:

- [Installing ROS2](#installing-ros2)
- [Installing SLAM Toolbox](#installing-slam-toolbox)
- [Installing Navigation 2](#installing-navigation-2)

## Installation Details

### Installing ROS2

ROS 2 (Robot Operating System 2) is a set of software libraries and tools for building robot applications. Here's how to install ROS2:

#### Set locale

```Bash
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify setting
```

#### Adding ROS 2 Apt Repository

You will need to add the ROS 2 apt repository to your system.

```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

Now add the ROS 2 GPG key with apt.

```bash 
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

Then add the repository to your sources list.

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

#### Install development tools and ROS tools

Install common packages

```Bash 
  sudo apt update && sudo apt install -y \
  python3-flake8-docstrings \
  python3-pip \
  python3-pytest-cov \
  ros-dev-tools
  ```

# For Ubuntu 22.04 LTS and later

```Bash
sudo apt install -y \
   python3-flake8-blind-except \
   python3-flake8-builtins \
   python3-flake8-class-newline \
   python3-flake8-comprehensions \
   python3-flake8-deprecated \
   python3-flake8-import-order \
   python3-flake8-quotes \
   python3-pytest-repeat \
   python3-pytest-rerunfailures
   ```

### Installing Navigation 2

Navigation 2 is a powerful ROS2 package for robot navigation. Here's how to install it:

#### Installing Nav2 Packages
```bash
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup
```
#### Configuring DDS Implementation
```bash
sudo apt install ros-humble-rmw-cyclonedds-cpp
```

#### Installing SLAM Toolbox
```bash
sudo apt install ros-humble-slam-toolbox
```


# Setup instructions for our code repository.

## Overview

This guide provides step-by-step instructions on how to download and use the code from our repository.

## Downloading the Code

1. Open a terminal.

2. Clone the repository using the `git clone` command:

   ```bash
   git clone https://github.com/NaeemSutton/Hilbert-Curve-for-ROS-2-Robots.git
   ```
3. Navigate to the downloaded directory:

   ```bash
   cd .../Hilbert-Curve-for-ROS-2-Robots
   ```

   ## Downloading the Code

4. Ensure that the Python script has execute permissions. If not, use the chmod command to add execute permissions:

    ```bash
    chmod +x hilbert_curve_navigation.py
    ```

5. Make sure ROS 2 is properly installed on your system. If not, you can follow the instructions provided earlier.

6. Source your ROS 2 installation:

    ```bash
    source /opt/ros/humble/setup.bash
    ```
7. Build the workspace:
    ```bash
    colcon build
    ```
8. Source your workspace:
    ```bash
    source install/setup.bash
    ``` 
9. Run the Python script using ROS 2 commands:

```bash
   python3 nav.py
   ```



## Conclusion

In conclusion, our research project aims to advance the state-of-the-art in robot navigation by implementing the Hilbert Curve algorithm alongside ROS 2 and other advanced technologies. Through our experimentation and analysis, we seek to provide valuable insights and solutions for enhancing the navigation capabilities of vacuum robots and other robotic platforms.


