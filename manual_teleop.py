#!/usr/bin/env python3

from robomaster import robot

x_val = 0.2
z_val = 45


def move_forward():
    chassis.move(x=x_val, y=0, z=0).wait_for_completed()

def move_back():
    chassis.move(x=-1 * x_val, y=0, z=0).wait_for_completed()

def move_left():
    chassis.move(x=x_val, y=0, z=-1 * z_val).wait_for_completed()

def move_right():
    chassis.move(x=x_val, y=0, z=z_val).wait_for_completed()
    

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
                move_forward()
            elif key == 'd':
                move_right()


        except Exception:
            robot.close()
            break
