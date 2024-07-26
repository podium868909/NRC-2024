#!/usr/bin/env pybricks-micropython
import time
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button
from pybricks.tools import StopWatch
from functions import robot
import run1, run2, run3
from functions import move_tank, turn


run_options = ["Run 1", "Run 2", "Run 3", "Run 4", "Run 5", "Run 6", "Run 7", "Run 8", "Run 9", "Run 10"]
current = 0
# Hard code parameters
water_location = []
white_outside = False


def main():
    global current
    robot.screen.clear()
    robot.screen.draw_text(0, 0, run_options[current])
    while True:
        if Button.UP in robot.buttons.pressed():
            robot.speaker.play_file(SoundFile.CLICK)
            if current < len(run_options) - 1:
                current += 1
                robot.screen.clear()
                robot.screen.draw_text(0, 0, run_options[current])
        elif Button.DOWN in robot.buttons.pressed():
            robot.speaker.play_file(SoundFile.CLICK)
            if current > 0:
                current -= 1
                robot.screen.clear()
                robot.screen.draw_text(0, 0, run_options[current])
        elif Button.CENTER in robot.buttons.pressed():
            robot.speaker.play_file(SoundFile.CLICK)
            time_taken_run = StopWatch()
            robot.screen.clear()
            robot.screen.draw_text(0, 0, str("Running: " + run_options[current]))
            if current == 0:
                run1.main()
            elif current == 1:
                run1.main()
            elif current == 2:
                run1.main()
            robot.screen.clear()
            print("Total seconds taken for", run_options[current], ":", time_taken_run.time() / 1000, "s")
            robot.screen.draw_text(0, 0, time_taken_run.time() / 1000)
        time.sleep(0.06)


main()

