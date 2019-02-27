import ssd1306_draw

OLED_HEIGHT = 64
OLED_WEIGHT = 128
PIN_SCL = 14
PIN_SDA = 27

i2c = machine.I2C(scl=machine.Pin(PIN_SCL), sda=machine.Pin(PIN_SDA))
oled = ssd1306.SSD1306_I2C(OLED_WEIGHT, OLED_HEIGHT, i2c, 0x3c)
oled.fill(0)
draw([1, 30, 0, 50], oled)
oled.show()
