from machine import Pin
import time

led = Pin("LED", Pin.OUT)

for _ in range(20):
    led.value(1)
    time.sleep(2)
    led.value(0)
    time.sleep(2)

