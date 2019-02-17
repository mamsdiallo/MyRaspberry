Author: Mamadou Diallo
mams.diallo@gmail.com
Date: 16.02.2019

Source: harware-libre.fr "Ajouter une horlog RTC en I2C"

Add Module Real Time Clock through I2C - serially
configuration
0. wiring of the RTC
see instruction for GND, VV, SDA, SCL

1. Activate the i2c module
from confuguration panel

2. Testing the installation I2C
>sudo i2cdetect -y 1

3. install and setup the RTC module
>sudo bash # entering bash mode
>echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-1/new_device
>exit # exiting bash mode

check time for the first time the module is used:
>sudo hwclock -r
2000-01-01 01:26:02.914252+0100
!!! this is not the right time obviously
>date # to check against current date/time
setting time
>sudo hwclock -w
>sudo hwclock -r

4. automatic start up
at the end of file /etc/modules add:
rtc-ds1307

>sudo nano /etc/modules

create the device ds1307 at boot 
by modifying the file /etc/rc.local

>sudo nano /etc/rc.local
 
then add before "exit 0" : 
echo ds1307 0x68 > 
 
>echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-1/new_device
>sudo hwclock -s

5. check 
reboot
from anywhere type:
>hwclock -r
 
