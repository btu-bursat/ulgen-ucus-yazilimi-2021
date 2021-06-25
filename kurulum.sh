#!/bin/bash
# BTU Ulgen, 2021

# Renklendirme icin degiskenler
BOLD_RED="\033[1;31m"
BOLD_BLUE="\033[1;34m"
BOLD_GREEN="\033[1;32m"
BOLD_BLACK="\033[1;30m"
BOLD_CYAN="\033[1;36m"
BOLD_PURPLE="\033[1;35m"
BOLD_WHITE="\033[1;37m"
BOLD_YELLOW="\033[1;33m"
NC="\033[00m"

# Servislerin kurulabilmesi icin root haklarina sahip olmak gerekiyor
if [ "$EUID" -ne 0 ]
then
	echo -e "${BOLD_RED}Root hakkina sahip degilsiniz!${NC}"
	echo -e "Sunu deneyin: sudo $0"
	exit
fi

# Sistem guncelleniyor
echo -e "${BOLD_BLUE}Sistem guncelleniyor ve gerekli yazilimlar yukleniyor${NC}"
#apt update
#apt install python3-pip
#pip3 install FaBo9Axis-MPU9250-python3

# Telemetri verilerini toplamak icin yeni dizin olusturulur
echo -e "${BOLD_BLUE}Telemetri verileri icin yeni dizin olusturuluyor${NC}"
mkdir -p /home/pi/telemetri_verileri

# Gerekli telemetri verileri icin dosyalar olusturulur
echo -n "39374" > /home/pi/telemetri_verileri/takim_no
echo -n "1" > /home/pi/telemetri_verileri/paket_numarasi
echo -n "" > /home/pi/telemetri_verileri/basinc
echo -n "" > /home/pi/telemetri_verileri/yukseklik
echo -n "" > /home/pi/telemetri_verileri/inis_hizi
echo -n "" > /home/pi/telemetri_verileri/sicaklik
echo -n "" > /home/pi/telemetri_verileri/pil_gerilimi
echo -n "" > /home/pi/telemetri_verileri/gps_latitude
echo -n "" > /home/pi/telemetri_verileri/gps_longitude
echo -n "" > /home/pi/telemetri_verileri/gps_altitude
echo -n "1" > /home/pi/telemetri_verileri/uydu_statusu
echo -n "" > /home/pi/telemetri_verileri/pitch
echo -n "" > /home/pi/telemetri_verileri/roll
echo -n "" > /home/pi/telemetri_verileri/yaw
echo -n "" > /home/pi/telemetri_verileri/donus_sayisi
echo -n "Hayir" > /home/pi/telemetri_verileri/video_aktarim_bilgisi
echo -n "" > /home/pi/telemetri_verileri/ivme_x
echo -n "" > /home/pi/telemetri_verileri/ivme_y
echo -n "" > /home/pi/telemetri_verileri/ivme_z

# Butun kodlar /home/pi/ dizine tasinir
echo -e "${BOLD_BLUE}Butun kodlar /home/pi/ dizinine tasiniyor${NC}"
cp telemetri/telemetri.py /home/pi/telemetri.py
cp telemetri/mpu9255.py /home/pi/mpu9255.py

# Servislerin yuklenmesi
echo -e "${BOLD_BLUE}Servisler yukleniyor${NC}"
cp servisler/*.service /etc/systemd/system/

# Servislerin etkinlestirilmesi
systemctl daemon-reload
systemctl enable telemetri
systemctl start telemetri
systemctl enable mpu9255
systemctl start mpu9255

echo -e "${BOLD_GREEN}Yukleme tamamlandi!${NC}"
