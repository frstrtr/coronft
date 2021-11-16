import random
import math
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import ImageFont, truetype

wanna_dots = 60

result_path = "result/copy/"
    
covid = Image.open("/home/sl33n/coronft/generator/letters/covid_alpha.png", "r").convert("RGBA")
covid_size = 125
covid = covid.resize((covid_size, covid_size), Image.ANTIALIAS)

def dist(a,b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def point_in_covid(x, y, xc, yc):
    # return (if (math.xc))
    # return (True if (math.sqrt((xc-x)**2 + (yc-y)**2) < covid_size*2) else False)
    return (True if dist((x,y), (xc,yc)) < covid_size else False)

im = Image.new('RGB', (4000,4000), (255,255,255))
draw = ImageDraw.Draw(im)
_xy = []

# f = open("result/dots_inside.txt", "r")
f = open(result_path + "dots_inside.txt", "r")
for l in f.readlines():
    _xy += [tuple(map(float, l.split(' ')[:2]))]
f.close()
_xy_copy = list(_xy)
print("Parsed points: {0}".format(len(_xy)))

f = open(result_path + "dots_contour.txt", "r")
contours = []
for l in f.readlines():
    contour = tuple(map(float, l.split(' ')[:2]))
    _xy.remove(contour)
    _xy_copy[_xy_copy.index(contour)] = -9999
    contours += [contour]
f.close()
#убираем все точки, которые заходят на контур.
contour_collision = []
for p in _xy:
    for cont_p in contours:
        flag = False
        if dist(p, cont_p) < covid_size:
            contour_collision += [p]
            flag = True
            break
        if flag:
            break

for p in contour_collision:
    _xy.remove(p)
    _xy_copy[_xy_copy.index(p)] = -9999
        

trngs = []
f = open(result_path + "d_triangles.txt", "r")
for l in f.readlines():
    trngs += [tuple(map(int, l.split(' ')[:3]))]
f.close()
print("Parsed triangles: {0}".format(len(trngs)))

# __xy = []

# for i in range(0,len(_xy)):
#     if i % 3 == 0:
#         __xy += _xy[i]


# draw.point(
#     xy= _xy,
#     fill='black'
# )

# im.paste(covid, (0,0), mask=covid)
def get_from_copy_xy(index):
    if _xy_copy[index] == -9999:
        raise IndexError("err")
    else:
        return _xy_copy[index]

_trngs_xy = []
for (a, b, c) in trngs:
    try:
        _a = get_from_copy_xy(a-1)
        _b = get_from_copy_xy(b-1)
        _c = get_from_copy_xy(c-1)
        _point = ((_a[0]+_b[0]+_c[0])/3,(_a[1]+_b[1]+_c[1])/3)
        offset = (int(_point[0]-covid_size/2),int(_point[1]-covid_size/2))
        _trngs_xy += [offset]
    except IndexError:
        continue
    # im.paste(covid, offset, mask=covid)

# for _ in range(len(trngs_xy)-wanna_dots):
#     index = random.randint(0, len(trngs_xy)-1)
#     trngs_xy.pop(index)
# print("Removed other trngls, len now: {0}".format(len(trngs_xy)))

# for (x,y) in _xy:
#     offset = (int(x-covid_size/2),int(y-covid_size/2))
#     im.paste(covid, offset, mask=covid)

# for _ in range(len(_xy)-wanna_dots):
#     index = random.randint(0, len(_xy)-1)
#     while _xy[index] in contour:
#         index = random.randint(0, len(_xy)-1)
#     _xy.pop(index)
# print("Removed other points, len now: {0}".format(len(_xy)))

# trngs_xy = _trngs_xy
# _trngs_xy = [(int(x), int(y)) for (x,y) in _xy]
trngs_xy = []
temp = []

for t_i in range(len(_trngs_xy)-2):
    if t_i in temp:
        continue
    trngs_xy += [_trngs_xy[t_i]]
    temp += [t_i]
    for t_h in range(t_i+1, len(_trngs_xy)-1):
        if t_h in temp:
            continue
        a = _trngs_xy[t_i]
        b = _trngs_xy[t_h]
        if point_in_covid(a[0], a[1], b[0], b[1]):
            temp += [t_h]

print("Result points: {0}".format(len(trngs_xy)))
    
# for (xc,yc) in _trngs_xy:
#     trngs_xy += [(xc,yc)]
#     # _trngs_xy.remove((xc,yc))
#     for (x, y) in _trngs_xy:
#         if point_in_covid(x,y, xc, yc):
#             _trngs_xy.remove((x,y))

for (x,y) in trngs_xy:
    im.paste(covid, (x,y), mask=covid)

#for debug triangles:
index = 1
for (x,y) in [(x2+covid_size/2, y2+covid_size/2) for (x2,y2) in trngs_xy]:
    draw.text((x,y), str(index), fill="blue", size=260)
    index += 1





#for debug coords:
# index = 1
# for (x,y) in trngs_xy:
#     offset = (int(x),int(y))
#     draw.text(offset, str(index), fill="blue", size=260)
#     index += 1

draw.point([(x, y) for (x,y) in trngs_xy], fill="blue")

# contour
# contour_edges = []
# f = open("result/edge_contour.txt", "r")
# for l in f.readlines():
#     pos = tuple(map(int, l.split(' ')[:2]))
#     contour_edges += [contours[pos[0]-1],contours[pos[1]-1]]

# draw.line(contour_edges, width=15, fill="green", joint="curve")

# r = 2
# for x, y in _xy:
#     temp = (x-r,y-r,x+r,y+r)
#     draw.rectangle(xy=temp, fill='red')

# print(_xy)
# im.show()
im.save('result/letter2.png', quality=95)