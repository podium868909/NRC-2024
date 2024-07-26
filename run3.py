from functions import move_tank, turn, move_arm

# Note: pseudocode is prone to changes
# Turning is 100% wrong


def main():
    # Run 3
    move_tank(900, None, 100, 100)
    turn(90, 'right', 100)
    move_tank(900, None, 100, 100)  # Wall align with top
    move_tank(0, None, -100, -100)
    turn(90, 'left', -100)
    move_tank(900, None, 100, 100)
    move_tank(40, None, -100, -100)
    turn(45, 'left', -100)
    move_tank(400, None, 100, 100)
