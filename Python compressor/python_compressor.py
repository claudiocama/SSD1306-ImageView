from PIL import Image

IMAGE_NAME = ""

im = Image.open(IMAGE_NAME)
im = im.convert("1") #convert to black and white
pixa = list(im.getdata()) #get list of pixels
###IMAGE COMPRESSION###
counter = 0
color = 0
ret = []
total = 0
if pixa[0] == 255:
    color = 1
else:
    color = 0
counter += 1
for x in pixa[1:]:
    if x == 255 and color == 1:
        counter += 1
    if x == 255 and color == 0:
        ret.append(color)
        ret.append(counter)
        color = 1
        counter = 1
    if x == 0 and color == 0:
        counter += 1
    if x == 0 and color == 1:
        ret.append(color)
        ret.append(counter)
        color = 0
        counter = 1

for i in range(1, len(ret), 2):
    total += ret[i]

ret.append(color)
ret.append(len(pixa)-total)
######
print("Successfully compressed image:")
print(ret)
