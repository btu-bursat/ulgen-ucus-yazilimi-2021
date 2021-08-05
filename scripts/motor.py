#!/usr/bin/env python3
# Ulgen, 2021

import telemetri_verileri as tv
import RPi.GPIO as GPIO
from time import sleep

def calistir():
	global motor, servo
	global motor_pin, servo_pin
	global motor_pwm, motor_bonus_pwm, motor_dusuk_pwm
	global servo_pwm

	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)

	motor_pin, servo_pin = 11, 7
	GPIO.setup(motor_pin, GPIO.OUT)
	GPIO.setup(servo_pin, GPIO.OUT)

	motor = GPIO.PWM(motor_pin, 50)
	servo = GPIO.PWM(servo_pin, 50)

	motor.start(0)
	servo.start(0)

	motor_pwm = 30
	motor_dusuk_pwm = 15
	motor_bonus_pwm = 50
	servo_pwm = 0

	while True:
		# ivmeye gore pwm burada ayarlanacak
		# tv.ivme_y
		# motor_pwm += delta
		# falan filan

		if tv.uydu_statusu == 1:
			sleep(1)
			pass
		elif tv.uydu_statusu == 2:
			sleep(0.5)
			pass

		# buralar da komple degisecek
		motor.ChangeDutyCycle(motor_pwm)

def tasiyiciyi_ayir():
	# servoyu 180 dereceye ayarla
	servo.ChangeDutyCycle(12)
	# ayrılmasını bekle
	sleep(2)
	# servoyu 0 dereceye ayarla
	servo.ChangeDutyCycle(0)

def motor_calistir(pwm):
	motor.ChangeDutyCycle(pwm)

def motor_durdur():
	motor.ChangeDutyCycle(0)
