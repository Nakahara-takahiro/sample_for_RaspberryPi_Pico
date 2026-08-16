from machine import Pin, PWM, time_pulse_us
import utime

#センサー初期設定
TEMP = 20

TRIG_PIN = 14
ECHO_PIN = 15

s_speed = 331.5 + 0.6 * TEMP

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

trig.value(0)
utime.sleep(1)

#サーボ初期設定
SERVO_PIN = 16
PWM_FREQ = 50

def measure():
    trig.value(1)
    utime.sleep_us(20)
    trig.value(0)
    
    while echo.value() == 0:
        sigoff = utime.ticks_us()
    while echo.value() == 1:
        sigon = utime.ticks_us()
    dist = (sigon - sigoff) * s_speed / 2 * (10 ** -4)
    return dist

def pulse_width(val, freq = PWM_FREQ, resol = 65535):
    pulse = freq * val * 1e-6 * resol
    return int(pulse)

def rotmotor(pulse):
    duty = pulse_width(pulse)
    servo.duty_u16(duty)
    utime.sleep(0.1)

def cnvPulse(degrees):
    if degrees < -90:
         degrees = -90
    if degrees > 90:
         degrees = 90
    return -degrees*1000/90+1500

def cnvDeg(dist):
    if dist < 5:
        dist = 5
    if dist > 105:
        dist = 105
    deg = 1.8 * dist - 99
    return deg

servo = PWM(Pin(SERVO_PIN))
servo.freq(PWM_FREQ)

while True:
    distance = measure()
    deg = cnvDeg(distance)
    pulse = cnvPulse(deg)
    rotmotor(pulse)