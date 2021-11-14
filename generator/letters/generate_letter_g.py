import random
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import ImageFont, truetype

wanna_dots = 50

covid = Image.open("/home/sl33n/coronft/generator/letters/covid_alpha.png", "r").convert("RGBA")
covid = covid.resize((260,260), Image.ANTIALIAS)

im = Image.new('RGB', (4000,4000), (255,255,255))
draw = ImageDraw.Draw(im)
_xy = []

# f = open("result/dots_inside.txt", "r")
f = open("result/dots_contour.txt", "r")
for l in f.readlines():
    _xy += [tuple(map(float, l.split(' ')[:2]))]
f.close()
print("Parsed points: {0}".format(len(_xy)))

# f = open("result/dots_contour.txt", "r")
# for l in f.readlines():
#     contour = tuple(map(float, l.split(' ')[:2]))
#     _xy.remove(contour)
# f.close()



# for _ in range(len(_xy)-wanna_dots):
#     index = random.randint(0, len(_xy)-1)
#     while _xy[index] in contour:
#         index = random.randint(0, len(_xy)-1)
#     _xy.pop(index)
# print("Removed other points, len now: {0}".format(len(_xy)))

# __xy = []

# for i in range(0,len(_xy)):
#     if i % 3 == 0:
#         __xy += _xy[i]


# draw.point(
#     xy= _xy,
#     fill='black'
# )

# im.paste(covid, (0,0), mask=covid)
for (x,y) in _xy:
    offset = (int(x),int(y))
    im.paste(covid, offset, mask=covid)


#for debug coords:
# index = 1
# for (x,y) in _xy:
#     offset = (int(x),int(y))
#     draw.text(offset, str(index), fill="blue", size=260)
#     index += 1

# r = 2
# for x, y in _xy:
#     temp = (x-r,y-r,x+r,y+r)
#     draw.rectangle(xy=temp, fill='red')

# print(_xy)
# im.show()
im.save('result/letter.png', quality=95)