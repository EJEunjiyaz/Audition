from machine import Pin, ADC, DAC, PWM
from time import sleep
from _thread import start_new_thread as thread


"Joystick code"
PINX = 34   # needs to be a pin that supports ADC
PINY = 32   # needs to be a pin that supports ADC
PINSW = 27

cx = ADC(Pin(PINX))
cx.atten(ADC.ATTN_11DB)
cy = ADC(Pin(PINY))
cy.atten(ADC.ATTN_11DB)
sw = Pin(PINSW, Pin.IN, Pin.PULL_UP)

def joystick(adc):
    return max(6, min(120, int(adc.read()/32)))

def check_joystick(dx, dy):
    "0=center, 1=left, 2=right, 3=up, 4=down, 5=up-left, 6=down-right, 7=up-right, 8=down-left"
    x = joystick(dx)
    y = joystick(dy)
    direction = 0
    if x < 14 and 54 < y < 64:
        direction = 1
    elif 113 < x and 54 < y < 64:
        direction = 2
    elif 54 < x < 64 and y < 13:
        direction = 3
    elif 54 < x < 64 and 113 < y:
        direction = 4
    elif x < 14 and y < 14:
        direction = 5
    elif 113 < x and 113 < y:
        direction = 6
    elif 113 < x and y < 14:
        direction = 7
    elif x < 14 and 113 < y:
        direction = 8
    return direction

sw.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed)


"Buzzer code"
buzzer = PWM(Pin(25))

def start_buzzer(value):
    buzzer.freq(value)

def stop_buzzer():
    buzzer.deinit()


"RGB code"
R = Pin(23, Pin.OUT)
G = Pin(19, Pin.OUT)
B = Pin(18, Pin.OUT)

def start_rgb_red():
    R.value(1)
    G.value(0)
    B.value(0)

def start_rgb_green():
    R.value(0)
    G.value(1)
    B.value(0)

def start_rgb_blue():
    R.value(0)
    G.value(0)
    B.value(1)

def stop_rgb():
    R.value(0)
    G.value(0)
    B.value(0)


"Button code"
button = Pin(5, Pin.IN)

def check_button():
    status = None
    if button.value() == 0:
        status = True
    elif button.value() == 1:
        status = False
    return status   #True = pressed, False = not pressed






start_val = False
button_val = False

def first():
    count_game = 0
    first_game = True
    datastat = {}

def start():
	start_val = False
    if button_val == True:
    	sleep(1):
    	#print screen 3 2 1
    	#buzzer makes sound
    	return start_val = True

def game():
	count_correct = 0
    count_ingame = 0
    count_game += 1

    if first_game == True:
    	while start_val == True:
			correct = False
			#recieve server to control the number of game.
			#print screen up down left rights.
	        #check count_correct
	        count_ingame += 1
			if correct==True:
				count_correct += 1
	        if count_ingame == count_server:
	            start_val = False
	    data_new = {str(count_game):int(count_correct)}
	    first_game = False

	else:
		while start_val == True:
			correct = False
			#recieve server to control the number of game.
			#print screen up down left rights.
	        #check count_correct
	        count_ingame += 1
			if correct==True:
				count_correct += 1
	        if count_ingame == count_server:
	            start_val = False
	    data_new = {str(count_game):int(count_correct)}

def data():
	datastat.update(data_new)

def end():
	#display score
	#sent netPRO to server
    #data.update({count_game:count_correct})


thread(joystick, (cx, cy))
