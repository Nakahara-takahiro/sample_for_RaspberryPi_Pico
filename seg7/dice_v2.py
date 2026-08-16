import random
from machine import Pin
import utime

# サイコロの目LED
pin_no = [13, 18, 14, 19, 17, 15, 16]
leds = [Pin(pin_no[i], Pin.OUT) for i in range(7)]

# サイコロスタートスイッチ
start_btn = Pin(12, Pin.IN, Pin.PULL_UP)

# 1～6の数字に対応した目を配列で指定する
POINT_NUM = [[0, 0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 1],
             [1, 1, 0, 0, 0, 1, 1],
             [1, 1, 0, 1, 0, 1, 1],
             [1, 1, 1, 0, 1, 1, 1]]

# ★改良①：フラグ変数とチャタリング対策用の時間記録
dice_triggered = False
last_press_time = 0

# ---------- 関数定義 ----------

# サイコロの目をLEDで表示する関数
def blinkDice(num, pattern):
    for i in range(7):
        leds[i].value(0)
    for i in range(7):
        leds[i].value(pattern[num - 1][i])

# ★改良③：サイコロの目のパターンからランダムに選ぶ（本物らしい演出）
def randomDice():
    num = random.randint(1, 6)
    blinkDice(num, POINT_NUM)
    utime.sleep(0.1)

# ランダムな整数を生成して最終表示する関数
def dice():
    num = random.randint(1, 6)
    print('num:', num)
    blinkDice(num, POINT_NUM)

# ★改良②：IRQハンドラを軽量化（フラグを立てるだけ）
def startDice(p):
    global dice_triggered, last_press_time
    now = utime.ticks_ms()
    # チャタリング対策：前回から300ms以内の割り込みは無視
    if utime.ticks_diff(now, last_press_time) < 300:
        return
    last_press_time = now
    dice_triggered = True

# ---------- 割り込み設定 ----------
start_btn.irq(trigger=Pin.IRQ_FALLING, handler=startDice)

# ---------- メインループ ----------
while True:
    if dice_triggered:
        dice_triggered = False
        for _ in range(20):
            randomDice()
        dice()