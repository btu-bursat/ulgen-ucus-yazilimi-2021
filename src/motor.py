#!/usr/bin/env python3

import telemetri_verileri as tv
import RPi.GPIO as GPIO

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

		# buralar da komple degisecek
		motor.ChangeDutyCycle(motor_pwm)
		servo.ChangeDutyCycle(servo_pwm)
