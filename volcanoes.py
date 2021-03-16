import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

map = folium.Map(location=[38.95, -104.94], zoom_start=5, tiles = "Stamen Terrain")


# this is the way to add a child. However, for more control we want to use feature groups.
# map.add_child(folium.Marker(location=[46.00, 9.18], popup="I'm a Marker", icon=folium.Icon(color="green")))

fg = folium.FeatureGroup(name="My Map")
# to add multiple we have to add them one at a time... helloo for loops!
# seeing as we're iterating over 2 lists at the same time we need to use zip!
for lat, lon, name, el in zip(lat, lon, name, elev):
    fg.add_child(folium.Marker(location=[lat, lon], popup=str(name)+" "+str(el)+" m", icon=folium.Icon(color="green")))
map.add_child(fg)


map.save("VolcanoesMap.html")

# popup=folium.Popup(str(el), parse_html=True) this is if the string you're passing has ' in them