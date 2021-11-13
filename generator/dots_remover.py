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

for_size = (len(_xy)//3)*3
print(for_size)
__xy = []
for i in range(0, for_size, 3):
    a = _xy[i]
    b = _xy[i+1]
    c = _xy[i+2]
    __xy += [((a[0]+b[0]+c[0])/3, (a[1]+b[1]+c[1])/3)]


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