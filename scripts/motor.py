#!/usr/bin/env python3
# Ulgen, 2021

import telemetri_verileri as tv
import RPi.GPIO as GPIO
from time import sleep

def calistir():
	global MOTOR_MIN_PWM, MOTOR_MAX_PWM
	global MOTOR_PWM_ARALIGI
	global MOTOR_PWM
	global MOTOR_PIN_1, MOTOR_PIN_2
	global AYRILMA_SIS_PIN
	global motor_1, motor_2

	MOTOR_MIN_PWM, MOTOR_MAX_PWM = 18.5, 23
	MOTOR_PWM_ARALIGI = MOTOR_MAX_PWM - MOTOR_MIN_PWM
	MOTOR_PWM = 0
	MOTOR_PIN_1, MOTOR_PIN_2 = 10, 38
	AYRILMA_SIS_PIN = 11

	GPIO.cleanup()

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

def tasiyiciyi_ayir():
	print(AYRILMA_SIS_PIN)
	GPIO.output(AYRILMA_SIS_PIN, GPIO.HIGH)
	sleep(3)
	GPIO.output(AYRILMA_SIS_PIN, GPIO.LOW)

def motor_calistir(yuzde):
	MOTOR_PWM = MOTOR_MIN_PWM + ((yuzde / 100) * MOTOR_PWM_ARALIGI)
	motor_1.ChangeDutyCycle(MOTOR_PWM)
	motor_2.ChangeDutyCycle(MOTOR_PWM)

def motor_durdur():
	motor_1.ChangeDutyCycle(0)
	motor_2.ChangeDutyCycle(0)
