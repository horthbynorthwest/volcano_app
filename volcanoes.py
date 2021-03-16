import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[45.98, 9.21], zoom_start=10, tiles = "Stamen Terrain")


# this is the way to add a child. However, for more control we want to use feature groups.
# map.add_child(folium.Marker(location=[46.00, 9.18], popup="I'm a Marker", icon=folium.Icon(color="green")))

fg = folium.FeatureGroup(name="My Map")
# to add multiple we have to add them one at a time... helloo for loops!
fg.add_child(folium.Marker(location=[46.00, 9.18], popup="I'm a Marker", icon=folium.Icon(color="green")))
map.add_child(fg)


map.save("Map1.html")