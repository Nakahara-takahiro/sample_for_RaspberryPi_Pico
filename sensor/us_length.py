from machine import Pin, time_pulse_us
import utime

TEMP = 20

TRIG_PIN = 14
ECHO_PIN = 15

s_speed = 331.5 + 0.6 * TEMP

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

trig.value(0)
utime.sleep(1)

def measure():
    trig.value(1)
    utime.sleep_us(20)
    trig.value(0)
    
    while echo.value() == 0:
        sigoff = utime.ticks_us()
    while echo.value() == 1:
        sigon = utime.ticks_us()
    dist = (sigon - sigoff) * s_speed/2 *(10**-4)
    return dist

while True:
    distance = measure()
    print('Distance:{:.1f} cm'.format(distance))
    utime.sleep(1)