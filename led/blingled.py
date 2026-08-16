from machine import Pin
import time

led = Pin("LED", Pin.OUT)
bling_time = 0.5

led.value(1)
time.sleep(bling_time)
led.value(0)
time.sleep(bling_time)

led.value(1)
time.sleep(bling_time)
led.value(0)
time.sleep(bling_time)

led.value(1)
time.sleep(bling_time)
led.value(0)
time.sleep(bling_time)
