from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor  = Motor(Port.B, Direction.CLOCKWISE)
right_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
motor_gear1 = Motor(Port.E, Direction.CLOCKWISE)

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

drive_base.straight(110)
drive_base.turn(36)
drive_base.straight(780)
motor_gear1.run(-300)
wait(1000)
motor_gear1.stop()
