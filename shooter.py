#import libraries/modules
python
from gpiozero import LED, Button
from time import sleep
from random import uniform
import sys
import RPi.GPIO as GPIO
import time

#assign pins to LED and buttons
led = LED(4)
right_button = Button(15)
left_button = Button(14)

#assign player variables
left_name = input('left player name is: ')
right_name = input('right player name is: ')

#turn on LED
led.on()

#randomized wait time for LED to flash within range 3 - 8 seconds
sleep(uniform(3,8))

#turn off LED
led.off()

#identify who won via pin assignment
def pressed(button):
    left_win=0
    right_win=0
#displays round winner and adds cumulative scores
    while left_win or right_win < 3:
        if button.pin.number == 14:
            left_win += 1
            print(left_name + ' won the round!\nReady for next round?')
            led.on()
        else:
            right_win += 1
            print(right_name + ' won the round!\nReady for next round?')
            led.on()
#displays the players' total scores and ultimate
    if left_win or right_win == 3:
        if left_win > right_win:
            print(left_name + "'s score is: " + left_win + "\n" + right_name + "'s score is: " + right_win + "\nThe winner is" + left_name + "!")
        else right_win > left_win:
            print(left_name + "'s score is: " + left_win + "\n" + right_name + "'s score is: " + right_win + "\nThe winner is" + right_name + "!")
    sys.exit()
    exit()

#pressed button will call pressed(button) function to determine who won
right_button.when_pressed=pressed
left_button.when_pressed=pressed

#add in a timer, to work out how long it took the players to press the button after the LED turned off
GPIO.setmode(GPIO.BCM)
#indicate which pins we will use in these variables
right_button = Button(15)
left_button = Button(14)
led_pin = 4
#setup the LED pin as an out pin
GPIO.setup(led_pin,GPIO.OUT)
#setup the switch pin as a switch that is always on by default (thus IN)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    while True:
        #since switch is always on by default, pressing button causes False
        if GPIO.input(switch_pin)== False:
            #print a message with the formatted current time (string format time method)
            print("Button Pressed at "+time.strftime("%Y/%m/%d - %H:%M:%S"))
            GPIO.output(led_pin,True) #turn on LED
            time.sleep(2) #wait 2 seconds
            GPIO.output(led_pin,False) #turn off LED
finally:
    print("cleaning up")
    GPIO.cleanup()
