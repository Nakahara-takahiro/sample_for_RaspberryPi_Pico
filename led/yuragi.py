from machine import Pin, PWM
import utime, random

pwm_g = PWM(Pin(11))
pwm_b = PWM(Pin(12))

pwm_g.freq(100)
pwm_b.freq(100)
x=0.5

while True:
    if 0.05 <= x < 0.5:
        x = x + 2*x*x
    elif 0.5 <= x < 0.95:
        x = x - 2*(1-x)*(1-x)
    else:
        x = random.random()
    pwm_g.duty_u16(int(65535*x))
    pwm_b.duty_u16(int(65535*(1-x)))
    
    utime.sleep(0.2)
    print(x, 1-x)