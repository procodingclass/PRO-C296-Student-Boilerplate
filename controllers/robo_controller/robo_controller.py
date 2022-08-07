from controller import Robot
import math

robot = Robot()

timestep = int(robot.getBasicTimeStep())

imu= robot.getDevice("inertial unit")
imu.enable(timestep)

            
while robot.step(timestep) != -1:

    angle=imu.getRollPitchYaw()
    
    yaw_current= round(math.degrees(angle[2]))+180
    
    print(yaw_current)
