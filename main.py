import os
import json
import urllib3
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

# Set current directory

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load graphic

img = Image.open("./logo.png")
draw = ImageDraw.Draw(img)

# get api data

try:
  f = urllib3.urlopen('http://pi.hole/admin/api.php')
  json_string = f.read()
  parsed_json = json.loads(json_string)
  adsblocked = parsed_json['ads_blocked_today']
  ratioblocked = parsed_json['ads_percentage_today']
  f.close()
except:
  adsblocked = '?'
  ratioblocked = '?'

font = ImageFont.truetype(FredokaOne, 32)

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

draw.text((20,20), str(adsblocked), inky_display.BLACK, font)
draw.text((20,50), str("%.1f" % ratioblocked) + "%", inky_display.BLACK, font)

inky_display.set_image(img)

inky_display.show()
