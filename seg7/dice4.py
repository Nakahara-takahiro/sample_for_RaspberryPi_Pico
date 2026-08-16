import random
from machine import Pin
import utime

#サイコロの目LED
pin_no = [13, 18, 14, 19, 17 ,15, 16]
leds = [Pin(pin_no[i], Pin.OUT) for i in range(7)]

#サイコロスタートスイッチ
start_btn = Pin(12, Pin.IN, Pin.PULL_UP)

#1～6の数字に対応した目を配列で指定する
POINT_NUM =[[0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 1],
            [1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1, 1]]

#プログラムで使う関数を定義（はじまり）///////////////////////////////////////////////////////
#サイコロの目をLEDで表示する関数
def blinkDice(num, pattern):
    for i in range(7):
        leds[i].value(0)
    #print(pattern[num-1])
    for i in range(7):
        leds[i].value(pattern[num-1][i])

#ランダムにサイコロの目を表示する関数
def randomDice():
    random_list = [random.choice([0, 1]) for _ in range(7)]
    for i in range(7):
        leds[i].value(random_list[i])
    utime.sleep(0.1)
    
# ボタンが押された時の処理をする関数
def dice():
    # ランダムな整数を生成して、表示する
    num = random.randint(1,6)
    print('num:',num)
    blinkDice(num, POINT_NUM)
    
def startDice(p):
    for _ in range(20):
        randomDice()
    dice()
    
#プログラムで使う関数を定義（おわり）/////////////////////////////////////////////////////////
'''
while True :
    start_btn.irq(trigger = Pin.IRQ_FALLING, handler=startDice)
'''
start_btn.irq(trigger = Pin.IRQ_FALLING, handler=startDice)