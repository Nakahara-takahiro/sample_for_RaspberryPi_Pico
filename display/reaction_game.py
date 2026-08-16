from machine import Pin, I2C
import ssd1306
import time
import random

# I2C初期化
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# LEDとボタンの設定
led = Pin(14, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    oled.fill(0)
    oled.text("Reaction Timer", 10, 10)
    oled.text("Wait for 'GO!'", 10, 30)
    oled.show()

    time.sleep(random.uniform(1, 4))  # ランダム待ち時間

    oled.fill(0)
    oled.text("GO!", 50, 20)
    oled.show()
    led.value(1)  # GO!時にLED点灯

    start_time = time.ticks_ms()
    while not button.value():
        pass
    reaction = time.ticks_diff(time.ticks_ms(), start_time)
    led.value(0)

    oled.fill(0)
    oled.text("Time:", 10, 20)
    oled.text(str(reaction) + " ms", 10, 40)
    oled.show()

    time.sleep(2)
