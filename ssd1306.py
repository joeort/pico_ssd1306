import machine
import utime
import framebuf
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=200000)
oled = SSD1306_I2C(128, 32, i2c, addr=0x3C)

# Raspberry Pi logo as 32x32 bytearray
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# Load the raspberry pi logo into the framebuffer (the image is 32x32)
fb = framebuf.FrameBuffer(buffer, 32, 46, framebuf.MONO_HLSB)

while True:
    # Clear the oled display in case it has junk on it.
    oled.fill(0)

    # Blit the image from the framebuffer to the oled display
    oled.blit(fb, 0, 0)


    # Finally update the oled display so the image & text is displayed
    oled.show()
    utime.sleep(1)
 