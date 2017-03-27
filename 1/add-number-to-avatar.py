#!/usr/bin/env python                                                                                                                  
# encoding: utf-8


from PIL import Image, ImageDraw, ImageFont

# get an image
im = Image.open('pillow.png').convert('RGBA')

# 画线
#draw = ImageDraw.Draw(im)
#draw.line((0, 0) + im.size, fill=128)
#draw.line((0, im.size[1], im.size[0], 0), fill=128)
## save to a new name
#im.save("test.png", "PNG")

# 写字
#d = ImageDraw.Draw(im)
#d.text((10, 10), "Hello", fill=(255,255,255,128))
#d.text((10, 60), "World", fill=(255,255,255,255))
#im.save("test.png", "PNG")

# make a blank image for the text, initialized to transparent text color
txtLayer = Image.new('RGBA', im.size, (255,0,0,0))
d = ImageDraw.Draw(txtLayer)
# get a font
font = ImageFont.truetype('/usr/share/fonts/truetype/Sacramento-Regular.ttf',20)
# draw text, half opacity
d.text((60, 5), "4", font=font, fill=(255,255,255,255))
# get a font
#font = ImageFont.load('/usr/share/fonts/otf/otfpoc.otf')
# draw text, full opacity
#d.text((10, 60), "World", font=font, fill=(255,255,255,255))

# 合并底层和文字层
rlt = Image.alpha_composite(im, txtLayer)
rlt.save("test.png", "PNG")
