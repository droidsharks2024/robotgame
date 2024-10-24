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
drive_base.use_gyro(True)


'''
drive_base.straight(300)
wait(1000)
drive_base.turn(37)
drive_base.straight(100)
wait(1000)
drive_base.turn(-24)
drive_base.straight(120)
wait(1000)
drive_base.turn(45)
drive_base.straight(95)
drive_base.straight(50)
wait(1000)
drive_base.turn(-20)
drive_base.turn(-25)
wait(1000)
drive_base.straight(30)
wait(1000)
drive_base.turn(-65)
drive_base.straight(700)
drive_base.straight(200)
'''

#drive_base.turn(-12)
#drive_base.straight(150)
#drive_base.turn(15)
#drive_base.straight(100)
#drive_base.turn(-25)
#drive_base.straight(175)
#drive_base.turn(-87)
drive_base.turn(20)
drive_base.straight(650)
