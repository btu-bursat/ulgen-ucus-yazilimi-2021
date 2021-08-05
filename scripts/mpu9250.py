#!/usr/bin/env python3
# Ulgen, 2021

import telemetri_verileri as tv
from FaBo9Axis_MPU9250 import MPU9250
from time import sleep

def calistir():
	mpu9250 = MPU9250()
	while True:
		tv.ivme_x = mpu9250.readAccel()['x']
		tv.ivme_y = mpu9250.readAccel()['y']
		tv.ivme_z = mpu9250.readAccel()['z']
		tv.roll = mpu9250.readGyro()['x']
		tv.pitch = mpu9250.readGyro()['y']
		tv.yaw = mpu9250.readGyro()['z']
		sleep(0.3)
