import geopy
geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")
def geolocate(place):
  return geocoder.geocode(place,exactly_one=False)[0][1]