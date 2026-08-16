import machine
import utime
from machine import Pin, PWM

#LEDの設定
pwm = PWM(Pin(25))
pwm.freq(1000)

#温度計の設定
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor

    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    
    if temperature < 26 : #25℃未満のとき
        duty = int(255/2) #50%の明るさ
        
    else:                 #25℃以上のとき
        duty = int(255)   #100%の明るさ

    pwm.duty_u16(duty * duty)   
    
    utime.sleep(3)




for i in range(10):
    print(i)
