#import libraries/modules
from gpiozero import LED, Button
import time
from time import sleep
from random import uniform
from sys import exit

#assign player names
left_name = input("Yellow Gunslinger's Name? ")
right_name = input("Blue Gunslinger's Name? ")

#assign pins, LED, GPIOs
GPIO.setmode(GPIO.BCM)
light=LED(4)
switch1 = 15
switch2 = 14
light.on()
sleep(uniform(5,10))
light.off()
GPIO.setup(led,GPIO.OUT)
GPIO.setup(switch1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch2,GPIO.IN,pull_up_down=GPIO.PUD_UP)

start=time.clock()

try:
    while True:
        if GPIO.input(switch1) == False or GPIO.input(switch2) == False:
            finish = time.clock()
            speed = finish - start
            if GPIO.input(switch1) == False:
                print(left_name + "'s draw speed: " + str(speed) + " seconds\n" + left_name + " is the Champion!\n" right_name + " has been killed!")
                break
            else:
                print(left_name + "'s draw speed: " + str(speed) + " seconds\n" + left_name + " is the Champion!\n" right_name + " has been killed!")
                break
finally:
    print("GAME OVER!")
    GPIO.cleanup()

