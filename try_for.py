from modules.reverse_geocode import reverse_geocode
latitude = 27.7172
longitude = 85.3240

location = reverse_geocode(latitude, longitude)

print(location)