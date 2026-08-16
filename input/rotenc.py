from machine import Pin
import time

ROT_A_PIN = 0
ROT_B_PIN = 1

sw_a = Pin(ROT_A_PIN, Pin.IN, Pin.PULL_UP)
sw_b = Pin(ROT_B_PIN, Pin.IN, Pin.PULL_UP)

count = 0

b_a = 1
b_b = 1
buf = [0, 0, 0, 0]

while True:
    flag = 0
    a = sw_a.value()
    b = sw_b.value()
    time.sleep(0.001)
    
    if b_a != a or b_b != b:
        del buf[0]
        buf.append(b_a*8 + b_b*4 + a*2 + b)
        b_a = a
        b_b = b
        if buf == [0b1101, 0b0100, 0b0010, 0b1011]:
            count += 1
            flag = 1
        if buf == [0b1110, 0b1000, 0b0001, 0b0111]:
            count -= 1
            flag = 1
    if flag == 1:
        print('Count:{} Angle:{}'.format(count, count*15))
        