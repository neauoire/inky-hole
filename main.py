import json
import urllib2
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

# Load graphic

img = Image.open("./logo.png")
draw = ImageDraw.Draw(img)

# get api data

try:
  f = urllib2.urlopen('http://pi.hole/admin/api.php')
  json_string = f.read()
  parsed_json = json.loads(json_string)
  adsblocked = parsed_json['ads_blocked_today']
  ratioblocked = parsed_json['ads_percentage_today']
  f.close()
except:
  queries = '?'
  adsblocked = '?'
  ratio = '?'

font = ImageFont.truetype(FredokaOne, 32)

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

draw.text((20,20), str(adsblocked), inky_display.BLACK, font)
draw.text((20,50), str("%.1f" % round(ratioblocked,2)) + "%", inky_display.BLACK, font)

inky_display.set_image(img)

inky_display.show()
