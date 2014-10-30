from PIL import Image
from nose.tools import assert_equal, assert_almost_equal
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
	
#def test_mapurl():
	#from mapurl import map_at
