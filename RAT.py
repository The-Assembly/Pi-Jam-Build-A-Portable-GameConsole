#Copyright (C) 2020 The Assembly, All Rights Reserved
#Authors Asif Rasheed, Shaham Kampala, Rawan Suwwan
import time
import Adafruit_GPIO.SPI as SPI
import os
import board
import digitalio
import keyboard

button1 = digitalio.DigitalInOut(board.D21)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.D5)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

button3 = digitalio.DigitalInOut(board.D6)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

button4 = digitalio.DigitalInOut(board.D12)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.UP

start = digitalio.DigitalInOut(board.D13)
start.direction = digitalio.Direction.INPUT
start.pull = digitalio.Pull.UP

up = digitalio.DigitalInOut(board.D26)
up.direction = digitalio.Direction.INPUT
up.pull = digitalio.Pull.UP

down = digitalio.DigitalInOut(board.D19)
down.direction = digitalio.Direction.INPUT
down.pull = digitalio.Pull.UP

left = digitalio.DigitalInOut(board.D20)
left.direction = digitalio.Direction.INPUT
left.pull = digitalio.Pull.UP

right = digitalio.DigitalInOut(board.D16)
right.direction = digitalio.Direction.INPUT
right.pull = digitalio.Pull.UP

while True:
	if (not button3.value) and (not start.value): #select button
		keyboard.press('k')
		time.sleep(0.167)
		keyboard.release('k')
	elif not button3.value:
		keyboard.press('b')
		time.sleep(0.167)
		keyboard.release('b')
	else:
		if not start.value:
			keyboard.press('s')
			time.sleep(0.167)
			keyboard.release('s')

	if not button1.value:
		keyboard.press('d')
		time.sleep(0.167)
		keyboard.release('d')

	if not button2.value:
		keyboard.press('a')
		time.sleep(0.167)
		keyboard.release('a')

	if not button4.value:
		keyboard.press('c')
		time.sleep(0.167)
		keyboard.release('c')

	if (not down.value) and (not start.value): #exit button = select + start
		keyboard.press('k+s')
		time.sleep(0.167)
		keyboard.release('k+s')
#===================================
	#combination1
	if (not up.value) and (not button1.value):
		keyboard.press('d+up')
		time.sleep(0.167)
		keyboard.release('d+up')
	elif (not up.value) and (not button2.value):
		keyboard.press('a+up')
		time.sleep(0.167)
		keyboard.release('a+up')
	elif (not up.value) and (not button3.value):
		keyboard.press('b+up')
		time.sleep(0.167)
		keyboard.release('b+up')
	elif (not up.value) and (not button4.value):
		keyboard.press('c+up')
		time.sleep(0.167)
		keyboard.release('c+up')
	elif not up.value:
		keyboard.press('up')
		time.sleep(0.167)
		keyboard.release('up')

	#combination2
	if (not down.value) and (not button1.value):
		keyboard.press('d+down')
		time.sleep(0.167)
		keyboard.release('d+down')
	elif (not down.value) and (not button2.value):
		keyboard.press('a+down')
		time.sleep(0.167)
		keyboard.release('a+down')
	elif (not down.value) and (not button3.value):
		keyboard.press('b+down')
		time.sleep(0.167)
		keyboard.release('b+down')
	elif (not down.value) and (not button4.value):
		keyboard.press('c+down')
		time.sleep(0.167)
		keyboard.release('c+down')
	elif not down.value:
		keyboard.press('down')
		time.sleep(0.167)
		keyboard.release('down')
	elif not down.value:
		keyboard.press('down')
		time.sleep(0.167)
		keyboard.release('down')

	#combination3
	if (not left.value) and (not button1.value):
		keyboard.press('d+left')
		time.sleep(0.167)
		keyboard.release('d+left')
	elif (not left.value) and (not button2.value):
		keyboard.press('a+left')
		time.sleep(0.167)
		keyboard.release('a+left')
	elif (not left.value) and (not button3.value):
		keyboard.press('b+left')
		time.sleep(0.167)
		keyboard.release('b+left')
	elif (not left.value) and (not button4.value):
		keyboard.press('c+left')
		time.sleep(0.167)
		keyboard.release('c+left')
	elif not left.value:
		keyboard.press('left')
		time.sleep(0.167)
		keyboard.release('left')

	#combination4
	if (not right.value) and (not button1.value):
		keyboard.press('d+right')
		time.sleep(0.167)
		keyboard.release('d+right')
	elif (not right.value) and (not button2.value):
		keyboard.press('a+right')
		time.sleep(0.167)
		keyboard.release('a+right')
	elif (not right.value) and (not button3.value):
		keyboard.press('b+right')
		time.sleep(0.167)
		keyboard.release('b+right')
	elif (not right.value) and (not button4.value):
		keyboard.press('c+right')
		time.sleep(0.167)
		keyboard.release('c+right')
	elif not right.value:
		keyboard.press('right')
		time.sleep(0.167)
		keyboard.release('right')




