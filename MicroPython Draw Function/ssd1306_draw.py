import machine, ssd1306

def draw(pixel_list, oled_obj, top=0, left=0, height=64, weight=128):
  counter = 0
  color = pixel_list[0]
  color_counter = 2
  counter_counter = 1
  for i in range(top, height):
    for j in range(left, weight):
      oled_obj.pixel(j, i, color)
      counter += 1
      if counter == pixel_list[counter_counter]:
        counter = 0
        color = pixel_list[color_counter]
        if counter_counter != len(pixel_list)-2 and counter_counter != len(pixel_list)-3:
          counter_counter += 2
          color_counter += 2
