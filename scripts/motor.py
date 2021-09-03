#!/usr/bin/env python3
# Ulgen, 2021

from time import sleep
import board
import busio
import adafruit_pca9685

import telemetri_verileri as tv

def calistir():
	global MOTOR_MIN_PWM, MOTOR_MAX_PWM
	global MOTOR_PWM_ARALIGI, MOTOR_PWM
	global motor_1, motor_2
	global ayrilma

	MOTOR_MIN_PWM, MOTOR_MAX_PWM = 3276, 6553
	MOTOR_PWM_ARALIGI = MOTOR_MAX_PWM - MOTOR_MIN_PWM
	MOTOR_PWM = 0

	i2c = busio.I2C(board.SCL, board.SDA)
	pca = adafruit_pca9685.PCA9685(i2c)
	pca.frequency = 50

	motor_1, motor_2 = pca.channels[0], pca.channels[1]
	ayrilma = pca.channels[2]

	# Esclerin max pwmi ve min pwmi ogrenmesi icin kalibre ediliyor
	# elimizdeki escleri kalibre etmek icin 20 mslik pulse width kullaniyoruz
	# max motor hizi icin %10 yani 2 mslik duty cycle
	# min motor hizi icin de %5 yani 1 mslik duty cycle kullaniyoruz
	motor_1.duty_cycle, motor_2.duty_cycle = MOTOR_MIN_PWM, MOTOR_MIN_PWM
	ayrilma.duty_cycle = 0
	sleep(10)

	while True:
		if tv.komut == "2":
			tasiyiciyi_ayir()
		elif tv.komut == "3":
			motor_calistir(10)
		elif tv.komut == "4":
			motor_calistir(0)

def tasiyiciyi_ayir():
	ayrilma.duty_cycle = 0xFFFF
	sleep(3)
	ayrilma.duty_cycle = 0

def motor_calistir(yuzde):
	MOTOR_PWM = MOTOR_MIN_PWM + ((yuzde / 100) * MOTOR_PWM_ARALIGI)
	motor_1.duty_cycle, motor_2.duty_cycle = MOTOR_PWM, MOTOR_PWM
