#import libraries/modules
from gpiozero import LED, Button
from time import sleep
from random import uniform
import sys


#assign pins to LED and buttons
led = LED(4)
right_button = Button(15)
left_button = Button(14)

#assign player variables
left_name = input('Yellow Gunslingers name is: ')
right_name = input('Blue Gunslingers name is: ')

#turn on LED
led.on()

#randomized wait time for LED to flash within range 3 - 8 seconds
sleep(uniform(5,10))

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
            print(left_name + ' won the round! Ready for next round?')
            led.on()
        else:
            right_win += 1
            print(right_name + ' won the round! Ready for next round?')
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


