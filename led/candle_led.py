from machine import Pin
import time

LED_PIN = 18

led = Pin(LED_PIN, Pin.OUT)

led.value(1)
time.sleep(10)

led.value(0)