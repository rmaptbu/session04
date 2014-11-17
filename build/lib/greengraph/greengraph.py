from geolocate import geolocate
from mapurl import map_at
import imagemanipulation as im
from locationsequence import location_sequence

def process():
	#count number of green pixels between london and birmingham
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
		green.write(im.show_green_in_png(map_at(51.5073509, -0.1277583,
			zoom=10,satellite=True)))

	plt.plot([
		im.count_green_in_png(
			map_at(*location,zoom=10,satellite=True))
			  for location in location_sequence(
				  geolocate("London"),
				  geolocate("Birmingham"),10)])
	plt.savefig('greengraph.png')
