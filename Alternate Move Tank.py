#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch

ev3 = EV3Brick()
lm = Motor(Port.B, Direction.CLOCKWISE)
rm = Motor(Port.C, Direction.CLOCKWISE)
arm = Motor(Port.D, Direction.CLOCKWISE)
ls = ColorSensor(Port.S3)


def move_time(lspeed, rspeed, time):
    rspeed = rspeed * -1
    invertl = -1 if lspeed > 0 else 1
    invertr = -1 if rspeed > 0 else 1
    lm.reset_angle(0)
    rm.reset_angle(0)
    watch = StopWatch()
    timenow = watch.time()
    while (watch.time() - timenow) < time:
        error = abs(lm.angle()) - abs(rm.angle())
        turn_rate = error * -1
        lm.dc((abs(lspeed) + turn_rate) * invertl)
        rm.dc((abs(rspeed) - turn_rate) * invertr)

    lm.dc(0)
    rm.dc(0)


def move(lspeed, rspeed, degrees):
    currleft = lm.angle()
    currright = rm.angle()
    if lspeed == 0:
        rm.run_angle(rspeed * 18, degrees)
    elif rspeed == 0:
        lm.run_angle(-lspeed * 18, degrees)
    elif abs(lspeed) != abs(rspeed):
        invertl = -1 if lspeed > 0 else 1
        invertr = -1 if rspeed < 0 else 1
        factor = abs(lspeed / rspeed)
        while (abs(lm.angle() - currleft) + abs(rm.angle() - currright)) / 2 < degrees:
            error = abs(lm.angle() - currleft) - (abs(rm.angle() - currright) * factor)
            turn_rate = error * -1
            lm.dc((abs(lspeed) + turn_rate) * invertl)
            rm.dc((abs(rspeed) - (turn_rate / factor)) * invertr)
    else:
        invertl = -1 if lspeed > 0 else 1
        invertr = -1 if rspeed < 0 else 1
        while abs(lm.angle() - currleft) < degrees:
            error = abs(lm.angle() - currleft) - abs(rm.angle() - currright)
            turn_rate = error * -1
            lm.dc((abs(lspeed) + turn_rate) * invertl)
            rm.dc((abs(rspeed) - turn_rate) * invertr)
    lm.dc(0)
    rm.dc(0)


def turn(direction, degrees):
    if direction == 'left':
        move(0,100,90) # Could
    elif direction == 'right':
        move(0,100,90) # Could change
    else:
        move(100,100)



# Turn right
move(100,100,50) # to be changed
arm.run_angle(-100,90) # Move arm up

move(100,100,100)
turn(direction = 'right', degrees = 90)
move(100,100,100)
move(100,0,90)




'''
turn right
move, collect white man
turn 45 deg to left
release and collect
135 to left
move straight -> blue man, release and collect 
135 left
move deposit everything
somehow wall align with most left wall
move forward, turn left move forward turn left and collect
wall glide along up most wall
move right and color scan 
deposit cube
turn 135 right 
move forward flip water thing
turn left
deposit/collect the kayak
move back and wall align with most right wall
move to collect red man
move forward deposit green kayak
'''



wait(100)

arm.run_angle(100, 90)
move(50, 50, 1000)
