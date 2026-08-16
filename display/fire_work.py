from machine import Pin, I2C
import ssd1306
import time
import urandom
import math

# I2C初期化
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)

# SSD1306 初期化 (128x64 の例)
oled = ssd1306.SSD1306_I2C(width=128, height=64, i2c=i2c)

# 画面の中心座標
cx = 128 // 2
cy = 64 // 2

while True:
    # 花火の角度をランダムに決める（8～16方向）
    num_lines = urandom.getrandbits(3) + 8
    angles = [i * (2*math.pi/num_lines) for i in range(num_lines)]

    # 外周に向けて伸びるアニメーション
    for length in range(5, 35, 3):  # 5～35まで徐々に伸ばす
        oled.fill(0)
        for ang in angles:
            x = int(cx + length * math.cos(ang))
            y = int(cy + length * math.sin(ang))
            oled.line(cx, cy, x, y, 1)
        oled.show()
        time.sleep(0.05)

    # 花火が消えるまでの余韻
    time.sleep(0.2)
    oled.fill(0)
    oled.show()
    time.sleep(0.3)
