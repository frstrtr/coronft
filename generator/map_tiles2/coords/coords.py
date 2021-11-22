import random
import time

#config
wanna_dots = 29903

_xy = []
f = open("dots_inside.txt", "r")
for l in f.readlines():
    _xy += [tuple(map(float, l.split(' ')[:2]))]
f.close()

contour = []
f = open("dots_contour.txt", "r")
for l in f.readlines():
    contour += [tuple(map(float, l.split(' ')[:2]))]
f.close()

print("Parsed contour points: {0}; of which is located in dots_inside.txt: {1}".format(len(contour), len([x for x in contour if x in _xy])))


print("Parsed points: {0}".format(len(_xy)))
for _ in range(len(_xy)-wanna_dots):
    index = random.randint(0, len(_xy)-1)
    while _xy[index] in contour:
        index = random.randint(0, len(_xy)-1)
    _xy.pop(index)
print("Removed other points, len now: {0}".format(len(_xy)))

print("Max x:{0}; y:{1}".format(max(_xy, key=lambda item:item[0])[0], max(_xy, key=lambda item:item[1])[1]))

f = open("letter_coords.txt", "w")
for (x, y) in _xy:
    f.write("{0} {1}\n".format(x, y))
