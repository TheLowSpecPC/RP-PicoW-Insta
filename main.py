import controls
import network
import socket
from pico_i2c_lcd import I2cLcd
from machine import I2C, Pin
from time import sleep

I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

sda = Pin(8, Pin.PULL_UP)

scl = Pin(9, Pin.PULL_UP)

i2c = I2C(0, sda=sda, scl=scl, freq=400000)
print(i2c.scan())
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.move_to(1,0)
lcd.putstr("RP PicoW Insta")
lcd.move_to(0,1)
lcd.putstr("By: TheLowSpecPC")
sleep(2)
lcd.clear()

# Connect to WiFi
lcd.move_to(0,0)
lcd.putstr("Enter WiFi SSID")
sleep(1.5)
lcd.clear()
wifi_ssid = controls.KeyPad()
lcd.clear()

lcd.move_to(1,0)
lcd.putstr("Enter WiFi Password")
sleep(1.5)
lcd.clear()
wifi_password = controls.KeyPad()
lcd.clear()

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_password)
while wlan.isconnected() == False:
    lcd.putstr('Waiting for connection...')
    sleep(1)
lcd.clear()
status = wlan.ifconfig()

lcd.move_to(0,0)
lcd.putstr('connected to:')
lcd.move_to(1,0)
lcd.putstr(wifi_ssid)
sleep(2)
lcd.clear()

lcd.move_to(0,0)
lcd.putstr('IP-adress:')
lcd.move_to(1,0)
lcd.putstr(status[0])

sock = socket.socket()
sock.connect(('google.com', 80))
sock.write('GET / HTTP/1.0\nHost: google.com\n\n')
sock.readline()