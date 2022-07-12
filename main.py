import os
import json
import urllib3
from sys import exit

from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

# Set current directory

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load graphic

img = Image.open("./logo.png")
draw = ImageDraw.Draw(img)

# get api data

http = urllib3.PoolManager()

try:
  r = http.request('GET', 'http://pi.hole/admin/api.php')
  if r.status >= 200 or r.status <= 299:
    exit("http request is unsuccessful")
    
except:
  adsblocked = '?'
  ratioblocked = '?'

parsed_json = json.loads(r.data)
adsblocked = parsed_json['ads_blocked_today']
ratioblocked = parsed_json['ads_percentage_today']

font = ImageFont.truetype(FredokaOne, 32)

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

draw.text((20,20), str(adsblocked), inky_display.BLACK, font)

if isinstance(ratioblocked, str):
  draw.text((20,50), f"{ratioblocked}%", inky_display.BLACK, font)
else:
  draw.text((20,50), f"{ratioblocked:.2f}%", inky_display.BLACK, font)

img = img.rotate(180)
inky_display.set_image(img)

inky_display.show()
