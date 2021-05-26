#More accurate location needed

import geocoder
# g = geocoder.ip('199.168.22.1')
g = geocoder.ip('me')
# c=geocoder.location()
# g = geocoder.google('India')
print(f"Lat: {g.lat}, Lon: {g.lng}")
# c = geocoder.google([g.lat, g.lng], method='reverse')

# print(c.country)