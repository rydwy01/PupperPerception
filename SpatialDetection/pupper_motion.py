# our final project code to control pupper based on perception inputs
import numpy as np
from StanfordQuadruped.src.State import State
from StanfordQuadruped.src.Command import Command
#from StanfordQuadruped.src.Controller import Controller

def moveToBall(depth, xcenter):
    #implement controller for xcenter to change yaw
    #implement controller for depth to change speed

    # xcenter is pixel value of center of ball
    # depth is distance to ball
    pixelcenter = 150; # the pixel value of the center of the x axis, NEED TO FIND THIS FROM OAKD

    #implement turncontroller to yaw toward ball
    #- output how rate of yaw to send to 
    state = State()
    current_turn_rate = state.yaw_rate
    turn_rate = yawcontrol(pixelcenter, current_turn_rate, xcenter)
    Command.yaw_rate = turn_rate
    print(Command.yaw_rate)

    #implement forwardcontroller to walk forward toward ball
    #- output speed that pupper should go
    currentspeed = state.horizontal_velocity
    speed = fwdcontrol(0, currentspeed, depth)
    Command.horizontal_velocity = speed
    print(Command.horizontal_velocity)

    return turn_rate, speed

# control the speed of pupper
def fwdcontrol(pos, vel, target):
    Kp = 100
    Kd = 10
    tau = Kp * (target - pos) +Kd * (-1*vel)
    return tau

# control the rate of turn of pupper
def yawcontrol(pos, vel, target):
    Kp = 100
    Kd = 10
    tau = Kp * (target - pos) + Kd * (-1-vel)
    return tau

def main():
    # loop until some offset in depth is reached ie pupper at tennis ball
    moveToBall(0,150)



if __name__ == "__main__":
  main()