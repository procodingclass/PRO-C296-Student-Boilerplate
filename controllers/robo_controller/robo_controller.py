from controller import Robot
import math

robot = Robot()

timestep = int(robot.getBasicTimeStep())

imu= robot.getDevice("inertial unit")
imu.enable(timestep)

            
while robot.step(timestep) != -1:

    angle=imu.getRollPitchYaw()
    
    yaw_current= angle[2]
    
    print(yaw_current)