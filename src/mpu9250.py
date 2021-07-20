#!/usr/bin/env python3

import sensor_verileri as sv
from FaBo9Axis_MPU9250 import MPU9250
from time import sleep

mpu9250 = MPU9250()

def calistir():
	while True:
		sv.ivme_x = mpu9250.readAccel()['x']
		sv.ivme_y = mpu9250.readAccel()['y']
		sv.ivme_z = mpu9250.readAccel()['z']
		sv.pitch = mpu9250.readGyro()['x']
		sv.roll = mpu9250.readGyro()['y']
		sv.yaw = mpu9250.readGyro()['z']
		sleep(0.5)
