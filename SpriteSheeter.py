#!/usr/bin/env python3
import os, sys, math, configparser
from PIL import Image, ImageDraw, ImageColor

usage = 'usage: ' + sys.argv[0] + ' [file.ini]\n\tno argument defaults to \'config.ini\''

# Check Arguments
config_filename = 'config.ini'
arguments = len(sys.argv);
if arguments == 2:
    config_filename = sys.argv[1]
elif arguments > 2:
    print(usage)
    exit()

# Check Config File
if os.path.isfile(config_filename) == False:
    print('Can\'t open config file \'' + config_filename + '\'')
    print(usage)
    exit()

# Load Config
config = configparser.ConfigParser()
config.read(config_filename)

# Read Config
setup = config['Setup']
output_format = setup['OutputFormat']
output_filename = setup['OutputFilename']
images_per_row = int(setup['ImagesPerRow'])
r, g, b = ImageColor.getrgb(setup['BackgroundColor'])
a = int(setup['BackgroundAlpha'])
draw_order = setup['DrawOrder'].split(os.linesep)

# Check Image Files
for image_file in draw_order:
    if os.path.isfile(image_file) == False:
        print('Missing image \'' + image_file + '\'')
        print('Fix config file \'' + config_filename + '\'')
        exit()

# Setup Dimensions
sprite = Image.open(draw_order[0]).convert('RGBA')
sprite_width, sprite_height = sprite.size
width = images_per_row * sprite_width
height = math.ceil((len(draw_order) / images_per_row)) * sprite_height
sheet = Image.new('RGBA', (width, height), (r, g, b, a))
x, y = (0, 0)

# Print Parameters
print('Sprite size: ' + str(sprite_width) + 'x' + str(sprite_height))
print('Sprite sheet size: ' + str(width) + 'x' + str(height))
print('Images per row: ' + str(images_per_row))
print('Writing ' + str(len(draw_order)) + ' images to \'' + output_filename + '\'')

# Draw Sprite Sheet
for image in draw_order:
    sprite = Image.open(image).convert('RGBA')
    sheet.paste(sprite, (x, y))
    x += sprite_width
    if x >= images_per_row * sprite_width:
        x = 0
        y += sprite_height

# Write Sprite Sheet
sheet.save(output_filename, output_format)
print('Done')
