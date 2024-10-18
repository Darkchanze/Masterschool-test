import folium

map = folium.Map(location=[21.39, 84.29], zoom_start=13)
map.save("map.html")
"""from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

location = geolocator.geocode("New York City")
latitude = location.latitude
longitude = location.longitude

print(f"Latitude: {latitude}, Longitude: {longitude}")"""