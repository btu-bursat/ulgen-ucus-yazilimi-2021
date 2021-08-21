#!/usr/bin/env python3
# Ulgen, 2021

import RPi.GPIO as GPIO
from time import sleep
import socket

def main():
	global MOTOR_MIN_PWM, MOTOR_MAX_PWM
	global MOTOR_PWM_ARALIGI
	global MOTOR_PWM
	global MOTOR_PIN_1, MOTOR_PIN_2
	global AYRILMA_SIS_PIN
	global motor_1, motor_2

	MOTOR_MIN_PWM, MOTOR_MAX_PWM = 18.5, 22
	MOTOR_PWM_ARALIGI = MOTOR_MAX_PWM - MOTOR_MIN_PWM
	MOTOR_PWM = 0
	MOTOR_PIN_1, MOTOR_PIN_2 = 32, 33
	AYRILMA_SIS_PIN = 11

	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(MOTOR_PIN_1, GPIO.OUT)
	GPIO.setup(MOTOR_PIN_2, GPIO.OUT)
	GPIO.setup(AYRILMA_SIS_PIN, GPIO.OUT)

	GPIO.output(AYRILMA_SIS_PIN, GPIO.LOW)
	motor_1 = GPIO.PWM(MOTOR_PIN_1, 50)
	motor_2 = GPIO.PWM(MOTOR_PIN_2, 50)

	motor_1.start(0)
	motor_2.start(0)

	host = "localhost"
	port = 5000
	while True:
		try:
			ana_islem = socket.socket()
			ana_islem.connect((host, port))
			break
		except:
			sleep(0.5)

	while True:
		komut = ana_islem.recv(1024).decode()
		if komut == "2":
			tasiyiciyi_ayir()
		elif komut == "3":
			motor_calistir(20)
		elif komut == "4":
			motor_calistir(0)

def tasiyiciyi_ayir():
	GPIO.output(AYRILMA_SIS_PIN, GPIO.HIGH)
	sleep(3)
	GPIO.output(AYRILMA_SIS_PIN, GPIO.LOW)

def motor_calistir(yuzde):
	MOTOR_PWM = MOTOR_MIN_PWM + ((yuzde / 100) * MOTOR_PWM_ARALIGI)
	motor_1.ChangeDutyCycle(MOTOR_PWM)
	motor_2.ChangeDutyCycle(MOTOR_PWM)

if __name__ == "__main__":
	main()
