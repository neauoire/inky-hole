import json
import urllib2
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

# Load graphic

img = Image.open("/home/pi/inky-hole/logo.png")

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)
inky_display.set_image(img)

# get api data

try:
    f = urllib2.urlopen('http://pi.hole/admin/api.php')
    json_string = f.read()
    parsed_json = json.loads(json_string)

    queries = parsed_json['dns_queries_today']
    adsblocked = parsed_json['ads_blocked_today']
    ratio = parsed_json['ads_percentage_today']

    f.close()
except:
    queries = '?'
    adsblocked = '?'
    ratio = '?'


font = ImageFont.truetype(FredokaOne, 22)

queries = 'Queries: ' + str(queries)
blocked = 'Blocked: ' + str(adsblocked)
ratio   = 'Ratio: ' + str(ratio)

inky_display.text((10, 10), name, inky_display.BLACK, font)

inky_display.show()
