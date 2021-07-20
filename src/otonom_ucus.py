#!/usr/bin/env python3

import telemetri_verileri as tv
import RPi.GPIO as GPIO
from time import sleep

def calistir():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)

	motor_pin = 11
	GPIO.setup(motor_pin, GPIO.OUT)
	motor_pwm = 30
	motor_dusuk_pwm = 15
	motor_bonus_pwm = 50
	p = GPIO.PWM(motor_pin, 50)
	p.start(0)

	# ayrilma icin gerekli pinlerin ayarlanmasi
	#servo_pin = 7
	
	while True:
		# ivmeye gore pwm burada ayarlanacak
		# tv.ivme_y
		# motor_pwm += delta
		# falan filan
		if tv.komut == "2":
			pass
		elif tv.komut == "3":
			p.ChangeDutyCycle(motor_pwm)
		elif tv.komut == "4":
			p.ChangeDutyCycle(0)

		if tv.uydu_statusu == "1":
			pass
		# devami da yazilacak
