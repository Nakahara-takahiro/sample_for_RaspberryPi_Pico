from machine import Pin
import time


class RotVolume:

    def __init__(self, ROT_A_PIN, ROT_B_PIN):
        #ロータリーエンコーダーはGPIO1とGPIO2に接続を想定
        #ROT_A_PIN = 1
        #ROT_B_PIN = 2
        self.sw_a = Pin(ROT_A_PIN, Pin.IN, Pin.PULL_UP)
        self.sw_b = Pin(ROT_B_PIN, Pin.IN, Pin.PULL_UP)
        
        self.count = 0
        self.b_a = 1
        self.b_b = 1
        self.buf = [0, 0, 0, 0]

    def putCount(self):
        #時計回りで1、反時計回りでマイナス1を返す
        self.flag = 0
        time.sleep(0.001)
        
        if self.b_a != self.sw_a.value() or self.b_b != self.sw_b.value():
            del self.buf[0]
            self.buf.append(self.b_a*8 + self.b_b*4 + self.sw_a.value()*2 + self.sw_b.value())
            self.b_a = self.sw_a.value()
            self.b_b = self.sw_b.value()

            if self.buf == [0b1101, 0b0100, 0b0010, 0b1011]:
                self.flag = 1
                return 1
            if self.buf == [0b1110, 0b1000, 0b0001, 0b0111]:
                self.flag = 1
                return -1

if __name__ == '__main__':
    rv = RotVolume(2, 1)
    
    while True:
        pos = rv.putCount()
        if pos is not None:
            print(pos)
        