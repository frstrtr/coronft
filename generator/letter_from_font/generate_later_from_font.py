import random
import math
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import ImageFont, truetype

original_size = 25
covid_size = 125

covid = Image.open("covid_alpha.png", "r").convert("RGBA")
covid = covid.resize((covid_size,covid_size), Image.ANTIALIAS)



for letter in ["A", "G", "T", "C"]:
    im = Image.new('RGB', (original_size*covid_size, original_size*covid_size), (255,255,255))
    draw = ImageDraw.Draw(im)


    _im = Image.open(letter+"25.png")
    rgb = _im.convert("RGB")
    points = []
    for n in range(25):
        for m in range(25):
            if rgb.getpixel((n,m)) == (0,0,0):
                points += [(n,m)]

    for p in points:
        offset = (int(p[0]*covid_size),int(p[1]*covid_size))
        im.paste(covid, offset, mask=covid)

    # draw.point(
    #     xy= points,
    #     fill='blue'
    # )

    print(len(points))
    size=len(points)
    # print(_xy)
    # im.show()
    im.save('result/{0}_{1}.png'.format(letter, size), quality=95)