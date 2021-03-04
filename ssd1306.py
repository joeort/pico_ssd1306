import machine
import utime
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=200000)
oled = SSD1306_I2C(128, 32, i2c, addr=0x3C)

while True:
    for i in range(-45,140, 1):
        oled.fill(0)
        oled.text('Hello', i, 8)
        oled.text('World', i, 18)
        oled.show()
        utime.sleep_ms(30)
        we