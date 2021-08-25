#!/usr/bin/env python3
# Ulgen, 2021

import RPi.GPIO as GPIO
from time import sleep
import socket

def main():
	global MOTOR_MIN_PWM, MOTOR_MAX_PWM
	global MOTOR_PWM_ARALIGI
	global MOTOR_SIFIR_PWM
	global MOTOR_PWM
	global MOTOR_PIN_1, MOTOR_PIN_2
	global AYRILMA_SIS_PIN
	global motor_1, motor_2

	MOTOR_MIN_PWM, MOTOR_MAX_PWM = 5, 10
	MOTOR_PWM_ARALIGI = MOTOR_MAX_PWM - MOTOR_MIN_PWM
	MOTOR_SIFIR_PWM = 4.5
	MOTOR_PWM = 0
	MOTOR_PIN_1, MOTOR_PIN_2 = 40, 38
	AYRILMA_SIS_PIN = 11

	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(MOTOR_PIN_1, GPIO.OUT)
	GPIO.setup(MOTOR_PIN_2, GPIO.OUT)
	GPIO.setup(AYRILMA_SIS_PIN, GPIO.OUT)

	GPIO.output(AYRILMA_SIS_PIN, GPIO.LOW)
	motor_1 = GPIO.PWM(MOTOR_PIN_1, 50)
	motor_2 = GPIO.PWM(MOTOR_PIN_2, 50)

	# esclerin max pwmi ve min pwmi ogrenmesi icin kalibre ediliyor
	# elimizdeki escleri kalibre etmek icin 20 mslik pulse width kullaniyoruz
	# max motor hizi icin %10 yani 2 mslik duty cycle
	# min motor hizi icin de %5 yani 1 mslik duty cycle kullaniyoruz
	motor_1.start(MOTOR_MAX_PWM)
	motor_2.start(MOTOR_MAX_PWM)
	sleep(10)
	motor_1.ChangeDutyCycle(MOTOR_MIN_PWM)
	motor_2.ChangeDutyCycle(MOTOR_MIN_PWM)
	sleep(10)
	motor_1.ChangeDutyCycle(MOTOR_SIFIR_PWM)
	motor_2.ChangeDutyCycle(MOTOR_SIFIR_PWM)

	host = "localhost"
	port = 5000
	ana_islem = socket.socket()

	while True:
		try:
			ana_islem.connect((host, port))
			logla("Motorlar calismaya basladi")
			break
		except BaseException as e:
			sleep(0.1)

	while True:
		komut = ana_islem.recv(1024).decode()
		if komut == "2":
			tasiyiciyi_ayir()
		elif komut == "3":
			motor_calistir(10)
		elif komut == "4":
			motor_durdur()

def tasiyiciyi_ayir():
	GPIO.output(AYRILMA_SIS_PIN, GPIO.HIGH)
	sleep(3)
	GPIO.output(AYRILMA_SIS_PIN, GPIO.LOW)

def motor_calistir(yuzde):
	MOTOR_PWM = MOTOR_MIN_PWM + ((yuzde / 100) * MOTOR_PWM_ARALIGI)
	motor_1.ChangeDutyCycle(MOTOR_PWM)
	motor_2.ChangeDutyCycle(MOTOR_PWM)

def motor_durdur():
	MOTOR_PWM = MOTOR_SIFIR_PWM
	motor_1.ChangeDutyCycle(MOTOR_PWM)
	motor_2.ChangeDutyCycle(MOTOR_PWM)

def logla(mesaj):
	with open("/home/pi/ulgen/log.txt", "a") as f:
		f.write(mesaj + "\n")

if __name__ == "__main__":
	main()
