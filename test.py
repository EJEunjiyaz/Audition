from machine import Pin
from time import sleep
from random import choice




























a = ['a','b','c','d']

def button():
	button_val = False
    BTN_PIN = 5
    btn = Pin(BTN_PIN,Pin.IN)
    if btn==1:
    	return button_value = True

def start():
	start_val = False
    if button_val == True:
    	sleep(1):
    	#print screen 3 2 1
    	return start_val = True

def game():
	if start_val == True:
		#print screen uo down left rights






import network
from time import sleep
import json
import urequests

ssid = 'exceed16_8'
pwd = '12345678'
station = network.WLAN(network.STA_IF)
station.active(True)

url = "https://exceed.superposition.pknn.dev/data/200"
data = {"1":100}
headers = {"content-type":"application/json"}

if True:
  if not station.isconnected():
    station.connect(ssid, pwd)
    print('Connecting...')
    sleep(3)
    if station.isconnected():
      print('connected')
  js = json.dumps({"data":data})
  print(data)
  r = urequests.put(url, data=js, headers=headers)
  results = r.json()
  print(results)
  sleep(2)

  if not station.isconnected():
    station.connect(ssid, pwd)
    print('Connecting...')
    sleep(3)
    if station.isconnected():
      print('connected')
  js = json.dumps({"data":data})
  print(data)
  r = urequests.put(url, data=js, headers=headers)
  results = r.json()
  print(results)
  sleep(2)
























"https://github.com/equinor/micropython/wiki/OLED-Display-(SSD1351)"
