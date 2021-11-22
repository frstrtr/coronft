import random
import time
from pathlib import Path
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

__im = [Image.new('RGB', (1024,1024), (0, 0, 0)) for _ in range(1)]

im = __im[0]#Image.new('RGB', (4096,4096), (0, 0, 0))
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

print("Max x:{0}; y:{1}".format(max(_xy, key=lambda item:item[0])[0], max(_xy, key=lambda item:item[1])[1]))
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
    

tile_size = 256

def dot(pixels, _x, _y, scale):
    _x = int(_x)
    _y = int(_y)
    for x in range(_x, _x+scale):
        # x = int(_x)+i
        # for h in range(scale):
        for y in range(_y, _y+scale):
            # y = int(_y)+h
            pixels += [(x,y)]


def draw_tile(z, x, y, pixels):
    _im = Image.new('RGB', (tile_size, tile_size), (0, 0, 0))
    _draw = ImageDraw.Draw(_im)
    for i in range(tile_size):
        for h in range(tile_size):
            if pixels[x*tile_size+i][y*tile_size+h]:
                _draw.point((i,h), fill = "white")

    Path("tiles/{0}/{1}".format(z, x, y)).mkdir(parents=True, exist_ok=True)
    _im.save('tiles/{0}/{1}/{2}.png'.format(z, x, y), quality=95)

def draw_tiles(draws, pixels):
    for (x,y) in pixels:
        draws[x//tile_size][y//tile_size].putpixel(xy=(x%tile_size,y%tile_size), value=(255, 255, 255))

    # for i in range(tile_size):
    #     for h in range(tile_size):
    #         if pixels[x*tile_size+i][y*tile_size+h]:
    #             _draw.point((i,h), fill = "white")

    

# for let in let_k:
#     #draw_letter(let)
#     draw_point(let)

for zoom in range(6):
    print('Zoom:{0}'.format(zoom))
    t0 = time.time()
    scale = 2**zoom
    size = 3 * scale
    # _im = [[Image.new('RGB', (tile_size, tile_size), (0, 0, 0)) for _ in range(size) ] for _ in range(size)]
    # _draw = [[ImageDraw.Draw(_im[x][y]) for x in range(size) ] for y in range(size)]
    # pixels = [[False for _ in range(size*tile_size)] for _ in range(size*tile_size)]
    pixels = []
    for (_x,_y) in _xy:
        dot(pixels, _x*scale, _y*scale, scale)
        # __draw = 
        # _draw.rectangle((x*scale,y*scale,(x+1)*scale,(y+1)*scale), fill = "white")
    
    _tiles = [[Image.new('RGB', (tile_size, tile_size), (0, 0, 0)) for _ in range(size) ] for _ in range(size)]
    _draw_tiles = [[ImageDraw.Draw(_tiles[x][y]) for x in range(size) ] for y in range(size)]
    # for x in range(size):
    #     for y in range(size):
    #         draw_tile(zoom, x, y, pixels)
    draw_start = time.time()
    draw_tiles(_tiles, pixels)
    # Save to file
    save_start = time.time()
    for x in range(size):
        for y in range(size):
            Path("tiles/{0}/{1}".format(zoom, x, y)).mkdir(parents=True, exist_ok=True)
            _tiles[x][y].save('tiles/{0}/{1}/{2}.png'.format(zoom, x, y), quality=95)

    t1 = time.time()
    print("Time for zoom = {0} -> {1}".format(zoom, t1-t0))
    print("Time for draw = {0} -> {1}".format(zoom, save_start-draw_start))
    print("Time for save = {0} -> {1}".format(zoom, t1-save_start))
    # Path("tiles/test/{0}".format(zoom)).mkdir(parents=True, exist_ok=True)
    # _im.save('tiles/test/{0}/1.png'.format(zoom), quality=95)
    
#DRAW_END

# im.save('result_letter_a.png', quality=95)