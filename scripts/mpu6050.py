#!/usr/bin/env python3
# Ulgen, 2021

import telemetri_verileri as tv
from time import sleep
import adafruit_mpu6050
import board
import numpy as np
import math

def calistir():
	i2c = board.I2C()
	mpu6050 = adafruit_mpu6050.MPU6050(i2c)
	while True:
		tv.ivme_x, tv.ivme_y, tv.ivme_z = mpu6050.acceleration

		tv.roll = np.arctan(tv.ivme_x / (math.sqrt((tv.ivme_y ** 2) + (tv.ivme_z ** 2)))) * 120
		tv.pitch = np.arctan(tv.ivme_y / (math.sqrt((tv.ivme_x ** 2) + (tv.ivme_z ** 2)))) * 120
		tv.yaw = mpu6050.gyro[2]
