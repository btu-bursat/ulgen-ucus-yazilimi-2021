#!/bin/bash
# BTU Bursat 1B 2021

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

# Butun kodlar /home/pi/ dizine tasinir
echo -e "${BOLD_BLUE}Butun kodlar /home/pi/ dizinine tasiniyor${NC}"
cp telemetri/telemetri.py /home/pi/telemetri.py

# Servislerin yuklenmesi
echo -e "${BOLD_BLUE}Servisler yukleniyor${NC}"
cp servisler/telemetri.service /etc/systemd/system/telemetri.service

# Servislerin etkinlestirilmesi
systemctl daemon-reload
systemctl enable telemetri
systemctl start telemetri

echo -e "${BOLD_GREEN}Yukleme tamamlandi!${NC}"
