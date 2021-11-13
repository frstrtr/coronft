import random
from PIL import Image, ImageDraw

wanna_dots = 29903

im = Image.new('RGB', (2200,2200), (255,255,255))
draw = ImageDraw.Draw(im)
_xy = []
f = open("dots.txt", "r")
for l in f.readlines():
    _xy += [tuple(map(float, l.split(' ')[:2]))]

for _ in range(len(_xy)-wanna_dots):
    _xy.pop(random.randint(0, len(_xy)))

draw.point(
    xy= _xy,
    fill='black'
)
# print(_xy)
im.show()
im.save('dots_remover_result.png', quality=95)