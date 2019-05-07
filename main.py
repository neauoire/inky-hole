from inky import InkyPHAT

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw

# img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
# draw = ImageDraw.Draw(img)

# from font_fredoka_one import FredokaOne

# font = ImageFont.truetype(FredokaOne, 22)

# message = "Hello, World!"
# w, h = font.getsize(message)
# x = (inky_display.WIDTH / 2) - (w / 2)
# y = (inky_display.HEIGHT / 2) - (h / 2)

# draw.text((x, y), message, inky_display.RED, font)
# inky_display.set_image(img)
# inky_display.show()

import json
import urllib2

try:
    f = urllib2.urlopen('http://pi.hole/admin/api.php')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    queries = parsed_json['dns_queries_today']
    adsblocked = parsed_json['ads_blocked_today']
    clients = parsed_json['unique_clients']
    f.close()
except:
    queries = '-'
    adsblocked = '-'
    clients = '-'

pihole = 'DNS-Queries: ' + str(queries) + ' - ' + 'Ads blocked: ' + str(adsblocked) + ' - ' + 'Devices: ' + str(clients)
print pihole


# img = Image.open("/home/pi/inky-hole/logo.png")
# inky_display.set_image(img)
# inky_display.show()
