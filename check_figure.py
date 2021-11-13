from PIL import Image, ImageDraw

im = Image.new('RGB', (2200,2200), (255,255,255))
draw = ImageDraw.Draw(im)
_xy = []
f = open("/home/sl33n/coronft/freefem_tests/xyf.txt", "r")
for l in f.readlines():
    _xy += [tuple(map(float, l.split(' ')[:2]))]

draw.point(
    xy= _xy,
    fill='black'
)
# print(_xy)
im.show()
im.save('check_figure.png', quality=95)