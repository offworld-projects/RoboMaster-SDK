#!/usr/bin/env python3

from robomaster import robot

x_val = 1.0
z_val = 45
xy_speed = 3.0


def move_forward():
    chassis.move(x=x_val, y=0, z=0, xy_speed=xy_speed).wait_for_completed()

def move_back():
    chassis.move(x=-x_val, y=0, z=0, xy_speed=xy_speed).wait_for_completed()
def move_left():
    chassis.move(x=x_val, y=0, z=-z_val, xy_speed=xy_speed).wait_for_completed()

def move_right():
    chassis.move(x=x_val, y=0, z=z_val, xy_speed=xy_speed).wait_for_completed()
    

if __name__ == '__main__':
    robot = robot.Robot()
    robot.initialize(conn_type="ap")
    chassis = robot.chassis

    while True:
        try:
            key = input("Enter wasd to move robot: ")
            if key == 'w':
                move_forward()
            elif key == 'a':
                move_left()
            elif key =='s':
                move_back()
            elif key == 'd':
                move_right()


        except Exception:
            robot.close()
            break
