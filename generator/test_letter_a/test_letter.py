import random
from PIL import Image, ImageDraw

wanna_dots = 29903

let_a = Image.open("../../images/a2.png", "r")

im = Image.new('RGB', (15000,15000), (255,255,255))
draw = ImageDraw.Draw(im)
_xy = []
f = open("dots3.txt", "r")
for l in f.readlines():
    _xy += [tuple(map(float, l.split(' ')[:2]))]

print("Parsed points: {0}".format(len(_xy)))
for _ in range(len(_xy)-wanna_dots):
    _xy.pop(random.randint(0, len(_xy)-1))
print("Removed other points, len now: {0}".format(len(_xy)))

# __xy = []

# for i in range(0,len(_xy)):
#     if i % 3 == 0:
#         __xy += _xy[i]


# draw.point(
#     xy= _xy,
#     fill='black'
# )

for (x,y) in _xy:
    offset = (int(x*2),int(y*2))
    im.paste(let_a, offset, mask=let_a)


# r = 2
# for x, y in _xy:
#     temp = (x-r,y-r,x+r,y+r)
#     draw.rectangle(xy=temp, fill='red')

# print(_xy)
# im.show()
im.save('result_letter_a.png', quality=95)