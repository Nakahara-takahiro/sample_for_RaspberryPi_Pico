
import random
from machine import Pin
import time

pin_no = [13, 18, 14, 19, 17 ,15, 16]

leds = [Pin(pin_no[i], Pin.OUT) for i in range(7)]

#1～6の数字に対応した目を配列で指定する
POINT_NUM =[[0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 1],
            [1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1, 1]]
#プログラムで使う関数を定義（はじまり）///////////////////////////////////////////////////////

def blinkLED(num, pattern):
    for i in range(7):
        leds[i].value(0)
    print(pattern[num-1])
    for i in range(7):
        leds[i].value(pattern[num-1][i])

# ボタンが押された時の処理をする関数
def dice():
    # ランダムな整数を生成して、表示する
    num = random.randint(1,6)
    print('num:',num)
    blinkLED(num, POINT_NUM)
#プログラムで使う関数を定義（おわり）/////////////////////////////////////////////////////////


while True :
    print(leds)
    dice()
    time.sleep(2)
