import random
import time
from PIL import Image, ImageDraw

#config
wanna_dots = 29903
let_k = ['A', 'C', 'G', 'T']
letter_size = 800

letter_nums = dict()
letter_nums['A'] = 8954
letter_nums['G'] = 5863
letter_nums['C'] = 5492
letter_nums['T'] = 9594
#CONFIG_END

def get_letter(let, size):
    img = Image.open("letters/{0}.png".format(let), "r").convert("RGBA")
    img = img.resize((letter_size,letter_size), Image.ANTIALIAS)
    return img

letters = {let:get_letter(let, letter_size) for let in let_k}

let_a = Image.open("/home/sl33n/coronft/images/a2.png", "r")

im = Image.new('RGB', (4096,4096), (0, 0, 0))
draw = ImageDraw.Draw(im)

#parse dots
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
#PARSE_DOTS_END

#draw
# for (x,y) in _xy:
#     offset = (int(x*2),int(y*2))
#     im.paste(let_a, offset, mask=let_a)
#     _xy.remove((x,y))

i = 0

def draw_letter(let):
    global i
    for _ in range(letter_nums[let]):
        letter_offset = random.choice(_xy)
        im.paste(letters[let], (int(letter_offset[0]*letter_size), int(letter_offset[1]*letter_size)), mask=letters[let])
        _xy.remove(letter_offset)

def draw_point(let):
    global i
    for _ in range(letter_nums[let]):
        letter_offset = random.choice(_xy)
        draw.point(xy=(int(letter_offset[0]), int(letter_offset[1])), fill = "white")
        _xy.remove(letter_offset)
    
for let in let_k:
    #draw_letter(let)
    draw_point(let)

#DRAW_END

im.save('result_letter_a.png', quality=95)