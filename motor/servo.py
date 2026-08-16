from machine import Pin, PWM
import time

SERVO_PIN = 16
PWM_FREQ = 50

def pulse_width(val, freq = PWM_FREQ, resol = 65535):
    pulse = freq * val * 1e-6 * resol
    return int(pulse)

def rotmotor(pulse):
    duty = pulse_width(pulse)
    servo.duty_u16(duty)
    time.sleep(1)

def cnvPulse(degrees):
    if degrees < -90:
         degrees = -90
    if degrees > 90:
         degrees = 90
    return -degrees*1000/90+1500

servo = PWM(Pin(SERVO_PIN))
servo.freq(PWM_FREQ)

degrees = [0, 90, 0, -90]

while True:
    for deg in degrees:
        pulse = cnvPulse(deg)
        rotmotor(pulse)
