import time
from machine import Pin, I2C#←
from ssd1306 import SSD1306_I2C#←

IN_PIN = [19, 20, 21, 22]#←自分の配線にあわせること
SEL_PIN = [16, 17, 18]#←自分の配線にあわせること

KEY_MAP =[[ '.','7','4','1'],
          [ '0','8','5','2'],
          [ '\n','9','6','3']]

sel_sw = []
in_sw = []

i = 0
while i < len(SEL_PIN):
    sel_sw.append(Pin(SEL_PIN[i], Pin.OUT))
    sel_sw[i].value(1)
    i += 1

i = 0
while i < len(IN_PIN):
    in_sw.append(Pin(IN_PIN[i], Pin.IN))
    i += 1

keybuf = []

def keypad():
    global keybuf
    fg_in = 0
    i = 0
    while i < len(SEL_PIN):
        sel_sw[i].value(0)
        j = 0
        while j < len(IN_PIN):
            if in_sw[j].value() == 0:
                keybuf.append(KEY_MAP[i][j])
                fg_in = 1
                while in_sw[j].value()==0:
                    time.sleep(0.05)
            j += 1
        sel_sw[i].value(1)
        i += 1
    return fg_in

def bufread():
    global keybuf
    buf = ''
    i = 0
    point = 0
    while i < len(keybuf):
        if keybuf[i] == '\n':
            break
        elif keybuf[i] == '.':
            point += 1
            if point >1:
                break
            else:
                buf += keybuf[i]
        else:
            buf += keybuf[i]
        i += 1
    
    keybuf = []
    return str(buf)#←

WIDTH = 128#←
HEIGHT = 64#←

i2c = I2C(0)#←
i2c.scan()#←

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)#←

while True:
    f = keypad()
    if f==1:
        if keybuf.count('\n') >= 0:
            value = bufread()
            print(value)
            oled.fill(0)#←
            oled.text(value, 5, 5)#←
            oled.show()#←
