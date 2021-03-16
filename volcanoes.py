import folium

map = folium.Map(location=[45.98, 9.21], zoom_start=10, tiles = "Stamen Terrain")

map.add_child(folium.Marker(location=[46.00, 9.18], popup="I'm a Marker", icon=folium.Icon(color="green")))

map.save("Map1.html")