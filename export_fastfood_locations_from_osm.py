'''

This script creates a file in the Data folder ("Data/fastfood_ohio.gpkg"),
 containing the geography data of all fast-food drive through locations in Ohio.
The Open Street Map (OSM) API is used. 

A figure is created with a map to check the validity of the found locations.

'''
import os


# Path to the Conda environment
conda_env = r"C:\Users\raab.75\AppData\Local\miniconda3\envs\erdos_ds_environment"

os.environ["GDAL_DATA"] = os.path.join(conda_env, "Library", "share", "gdal")
os.environ["PROJ_LIB"] = os.path.join(conda_env, "Library", "share", "proj")


# Optional: verify setup
#print("GDAL_DATA:", os.environ.get("GDAL_DATA"))
#print("PROJ_LIB:", os.environ.get("PROJ_LIB"))


import pandas as pd
import osmnx as ox
import plotly.express as px


ohio = ox.geocode_to_gdf("Ohio, USA")

# Get all fast-food drive-through locations
fastfood = ox.features_from_place(
    "Ohio, USA",
    tags={"amenity": "fast_food", "drive_through": "yes"}
)

#more strict filtering... before this line also banks with drive through showed up
fastfood = fastfood[(fastfood["amenity"]=="fast_food") & (fastfood["drive_through"]=="yes")]

# Extract coordinates
fastfood_proj = fastfood.to_crs(epsg=4326)  # project to meters
fastfood["lat"] = fastfood_proj.centroid.y
fastfood["lon"] = fastfood_proj.centroid.x

# opening a map to check if those locations make sense


fig = px.scatter_map(
    fastfood,
    lat="lat",
    lon="lon",
    hover_name="name",       # optional, if 'name' column exists
    zoom=9,                  # adjust zoom to fit Franklin County
    size_max=10,
    map_style="carto-positron",
    title="Fast-Food Drive-Throughs in Ohio"
)

fig.show()

fastfood.to_file("Data/fastfood_ohio.gpkg", layer="fastfood", driver="GPKG")



