import random
from PIL import Image, ImageDraw

wanna_dots = 29903

im = Image.new('RGB', (2200,2200), (255,255,255))
draw = ImageDraw.Draw(im)
_xy = []
f = open("dots.txt", "r")
for l in f.readlines():
    _xy += [tuple(map(float, l.split(' ')[:2]))]

print("Parsed points: {0}".format(len(_xy)))
# for _ in range(len(_xy)-wanna_dots):
#     _xy.pop(random.randint(0, len(_xy)-1))

__xy = []

for i in range(0,len(_xy)):
    if i % 3 == 0:
        __xy += _xy[i]


draw.point(
    xy= __xy,
    fill='black'
)
# r = 2
# for x, y in _xy:
#     temp = (x-r,y-r,x+r,y+r)
#     draw.rectangle(xy=temp, fill='red')

# print(_xy)
im.show()
im.save('dots_remover_result.png', quality=95)