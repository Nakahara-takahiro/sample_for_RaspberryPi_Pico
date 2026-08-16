from machine import Pin, PWM
import  time

import rotenc

def zero2hex(target, num):
    target += num
    if target <= 0:
        target = 0
    if target >= 16:
        target =16
    return  target
    
#タクトスイッチの設定
SW_PIN_R, SW_PIN_G, SW_PIN_B = 6, 11, 8

sw_r = Pin(SW_PIN_R, Pin.IN, Pin.PULL_DOWN)
sw_g = Pin(SW_PIN_G, Pin.IN, Pin.PULL_DOWN)
sw_b = Pin(SW_PIN_B, Pin.IN, Pin.PULL_DOWN)

#カラーLEDの設定
RED_PIN, GREEN_PIN, BLUE_PIN = 15, 18, 12
LED_FREQ = 1000

led_r = PWM(Pin(RED_PIN))
led_g = PWM(Pin(GREEN_PIN))
led_b = PWM(Pin(BLUE_PIN))

led_r.freq(LED_FREQ)
led_g.freq(LED_FREQ)
led_b.freq(LED_FREQ)

r_retio, g_retio, b_retio = 1, 1, 1

#メインプログラム
rv = rotenc.RotVolume(2, 1)

while True:
    led_r.duty_u16(256*16*r_retio)
    led_g.duty_u16(256*16*g_retio)
    led_b.duty_u16(256*16*b_retio)

    #ロータリーエンコーダーで明るさ設定値をRGBそれぞれ変更
    pos = rv.putCount()
    
    if pos is not None:
        print(pos, type(pos))
        if sw_r.value()==1:
            r_retio = zero2hex(r_retio, pos)
        if sw_g.value()==1:
            g_retio = zero2hex(g_retio, pos)
        if sw_b.value()==1:
            b_retio = zero2hex(b_retio, pos)
    #print(r_retio, g_retio, b_retio)
