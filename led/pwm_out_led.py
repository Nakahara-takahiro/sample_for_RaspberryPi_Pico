import time
from machine import Pin, PWM

pwm_r = PWM(Pin(19)) #red
pwm_g = PWM(Pin(11)) #green
pwm_b = PWM(Pin(12)) #blue

pwm_r.freq(1000)
pwm_g.freq(1000)
pwm_b.freq(1000)

duty = 0
direction = 1
for _ in range(8 * 256):
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm_r.duty_u16(duty * duty)
    pwm_g.duty_u16(duty * duty)
    pwm_b.duty_u16(duty * duty)
        
    time.sleep(0.007)