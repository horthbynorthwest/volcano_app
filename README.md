## Let's track some volcanoes! 🌋

Built using Python & Folium.

To create a base map simply type
```python
import folium

map = folium.Map(location=[45.98, 9.21])
map.save("Map1.html")
```

In the list after the location simply pass a list with coordinates. Once you open the Map1.html file it will load in your chosen browser and start focused at your chosen location.

The given coordinates will start you looking at Lake Como, Italy