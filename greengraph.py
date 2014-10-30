from geolocate import geolocate
from mapurl import map_at
import imagemanipulation as im
from locationsequence import location_sequence

#find london location in coordinates
london_location=geolocate("London")
print london_location

#find url of map of london in google maps
map_response=map_at(*london_location, zoom=10)
url=map_response.url
print url

#count number of green pixels on map
print im.count_green_in_png(map_at(*london_location))

#find number of green pixels from London to Birmingham
greens=[im.count_green_in_png(map_at(*location,zoom=10,satellite=True))
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
