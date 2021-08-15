#!/bin/bash

# Servislerin kurulabilmesi icin root haklarina sahip olmak gerekiyor
if [ "$EUID" -ne 0 ]
then
	echo "Programi soyle calistirin: sudo $0"
	exit
fi

# Sistemin guncellenmesi ve gerekli yazilimlarin kurulmasi
#apt update
#apt install -y python3-pip
#pip3 install FaBo9Axis-MPU9250-python3 adafruit-circuitpython-bmp280

# Butun kodlar /home/pi/ dizine tasinir
cp scripts/* /home/pi/

# Servislerin yuklenmesi
cp ulgen.service /etc/systemd/system/
cp motor.service /etc/systemd/system/

# Servislerin etkinlestirilmesi
systemctl daemon-reload

systemctl enable ulgen
systemctl start ulgen

systemctl enable motor
systemctl start motor
