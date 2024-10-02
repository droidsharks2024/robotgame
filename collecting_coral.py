'''
this script contains code for collecting krills and coral
for missions 3 and 12
'''

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
MotorA = Motor(Port.F, Direction.COUNTERCLOCKWISE)
MotorB = Motor(Port.B, Direction.CLOCKWISE)

left_angle = MotorA.angle()
right_angle = MotorB.angle()
drive_base = DriveBase(MotorA, MotorB, wheel_diameter=56, axle_track=112)

'''
drive_base.straight(300)
drive_base.turn(-20)
drive_base.straight(150)
drive_base.turn(30)#collect water sample
drive_base.straight(100)#collect krill
drive_base.turn(-50)
drive_base.straight(100)#collect coral1
drive_base.turn(-75)
drive_base.straight(100)#collect coral2
drive_base.turn(25)
drive_base.straight(500)#back to red home base
'''

drive_base.straight(300)
wait(1000)
drive_base.turn(37)
drive_base.straight(100)
wait(1000)
drive_base.turn(-30)
drive_base.straight(100)
wait(1000)
drive_base.turn(47)
drive_base.straight(95)
drive_base.straight(50)
wait(1000)
drive_base.turn(-45)
wait(1000)
drive_base.straight(30)
drive_base.turn(-45)
#drive_base.turn(-25)
#drive_base.turn(-14.5)
