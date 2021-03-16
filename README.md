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

### Quick Start

1. Clone this repo
2. Ensure you have Python 3.9 on your machine
3. Move into the project repo
4. Run `pip3 install -r requirements.txt` to install dependencies
5. Run `python3 volcanoes.py` to run the file locally
6. Open `VolcanoesMap.html`
7. Click on either 'USA Volcanoes' or 'Population' to toggle the layers