from PIL import Image
from nose.tools import assert_equal
import math
import numpy as np
def test_greengraph():
    #regression test
    import greengraph
    assert_equal(Image.open("greengraph_test.png").histogram(), 
	Image.open("greengraph.png").histogram())
	
#unit tests
def test_geolocate():
	from geolocate import geolocate
	np.testing.assert_almost_equal(geolocate("london"), (51.5073509, -0.1277583))
	
def test_mapurl():
	from mapurl import map_at
	assert_equal(map_at(51.5073509, -0.1277583, zoom=10).url, "http://maps.googleapis.com/maps/api/staticmap?style=feature%3Aall%7Celement%3Alabels%7Cvisibility%3Aoff&center=51.5073509%2C-0.1277583&sensor=false&zoom=10&size=400x400")

#def test_imagemanipulation():
