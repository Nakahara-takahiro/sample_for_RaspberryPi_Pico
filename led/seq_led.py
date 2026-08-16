import machine
import time

# ピンアサイン
btn = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_UP)
led_pins = [12, 13, 14, 15]
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

# 点灯順「青→赤→黄→緑→黄→赤→青」
seq = [
    (1,0,0,0), # 青
    (0,1,0,0), # 赤
    (0,0,1,0), # 黄
    (0,0,0,1), # 緑
    (0,0,1,0), # 黄
    (0,1,0,0)  # 赤   
]

def set_leds(state):
    for led, val in zip(leds, state):
        led.value(val)

def all_on(): set_leds((1,1,1,1))
def all_off(): set_leds((0,0,0,0))

def wait_btn_press():
    while btn.value(): time.sleep_ms(1)
    time.sleep_ms(20) # チャタ防止
    while not btn.value(): time.sleep_ms(1)
    time.sleep_ms(20)

while True:
    # 初期化：全点灯
    all_on()
    wait_btn_press()   # タクトスイッチ押下で点灯順モードへ

    idx = 0
    while True:
        set_leds(seq[idx])
        idx = (idx+1) % len(seq)
        # ボタン押しで消灯+2秒待ち
        for _ in range(10): # 約0.1秒点灯
            if not btn.value():
                wait_btn_press()
                all_off()
                time.sleep(2)
                break
            time.sleep(0.01)
        else:
            continue
        break