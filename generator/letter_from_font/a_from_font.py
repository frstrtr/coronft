import random
import math
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import ImageFont, truetype


im = Image.new('RGB', (100,100), (255,255,255))
draw = ImageDraw.Draw(im)


_im = Image.open("T25.png")
rgb = _im.convert("RGB")
points = []
for n in range(25):
    for m in range(25):
        if rgb.getpixel((n,m)) == (0,0,0):
            points += [(n,m)]
            
draw.point(
    xy= points,
    fill='blue'
)

print(len(points))
# print(_xy)
im.show()