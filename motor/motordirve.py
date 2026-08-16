import utime
from machine import PWM, Pin
class motorDrv:
    #DRV8835モータードライバを使ったときの制御用

    def __init__(self, ain1, ain2):
        
        #正転のためのスイッチ(forward rotation)
        self.pwm_ain1 = PWM(Pin(ain1, Pin.OUT), freq=1000)
        self.pwm_ain2 = PWM(Pin(ain2, Pin.OUT), freq=1000)
        
        #速度設定 100%=65535
        #lowが小さいとモーターが起動しない high:100%, low:60%, stop:0%
        self.speed = {'high':100, 'low':100, 'stop':0}
        
    def rotfor(self, speed_setting:str):
        '''モーターを正転させる処理'''
        self.pwm_ain2.duty_u16(0)
        self.pwm_ain1.duty_u16(int(self.speed[speed_setting]/100*65535))
        print('cw',speed_setting, self.speed[speed_setting]/100*65535)

    def rotrev(self, speed_setting:str):
        '''モーターを逆転させる処理'''
        #逆転のときは、デューティー比20％アップ
        self.pwm_ain1.duty_u16(0)
        self.pwm_ain2.duty_u16(int((self.speed[speed_setting])/100*65535))
        print('ccw',speed_setting, (self.speed[speed_setting])/100*65535)
    
    def rotstop(self):
        '''モーターを停止させる処理'''
        self.pwm_ain1.duty_u16(0)
        self.pwm_ain2.duty_u16(0)
        print('stopping')

ITV_TIME = 2
if __name__ == '__main__':
    mainmotor = motorDrv(18, 19)
    mainmotor.rotstop()
    
    while True :
        mainmotor.rotrev('low')
        utime.sleep(ITV_TIME)
        mainmotor.rotrev('high')
        utime.sleep(ITV_TIME)
        mainmotor.rotstop()
        utime.sleep(ITV_TIME)
        
        mainmotor.rotfor('low')
        utime.sleep(ITV_TIME)
        mainmotor.rotfor('high')
        utime.sleep(ITV_TIME)
        mainmotor.rotstop()
        utime.sleep(ITV_TIME)
    
    