from PIL import Image
from nose.tools import assert_equal
import math
def test_greeter():
    #regression test
    import greengraph
    assert_equal(Image.open("greengraph_test.png").histogram(), 
	Image.open("greengraph.png").histogram())
	#unit tests