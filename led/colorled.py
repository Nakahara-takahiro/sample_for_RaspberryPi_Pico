from machine import Pin, PWM

RED_PIN = 15
GREEN_PIN = 18
BLUE_PIN = 12

RED  = 10000
GREEN =60000
BLUE = 12428

led_r = PWM(Pin(RED_PIN))
led_g = PWM(Pin(GREEN_PIN))
led_b = PWM(Pin(BLUE_PIN))

led_r.freq(50)
led_g.freq(50)
led_b.freq(50)

led_r.duty_u16(RED)
led_g.duty_u16(GREEN)
led_b.duty_u16(BLUE)