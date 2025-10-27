import os
import pandas as pd
import osmnx as ox
import plotly.express as px

# Path to the Conda environment (needed for GDAL/PROJ)
conda_env = r"C:\Users\raab.75\AppData\Local\miniconda3\envs\erdos_ds_environment"
os.environ["GDAL_DATA"] = os.path.join(conda_env, "Library", "share", "gdal")
os.environ["PROJ_LIB"] = os.path.join(conda_env, "Library", "share", "proj")

# OSMnx settings
ox.settings.timeout = 600  # increase timeout
ox.settings.overpass_endpoint = "https://overpass.kumi.systems/api/interpreter"

# Get Ohio boundary
ohio = ox.geocode_to_gdf("Ohio, USA")

# Get pizza places (restaurants or fast food serving pizza)
tags = {
    "amenity": ["restaurant", "fast_food"],
    "cuisine": "pizza"
}
pizza_places = ox.features_from_place("Ohio, USA", tags=tags)

# Optional: only keep rows with amenity pizza/restaurant
pizza_places = pizza_places[(pizza_places["amenity"].isin(["restaurant", "fast_food"]))]

# Project to WGS84 for map
pizza_places_proj = pizza_places.to_crs(epsg=4326)
pizza_places["lat"] = pizza_places_proj.centroid.y
pizza_places["lon"] = pizza_places_proj.centroid.x

# Map check
fig = px.scatter_map(
    pizza_places,
    lat="lat",
    lon="lon",
    hover_name="name",
    zoom=7,
    size_max=10,
    map_style="carto-positron",
    title="Pizza Places in Ohio"
)
fig.show()

# Save to GeoPackage
pizza_places.to_file("Data/pizza_places_ohio.gpkg", layer="pizza_places", driver="GPKG")