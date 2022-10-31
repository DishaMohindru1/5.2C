from tkinter import *
import tkinter.font
from gpiozero import LED 

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

Red = LED(14)
YelloW = LED(15)
Green = LED(18)

win = Tk() #creating a window.
win.title("LED Toggler") #creating  the title of the window.
winFont = tkinter.font.Font(family = 'Cambria', size = 12, weight = "bold") # defining custom font

def RedLedToggle():

    if Red.is_lit:
        Red.off()
        RedLedButton["text"] = "Turn on Red LED"

    else:

        YelloW.off()
        Green.off()
        Red.on()
        RedLedButton["text"] = "Turn on Red LED "


def YellowLedToggle():

    if YelloW.is_lit:

        YelloW.off()
        YellowLedButton["text"] = "Turn on Yellow LED"

    else:

        Red.off()
        Green.off()
        YelloW.on()
        YellowLedButton["text"] = "Turn off Yellow LED "


def GreenLedToggle():

    if Green.is_lit:

        Green.off()
        GreenLedButton["text"] = "Turn on Green LED"

    else:

        Red.off()
        YelloW.off()
        Green.on()
        GreenLedButton["text"] = "Turn Green LED"

def close():

    GPIO.cleanup()
    Red.off()
    YelloW.off()
    Green.off()
    win.destroy()

RedLedButton = Radiobutton(win, text = 'Turn on Red LED', font  = Ariel, command = RedLedToggle, bg = 'red', height = 1, width = 24)  
RedLedButton.grid(row=0, column=1)

YellowLedButton = Radiobutton(win, text = 'Turn on Yellow LED', font  = Ariel, command = YellowLedToggle, bg = 'yellow', height = 1, width = 24)  
YellowLedButton.grid(row=1, column=1)

GreenLedButton = Radiobutton(win, text = 'Turn on Green LED', font  = Ariel, command = GreenLedToggle, bg = 'green', height = 1, width = 24)  
GreenLedButton.grid(row=2, column=1)

exitButton = Radiobutton(win, text = 'Exit', font  = Ariel, command = close, bg = 'black', height = 1, width = 24)  
exitButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()

