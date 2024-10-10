'''
   This script is written for mission 1: Coral nursery and mission 4: scuba diver
'''

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
left_wheel = Motor(Port.F, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.B, Direction.CLOCKWISE)
attachment = Motor(Port.E)

left_angle = left_wheel.angle()
right_angle = right_wheel.angle()
attachment_angle = attachment.angle()
drive_base = DriveBase(left_wheel, right_wheel, wheel_diameter=56, axle_track=112)
drive_base.use_gyro(True)

#mission 1 coral buds
drive_base.straight(300)
drive_base.turn(15)
drive_base.straight(375)
drive_base.turn(-90)
attachment.run(25)
drive_base.straight(75)

#mission 4 beginning
attachment.run(100)
wait(1000)
drive_base.straight(-100)
drive_base.turn(80)
attachment.run(-45)
drive_base.straight(100)