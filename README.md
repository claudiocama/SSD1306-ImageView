# SSD1306-ImageView
Image viewer function for SSD1306 library (MicroPython)
Use this library to compress images and view them on any oled compatible with the [SSD1306 library](https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py)

## The compression algorithm
The compression algorithm is extremely simple, but still very efficient.
Turn a list of pixels (their color) into a list of [pixel color, number of repetitions]
Ex. [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0] -> [0, 5, 1, 3, 0, 5]
