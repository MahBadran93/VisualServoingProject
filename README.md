
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
This repository includes the code necessery to implement the visual servoing reltated tasks. The first task is to allow the robot to follow a specific line where the second task is to enable the robot to stop and park when detecting a QR and AR tags. To develop the project we faced many challenges regarding the environment setup since our devices can't handle installing and working with Gazebo simulation. So, we have another solution like using the online platform, **The Constructsim**. <br>
Another problem comes with the online platform which is the stability and the constraints of setting up a map that works for our tasks.
Luckily, we were able to complete the line follow task using the online platform. <br>
For task two, we tried to make it work using the online platform but we faced many problems regarding the map and importing the necessery and required models to complete the task like Qr code. So we decided to use local devices and install gazebo for task two.

<h1 align="center">  </h1> <br>

## Implementation 
- Task 1: 
  - For this task we used the construct platform to implement. The code is tested on different maps which are provided by the <a href="https://app.theconstructsim.com/#/Desktop"> OpenCV Basics for Robotics(Unit5)</a>  and the <a href="https://app.theconstructsim.com/#/Desktop"> ROS Perception (unit3) </a> courses in the construct platform. <br>
        <p align = "center">
        <img  src = "Demonstration Resources/followlineMapTurtleBot.png" width=500> <br>
        <em> The map provided by the Perception course(unit3) in the construct platform</em>
        </p>
        <p align = "center">
        <img  src = "Demonstration Resources/streetMapRosBot.png" width=400> <br>
        <em> The map provided by the OpenCv course(unit5) in the construct platform</em>
        </p>

  - The Construct platform provide a static environment setup where it is hard to control the Robot, and other model positions and orientations (we need that because it is important for us to easily move the robot to different poses to check that our algorithm is working  and the the Robot can detect and follow the line from different poses).<br>
   We tried to work with  **Ros Development Studio** which is an online IDE created by the construct to create our own projects and provide robotics environment where it is easier and more flexible to make some modifications on the map simulation. So our goal here is to import the specific map created by the <a href="https://app.theconstructsim.com/#/Desktop"> OpenCV Basics for Robotics(Unit5)</a> course to our project in Ros Development Studio which allows for more flexibility in controling the models in the map. But doing that was not easy and created a lot of problems for us, like the models some times becomes invisible and can't be seen in the map simulation and for some models we can only see the bounding boxes without the meshes and other problems that affects the lighting and could lead to some issues that will make the robot diverge from the line. 

   - **To run the code:** 
     - In [catkin_ws](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws) workspace, under [src](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src) folder we created a package called [followline](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src/followline). This package is responsible for the line follow task. 
     - [follow_line.py](https://github.com/MahBadran93/VisualServoingProject/blob/main/catkin_ws/src/followline/src/follow_line.py) file has been created   inside the [src](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src/followline/src) in the [followline](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src/followline)  
     - You can download the [followline](https://github.com/MahBadran93/VisualServoingProject/tree/main/catkin_ws/src/followline) package and import it into your **catkin_ws** workspace or you can go directly to the construct platform (Perception course unit 3) to test the code on the same map then add the **followline** package to their **catkin_ws** workspace **src** folder. 
     - After that, you need to build the workspace by changing the path to **catkin_ws** directory and run the **catkin_make** command.
     - After the building is done, type **source/devel/setup.bash** command in the terminal.
     - Now, type **rosrun followline follow_line.py** and the robot should start following the line.  

