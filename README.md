
<h1 align="center"> Visual Servoing Project </h1> <br>
<h3 align="center"> Multi-Sensor Fusion & Tracking</h3> <br>
<p align="center">
University Of Burgundy
  <p align="center">
    <a href="https://www.vibot.org/"> <img src = "https://www.vibot.org/uploads/2/3/5/8/2358523/696297.png" width=60> </a>
  </p>
</p>
<h3 align="center">                       
Supervisors: 
</h3>
<p align='center'> Omar Tahri <p>
<h4 align="center">                       
Students:
</h4>
 <p align='center'> Thien Bao BUI, Mahmoud Badran, <a href="https://github.com/akhawaja2014"> Muhammad Arsalan Khawaja </a> <p> <br>
<h1 align="center">  </h1> <br>

## Introduction
This repository includes the code necessery to implement the visual servoing reltated tasks. The first task is to allow the robot to follow a specific line where the second task is to enable the robot to stop and park when detecting a QR tag. To develop the project we faced many challenges regarding the environment setup since our devices can't handle installing and working with Gazebo simulation. So, we had another solution like using the online platform, **The Constructsim**. <br>
Other problems come with the online platform which is the stability and the constraints of setting up a map that works for our tasks.
Luckily, we were able to complete the line follow task using the online platform. <br>
For task two, we tried to make it work using the online platform but we faced many problems regarding the map and importing the necessery and required models to complete the task like Qr code. So we decided to use local devices and install gazebo for task two.
<h1 align="center">  </h1> <br>

## Implementation 
- **Dependencies:** 
  - The Constructsim platform 
  - ROS Melodic
  - Python
  - C++ 
  - OpenCV 
  - VISP 

- **Task 1 Follow Line** 
  - For this task we used the construct platform to implement. The code is tested on different custom maps which are provided by the <a href="https://app.theconstructsim.com/#/Course/48"> OpenCV Basics for Robotics(Unit 5)</a>  and the <a href="https://app.theconstructsim.com/#/Course/5"> ROS Perception (unit 3) </a> courses in the construct platform. <br>
        <p align = "center">
        <img  src = "Demonstration Resources/followlineMapTurtleBot.png" width=500> <br>
        <em> The map provided by the Perception course(unit3) in the construct platform</em>
        </p>
        <p align = "center">
        <img  src = "Demonstration Resources/streetMapRosBot.png" width=400> <br>
        <em> The map provided by the OpenCv course(unit5) in the construct platform</em>
        </p>

  - The Construct platform courses provide a static gazebo environment setup where it is hard to control the Robot, and other model positions and orientations(Constraints in gazebo user interface setup where we will not be able to control the Robot using the Gzebo user interface), we need that because it is important for us to easily move the robot to different poses to check that our algorithm is working  and the the Robot can detect and follow the line from different poses.<br>
   We tried to work with  **Ros Development Studio** which is an online IDE created by the construct to create our own projects and provide robotics environment where it is easier and more flexible to make some modifications on the map simulation. So we tried to import the custom map created by the <a href="https://app.theconstructsim.com/#/Course/48"> OpenCV Basics for Robotics(Unit 5)</a> course to our project in Ros Development Studio which allows for more flexibility in controling the models in the map. To do that we need to find and import all the dependent packages to launch the map and configure the project accordingly But doing that was not easy and created a lot of problems for us, like the models some times becomes invisible and can't be seen in the map simulation and for some models we can only see the bounding boxes without the meshes and other problems that affects the lighting and could lead to some issues that will make the robot diverge from the line. 

   - **To run the code:** 
     - In [catkin_ws](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws) workspace, under [src](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src) folder we created a package called [followline](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src/followline). This package is responsible for the line follow task. 
     - [follow_line.py](https://github.com/MahBadran93/VisualServoingProject/blob/main/catkin_ws/src/followline/src/follow_line.py) file has been created   inside the [src](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src/followline/src) folder in the [followline](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src/followline) package.
     - You can download the [followline](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src/followline) package and import it into your **catkin_ws** workspace or you can go directly to the construct platform (Perception course unit 3) to test the code on the same map then add the **followline** package to **src** folder in their **catkin_ws** workspace. 
     - After that, you need to build the workspace by changing the path to **catkin_ws** directory and run the **catkin_make** command.
     - After the building is done, type **source/devel/setup.bash** command in the terminal.
     - Now, type **rosrun followline follow_line.py** and the robot should start following the line. 
     - Video demonstration below: 
       <p align="center">
        https://www.loom.com/share/e3fb418493244c50b8359afff7d42a46
       </p> 
     - As we discussed before, we tried to use **Ros Development Studio** in the construct platform to be able to easily change the Robot pose. To import the map (we choose to import the map provided by the OpenCv course unit 5) two packages needed, [opencv_course_sims](https://bitbucket.org/theconstructcore/opencv_course_sims/src/master/) and **rosbot_husarion** where they include the map files (models, world, urdf, launch). Click  <a href="https://app.theconstructsim.com/#/l/c8d160f/"> Here </a> to go to the project page in **ROS Development Studio** (you need to login to the construct platform).
     - After launching the project in **ROS Development Studio**, you can customize your screen layout and open the important applications like terminal, gazebo, Rviz graphic tool.
     - To run the code you need to import the map by typing **roslaunch unit_5_sim course_simulation_5.launch** in the terminal and wait till you see the map fully rendered in the gazebo application.
     - When you see the map fully rendered, you can control the Robot pose using gazebo but you need to be sure that the robot camera can see the line. You can check by using the **rqt** graphic tool, type **rqt_image_view** and you will see the camera view in Rviz.
     - After that, run the **follow_line.py** file. Type **rosrun followline follow_line.py**
     - video demonstration below: 
       <p align="center">
        https://www.loom.com/share/33ca77c452934220803740d948a3f46c
       </p>
     - Using the map from the opencv course and importing it in **ROS Development Studio** for the follow line task was good interm of the ability to customize our maps and add models and easily change their positions but the problem is the stability and the rendered map can sometimes be different from the map in the course where it leads to some performance issues. For example, sometimes it can be noticed that the rendered map is more dark and affect the quality of the images observed by the Robot which affect the algorithm performance. 

-  **Task2 Parking** <br>
    For task 2 it was not possible for us to set up the required custom map using the construct platform. To implement this task we need a custom map with a QR code included. We created QR model using blender modeling software but to import it in the the construct gazebo environment created problems in the map and the model was not fully rendered so we decided to work on our local machines and install ROS and Gazebo. <br> 
    - **How to run:** 
      - We created a package called [vs_proj](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src/vs_proj) which will handle the parking task. In this package [src](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src/vs_proj/src)  folder we created [vs.cpp](https://github.com/MahBadran93/VisualServoingProject/blob/main/catkin_ws/src/vs_proj/src/vs.cpp) file where we implemented the parking task.  
      - To setup the environment and run the code in your machine, you need to have **ROS Melodic** installed. We also used the **turtlebot3 waffle model** and **world** so you need to have the **turtlebot3** and the **turtlebot3_simulations** packages installed so we already installed these packages in the [src](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src) folder of [catkin_ws](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws) package. So what you need is to install the files inside this [src](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src) folder and add them to your **src** folder in your **catkin_ws** working space. Then **build** and **source** your **catkin_ws** working space.
      - After that, You need to add Qr tag model to the world and it is done by installing the [marker0](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src/vs_proj/marker0) folder in our [vs_proj](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src/vs_proj) package and add it to the **models** folder in your **gazebo** folder. After that the Qr model will appear in the **Insert** tab in your gazebo with **Marker0** name.
        <p align = "center">
        <img  src = "Demonstration Resources/options_turtlebotWorld.png" width=200> 
         <img  src = "catkin_ws/src/vs_proj/marker0/materials/textures/Marker0.png" width=100> <br>
        <em> The left image is the Gazebo Insert tab where you can find the Marker0 model to drag into the world. The right image you can see the Marker0 model</em>
        </p>
     

      - Now everything is ready to run the code. First,  you need to launch the **turtlebot3_world** and you can do that by typing **roslaunch turtlebot3_gazebo turtlebot3_world.launch** in the terminal. If launching the world failed and an error related to **TURTLEBOT3_MODEL** appears just type **export TURTLEBOT3_MODEL=waffle** in the terminal and then launch the world. After the world is rendered in gazebo you go to the **Insert** tab and drag the **Marker0** model infront of the robot in the world. 
    
        <p align = "center">
        <img  src = "Demonstration Resources/turtlebot3_world.png" width=400> <br>
        <em> Turtlebot 3 World</em>
        </p>

      - Now you need to launch the [vs.launch](https://github.com/MahBadran93/VisualServoingProject/blob/main/catkin_ws/src/vs_proj/launch/vs.launch) file in the [launch](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src/vs_proj/launch) folder of the [vs_proj](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src/vs_proj) package by typing **roslaunch  vs_proj vs.launch** in the terminal.
      - Video demonstration below: 
        <p align="center">
         https://www.loom.com/share/4f69c94907ab4e16b4684f05f108281b
        </p>
      - We tested the parking on another map with rosbot robot: 
        <p align="center">
         https://www.loom.com/share/c799fd210d9442be976f0a9e7bee650f
        </p>

    


