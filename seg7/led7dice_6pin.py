from machine import Pin
import time

pin_no = [12, 13, 14, 15, 16 ,17, 18]

led = [Pin(pin_no[i], Pin.OUT) for i in range(7)]

'''
led1 = Pin(12, Pin.OUT)
led2 = Pin(13, Pin.OUT)
led3 = Pin(14, Pin.OUT)
led4 = Pin(15, Pin.OUT)
led5 = Pin(16, Pin.OUT)
led6 = Pin(17, Pin.OUT)
led7 = Pin(18, Pin.OUT)
'''
blink_pattern =[[1, 0, 0, 0, 0, 0, 0],
               [1, 1, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0]]

def blinkLED(pattern):
    for i in range(len(pattern)):
        for j in range(7):
            led[j].value(pattern[i][j])
        time.sleep(1)


while True :
    blinkLED(blink_pattern)

'''
led1.value(1)
    time.sleep(1)
    
    led2.value(1)
    time.sleep(1)
    
    led3.value(1)
    led4.value(1)
    led5.value(1)
    led6.value(1)
    led7.value(1)
    time.sleep(1)
    
    led1.value(0)
    led2.value(0) 
    led3.value(0)
    led4.value(0)
    led5.value(0)
    led6.value(0)
    led7.value(0)
    time.sleep(1)
'''