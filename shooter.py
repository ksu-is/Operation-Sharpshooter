#import libraries/modules
python
from gpiozero import LED, Button
from time import sleep
from random import uniform
import sys

#assign pins to LED and buttons
led = LED(4)
right_button = Button(15)
left_button = Button(14)

#assign player variables
left_name = input('left player name is ')
right_name = input('right player name is ')

#turn on LED
led.on()

#randomized wait time for LED to flash within range 3 - 8 seconds
sleep(uniform(3,8))

#turn off LED
led.off()

#identify who won via pin assignment
def pressed(button):
    if button.pin.number == 14:
        print(left_name + ' won the game')
    else:
        print(right_name + ' won the game')
    sys.exit()

#pressed button will call pressed(button) function to determine who won
right_button.when_pressed=pressed
left_button.when_pressed=pressed

#put the game into a loop (remove `exit()`) so that the LED comes on again
#add scores for both players that accumulate over a number of rounds, and displays the players' total scores
#add in a timer, to work out how long it took the players to press the button after the LED turned off

