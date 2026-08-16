import machine
import neopixel
import time
import _thread

# ハードウェア設定
PIN_CONFIG = {
    "LED_PIN": 17,       # WS2812B接続GPIO番号
    "BUTTON_PIN": 15,    # タクトスイッチ接続GPIO番号
    "NUM_LEDS": 4,      # LEDの数
}

# 色の定義
COLORS = {
    "RED": (128, 0, 0),    
    "GREEN": (0, 128, 0),  
    "BLUE": (0, 0, 128),
    "YELLOW": (128, 128, 0),
    "CYAN": (0, 128, 128),
    "MAGENTA": (128, 0, 128),
    "WHITE": (128, 128, 128),
    "OFF": (0, 0, 0)      # 消灯
}

# 色の順序リスト
COLOR_SEQUENCE = ["RED", "GREEN", "BLUE", "YELLOW", "CYAN", "MAGENTA", "WHITE", "OFF"]

class WS2812BController:
    def __init__(self):
        # NeoPixelの初期化
        self.np = neopixel.NeoPixel(machine.Pin(PIN_CONFIG["LED_PIN"]), PIN_CONFIG["NUM_LEDS"])
        
        # タクトスイッチの初期化（プルアップ抵抗を有効）
        self.button = machine.Pin(PIN_CONFIG["BUTTON_PIN"], machine.Pin.IN, machine.Pin.PULL_UP)
        
        # 現在の色インデックス
        self.current_color_index = 0
        
        # チャタリング防止用変数
        self.last_button_time = 0
        self.debounce_time = 200  # 200ms
        self.last_button_state = 1  # プルアップなので初期値は1（HIGH）
        
        # 初期状態で最初の色を設定
        self.set_color(COLOR_SEQUENCE[self.current_color_index])
        
        print("WS2812B Controller initialized")
        print("Press the button to change colors!")
        
    def set_color(self, color_name):
        """指定した色でLEDを点灯"""
        color = COLORS[color_name]
        for i in range(PIN_CONFIG["NUM_LEDS"]):
            self.np[i] = color
        self.np.write()
        print(f"Color changed to: {color_name} {color}")
    
    def debounce_button(self):
        """チャタリング防止付きボタン読み取り"""
        current_time = time.ticks_ms()
        current_state = self.button.value()
        
        # ボタンが押された瞬間を検出（HIGH→LOWの変化）
        if (self.last_button_state == 1 and current_state == 0):
            # デバウンス時間チェック
            if time.ticks_diff(current_time, self.last_button_time) > self.debounce_time:
                self.last_button_time = current_time
                self.last_button_state = current_state
                return True
        
        self.last_button_state = current_state
        return False
    
    def next_color(self):
        """次の色に変更"""
        self.current_color_index = (self.current_color_index + 1) % len(COLOR_SEQUENCE)
        self.set_color(COLOR_SEQUENCE[self.current_color_index])
    
    def run(self):
        """メインループ"""
        try:
            while True:
                if self.debounce_button():
                    self.next_color()
                time.sleep_ms(10)  # CPU負荷軽減のため短い待機
                
        except KeyboardInterrupt:
            print("\nProgram interrupted")
            # 全LEDを消灯
            self.set_color("OFF")
            print("All LEDs turned off")

# メイン実行部
if __name__ == "__main__":
    try:
        controller = WS2812BController()
        controller.run()
    except Exception as e:
        print(f"Error: {e}")
        # エラー時も全LEDを消灯
        np = neopixel.NeoPixel(machine.Pin(PIN_CONFIG["LED_PIN"]), PIN_CONFIG["NUM_LEDS"])
        for i in range(PIN_CONFIG["NUM_LEDS"]):
            np[i] = (0, 0, 0)
        np.write()
        print("All LEDs turned off due to error")