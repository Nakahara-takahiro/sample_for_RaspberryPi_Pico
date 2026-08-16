from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

WIDTH = 128
HEIGHT = 64

i2c = I2C(0)
i2c.scan()

print('i2c address      : '+hex(i2c.scan()[0]).upper())
print('i2c configuration: '+str(I2C))

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)

oled.text('Raspberry Pi', 5, 5)
oled.text('Pico', 5, 15)

oled.show()