import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def colour_producer(elev):
    if elev < 1500:
        return 'green'
    elif 1500<= elev < 2500:
        return 'orange'
    else:
        return 'red' 

map = folium.Map(location=[38.95, -104.94], zoom_start=5, tiles = "Stamen Terrain")

# this is the way to add a child. However, for more control we want to use feature groups.
# map.add_child(folium.Marker(location=[46.00, 9.18], popup="I'm a Marker", icon=folium.Icon(color="green")))

fg = folium.FeatureGroup(name="USA Volcanoes")
# to add multiple we have to add them one at a time... helloo for loops!
# seeing as we're iterating over more than one list at the same time we need to use zip!
for lat, lon, name, el in zip(lat, lon, name, elev):
    fg.add_child(folium.CircleMarker(location=[lat, lon], radius=6, popup=str(name)+" "+str(el)+" m",
    fill_color=colour_producer(el), fill = True, fill_opacity=0.8, color='grey'))

pop = folium.FeatureGroup(name="Population")

pop.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: { 'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(pop)
map.add_child(folium.LayerControl())

map.save("VolcanoesMap.html")

# popup=folium.Popup(str(el), parse_html=True) this is if the string you're passing has ' in them