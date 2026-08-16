from machine import Pin
import  time

SW_PIN_R = 6
SW_PIN_G = 11
SW_PIN_B = 8

sw_r = Pin(SW_PIN_R, Pin.IN, Pin.PULL_DOWN)
sw_g = Pin(SW_PIN_G, Pin.IN, Pin.PULL_DOWN)
sw_b = Pin(SW_PIN_B, Pin.IN, Pin.PULL_DOWN)

while True :
    if sw_r.value() == 1:
        print('r_hit')
    
    if sw_g.value() == 1:
        print('g_hit')
    
    if sw_b.value() == 1:
        print('b_hit')
    time.sleep(1)

