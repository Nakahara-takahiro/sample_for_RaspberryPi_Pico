# sample_for_RaspberryPi_Pico
RaspberryPi Pico用のサンプルプログラム

# 使い方
* 用途ごとのディレクトリにサンプルプログラムを入れています。
* プログラミングクラブの説明用として作ったプログラムです。
* RaspberryPi PicoをMicroPythonで動かす前提です。
* Thonnyなどのエディタで Pico に転送して実行してください。
* OLED（SSD1306）を使うプログラムは、Pico側に `ssd1306.py` を入れておく必要があります。

# ディレクトリの説明
| ディレクトリ | 説明 |
|---------|--------|
|led|LEDの点灯・点滅・PWM調光、フルカラーLED（WS2812B）、LEDマトリクス|
|seg7|7セグメントLED・LED7個を使ったサイコロ|
|display|OLED（SSD1306）を使った表示。花火アニメーション、反射神経ゲームなど|
|sensor|温度センサー、超音波距離センサー|
|motor|サーボモーター、DCモーター、フルブリッジ駆動|
|input|スイッチ、キーパッド、ロータリーエンコーダ|
|rgbled|カラーLEDの調色。回路図（drawio / svg）付き|
|lib|外部ライブラリ（SDカードドライバなど）|

# 主なサンプルプログラム
| ファイル | 説明 |
|---------|--------|
|led/first_led.py|一番はじめに動かすLED点灯プログラム|
|led/color_sample.py|色の三原色を説明するために、WS2812Bで動かしながら説明するプログラム|
|led/yuragi.py|ロウソクのようにLEDをゆらがせるプログラム|
|led/leds_matrix64.py|8×8のLEDマトリクスを光らせるプログラム|
|seg7/dice.py|LED7個をサイコロのように表示させるプログラム|
|seg7/dice_v2.py|サイコロプログラムの改良版|
|display/fire_work.py|OLEDに花火のアニメーションを表示するプログラム|
|display/reaction_game.py|OLEDを使った反射神経ゲーム|
|sensor/temperature.py|Pico内蔵の温度センサーを読むプログラム|
|sensor/us_length.py|超音波センサーで距離を測るプログラム|
|motor/servo.py|サーボモーターを動かすプログラム|
|input/rotenc.py|ロータリーエンコーダの回転を読むプログラム|
|input/keypad.py|4×4キーパッドの入力を読むプログラム|

# ライセンス
ライセンスについてはLICENSE参照のこと
