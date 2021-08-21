#!/usr/bin/env python3
# Ulgen, 2021

import telemetri_verileri as tv
from FaBo9Axis_MPU9250 import MPU9250
from time import sleep
import numpy as np
import math

def calistir():
	mpu9250 = MPU9250()
	while True:
		ivme = mpu9250.readAccel()
		gyro = mpu9250.readGyro()

		tv.ivme_x = ivme['x']
		tv.ivme_y = ivme['y']
		tv.ivme_z = ivme['z']

		#tv.roll = gyro['x']
		#tv.pitch = gyro['y']
		tv.roll = np.arctan(tv.ivme_x/(math.sqrt((tv.ivme_y ** 2) + (tv.ivme_z ** 2)))) * 120
		tv.pitch = np.arctan(tv.ivme_y / (math.sqrt((tv.ivme_x ** 2) + (tv.ivme_z ** 2)))) * 120
		tv.yaw = gyro['z']
