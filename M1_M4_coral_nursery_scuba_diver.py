from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

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
wait(1000)
drive_base.straight(130)

#mission 4 beginning
wait(1000)
attachment.run(70)
wait(1000)
drive_base.straight(-100)
drive_base.turn(80)
attachment.run(-45)
wait(1000)
attachment.run(-60)
wait(1000)
drive_base.straight(80)
drive_base.straight(10)

'''
#coral tree
drive_base.straight(200)
wait(1000)
drive_base.straight(-320)
wait(1000)
drive_base.straight(140)
wait(1000)
drive_base.straight(400)
wait(1000)
#drive_base.straight(-300)
'''
