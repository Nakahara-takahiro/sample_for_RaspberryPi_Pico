import random
from machine import Pin
import utime

#サイコロの目LED（VCC共通配線：ピンがLow(0)で点灯、High(1)で消灯）
pin_no = [15, 13, 18, 14]
leds = [Pin(pin_no[i], Pin.OUT) for i in range(4)]

#サイコロスタートスイッチ（ONでVCCと接続：押すとHigh(1)、押していない間はLow(0)）
start_btn = Pin(12, Pin.IN, Pin.PULL_DOWN)

#プログラムで使う関数を定義（はじまり）///////////////////////////////////////////////////////
#サイコロの目をLEDで表示する関数
def blinkDice(num):
    #1～6の数字に対応した目を配列で指定する（1=点灯、0=消灯）
    POINT_NUM =[[1, 0, 0, 0],
                [0, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 1, 0],
                [1, 1, 1, 0],
                [0, 1, 1, 1]]

    #VCC共通なので、全部消灯(1)にしてから、点灯するLEDだけ0にする
    for i in range(4):
        leds[i].value(1)
    for i in range(4):
        #点灯(1)のときピンを0、消灯(0)のときピンを1にする
        leds[i].value(1 - POINT_NUM[num-1][i])

# ボタンが押された時の処理をする関数
def dice():
    # ランダムな整数を生成して、表示する
    num = random.randint(1,6)
    print('num:',num)
    blinkDice(num)

#プログラムで使う関数を定義（おわり）/////////////////////////////////////////////////////////


while True :
    #タクトスイッチのポーリング
    if start_btn.value() == 1:
        #ランダムにサイコロの目を表示する
        for _ in range(20):
            dice()
            utime.sleep(0.1)
        #サイコロの目を確定する
        dice()
    utime.sleep(0.1)
