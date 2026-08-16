from machine import Pin, PWM, time_pulse_us
import utime
#import time

TEMP = 20

#センサー接続用
TRIG_PIN = 14
ECHO_PIN = 15

#サーボモーター接続用
SERVO_PIN = 16
PWM_FREQ = 50

#センサー初期設定
s_speed = 331.5 + 0.6 * TEMP

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

trig.value(0)
utime.sleep(1)

#センサーで使う関数群
def measure():
    trig.value(1)
    utime.sleep_us(20)
    trig.value(0)
    
    #届くまで待つ
    while echo.value() == 0:
        sigoff = utime.ticks_us()
        #print('off:', sigoff)
    while echo.value() == 1:
        sigon = utime.ticks_us()
        #print('on:', sigon)
    dist = (sigon - sigoff) * s_speed / 2 * (10 ** -4)
    return dist

#サーボモーターで使う関数群
def pulse_width(val, freq = PWM_FREQ, resol = 65535):
    pulse = freq * val * 1e-6 * resol
    return int(pulse)

def rotmotor(pulse):
    duty = pulse_width(pulse)
    servo.duty_u16(duty)
    #utime.sleep(1)
    
def cnvDeg(dist):
    if dist < 5:
         dist = 5
    if dist > 105:
         dist = 105
    degrees = 1.8 * dist - 99 
    return degrees

def cnvPulse(degrees):
    if degrees < -90:
         degrees = -90
    if degrees > 90:
         degrees = 90
    return -degrees*1000/90+1500

servo = PWM(Pin(SERVO_PIN))
servo.freq(PWM_FREQ)


#メイン処理

while True:
    distance = measure()
    
    deg = cnvDeg(distance)
    pulse = cnvPulse(deg)
    rotmotor(pulse)
    print(distance, deg)
    utime.sleep(0.2)

