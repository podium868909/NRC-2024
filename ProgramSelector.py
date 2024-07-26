#!/usr/bin/env pybricks-micropython
import time
import run1
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button
from pybricks.tools import StopWatch
from functions import robot

run_options = ["Run 1", "Run 2", "Run 3", "Run 4", "Run 5", "Run 6", "Run 7", "Run 8", "Run 9", "Run 10"]
current = 0


def main():
    global current
    robot.screen.clear()
    robot.screen.draw_text(0, 0, run_options[current])
    while True:
        if robot.buttons.pressed() == Button.UP:
            robot.speaker.play_file(SoundFile.CLICK)
            if current > 0:
                current += 1
                robot.screen.clear()
                robot.screen.draw_text(0, 0, run_options[current])
        elif robot.buttons.pressed() == Button.DOWN:
            robot.speaker.play_file(SoundFile.CLICK)
            if current < len(run_options) - 1:
                current -= 1
                robot.screen.clear()
                robot.screen.draw_text(0, 0, run_options[current])
        elif robot.buttons.pressed() == Button.CENTER:
            robot.speaker.play_file(SoundFile.CLICK)
            time_taken_run = StopWatch()
            robot.screen.clear()
            robot.screen.draw_text(0, 0, str("Running" + run_options[current]))
            if current == 0:
                run1.main()
            elif current == 1:
                pass
            elif current == 2:
                pass
            robot.screen.clear()
            print("Total seconds taken for", run_options[current], ":", time_taken_run.time() / 1000, "s")
            robot.screen.print(time_taken_run.time() / 1000)
            while True:
                if robot.buttons.pressed() is not None:
                    break
        time.sleep(0.1)


if __name__ == "__main__":
    time_taken = StopWatch()
    main()
    print("Total seconds taken:", time_taken.time() / 1000, "s")
    robot.screen.print(time_taken.time() / 1000)
    while True:
        pass
