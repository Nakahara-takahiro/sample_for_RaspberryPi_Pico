from machine import Pin
import time

pin_no = [12, 13, 14, 15, 16 ,17, 18]

leds = [Pin(pin_no[i], Pin.OUT) for i in range(7)]


blink_pattern =[[1, 0, 0, 0, 0, 0, 0],
               [1, 1, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0]]

def blinkLED(pattern):
    for i in range(len(pattern)):
        for j in range(7):
            leds[j].value(pattern[i][j])
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

'''GEMINIの解答
from machine import Pin
import time

leds = [Pin(i, Pin.OUT) for i in range(12, 19)]  # ピン番号のリストを作成

while True:
    for led in leds:  # 順番にLEDを点灯
        led.value(1)
        time.sleep(1)

    for led in reversed(leds):  # 逆順にLEDを消灯
        led.value(0)
        time.sleep(1)
'''
'''copilotの解答
from machine import Pin
import time

# LEDのピン番号をリストで管理
led_pins = [12, 13, 14, 15, 16, 17, 18]

# 各LEDのピンを設定
leds = [Pin(pin_num, Pin.OUT) for pin_num in led_pins]

while True:
    # 全てのLEDを点灯
    for led in leds:
        led.value(1)
    time.sleep(1)
    
    # 全てのLEDを消灯
    for led in leds:
        led.value(0)
    time.sleep(1)
'''