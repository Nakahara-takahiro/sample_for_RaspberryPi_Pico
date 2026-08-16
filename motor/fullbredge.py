import machine
import time
from machine import PWM
import utime


class motor:
    '''forward rotationreversal'''
    def __init__(self, p1sw, p2sw, n1sw, n2sw):
        '''pwm1swとn2swがクロスでペア、pwm2swとn1swがクロスでペア'''
        #正転のためのスイッチ(forward rotation)
        self.FRotP = PWM(machine.Pin(p1sw, machine.Pin.OUT))#起点方向
        self.FRotN = machine.Pin(n2sw, machine.Pin.OUT)
        self.FRotP.freq(1000)

        #逆転のためのスイッチ(reversal rotation)
        self.RRotP = PWM(machine.Pin(p2sw, machine.Pin.OUT))
        self.RRotN = machine.Pin(n1sw, machine.Pin.OUT)
        self.RRotP.freq(1000)

    def rotfor(self):
        '''モーターを正転させる処理'''
        self.RRotP.value(1)
        self.RRotN.value(0)
        time.sleep(1)
        self.FRotP.value(0)
        self.FRotN.value(1)
        print('cw',speed_setting)

    def rotrev(self):
        '''モーターを逆転させる処理'''
        self.FRotP.value(1)
        self.FRotN.value(0)
        time.sleep(1)
        self.RRotP.value(0)
        self.RRotN.value(1)
        print('ccw',speed_setting)
    
    def rotstop(self):
        '''モーターを停止させる処理'''
        self.FRotP.value(1)
        self.FRotN.value(0)
        self.RRotP.value(1)
        self.RRotN.value(0)
        print('stopping')

if __name__ == '__main__':
    mainmotor=motor(21, 20, 18, 19)
    
    motor.rotfor('high')
    time.sleep(2)
    motor.rotrev('high')
    time.sleep(2)
    motor.rotstop()