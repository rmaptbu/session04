### "geolocation"
from geolocate import geolocate
london_location=geolocate("London")
print london_location

### "URL"
from mapurl import map_at
map_response=map_at(51.5072, -0.1275, zoom=10)
url=map_response.url
print url

### "png"
import imagemanipulation as im
print im.count_green_in_png(map_at(*london_location))

### "points"

from numpy import linspace
def location_sequence(start,end,steps):
  # Would actually prefer this if steps
  # were deduced from zoomlevel
  # But need projection code for that
  lats=linspace(start[0],end[0],steps)
  longs=linspace(start[1],end[1],steps)
  return zip(lats,longs)

[im.count_green_in_png(map_at(*location,zoom=10,satellite=True))
            for location in location_sequence(
                geolocate("London"),
                geolocate("Birmingham"),
                10)]


### "save"
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
with open('green.png','w') as green:
    green.write(im.show_green_in_png(map_at(*london_location,
        zoom=10,satellite=True)))

plt.plot([
    im.count_green_in_png(
        map_at(*location,zoom=10,satellite=True))
          for location in location_sequence(
              geolocate("London"),
              geolocate("Birmingham"),10)])
plt.savefig('greengraph.png')
