'''

This script creates a file in the Data folder ("Data/coffee_places_ohio.gpkg"),
 containing the geography data of all coffeeshop locations in Ohio.
The Open Street Map (OSM) API is used. 

A figure is created with a map to check the validity of the found locations.

'''

#%% load modules
import os
import pandas as pd
import osmnx as ox
import plotly.express as px

#%% get data

# Path to the Conda environment (needed for GDAL/PROJ)
conda_env = r"C:\Users\boie.2\.conda\envs\erdos_ds_environment"
os.environ["GDAL_DATA"] = os.path.join(conda_env, "Library", "share", "gdal")
os.environ["PROJ_LIB"] = os.path.join(conda_env, "Library", "share", "proj")

# OSMnx settings
ox.settings.timeout = 600  # increase timeout
ox.settings.overpass_endpoint = "https://overpass.kumi.systems/api/interpreter"

# Get Ohio boundary
ohio = ox.geocode_to_gdf("Ohio, USA")

# Get coffee places (coffee shops like Starbucks)
# evaluating the fast_food file list manually looking for keyword "coffee", the following 
# cuisine tag seems to fit best
tags = {
    "amenity": ["cafe"]
    }
coffee_places = ox.features_from_place("Ohio, USA", tags=tags)

# Only keep rows with "breakfast style" cafe
# if cuisine is empty, check that "name" contains cafe/tea/coffee/bagel/bakery
keywords = "cafe|tea|coffee|bagel|bakery"
cuisine = "coffee|donut|bagel|bakery"
coffee_places = coffee_places[
    (coffee_places["cuisine"].str.contains(cuisine, case=False, na=False)) |
    (coffee_places["cuisine"].isna() & coffee_places["name"].str.contains(keywords, case=False, na=False))
    ]



# Project to WGS84 for map
coffee_places_proj = coffee_places.to_crs(epsg=4326)
coffee_places["lat"] = coffee_places_proj.centroid.y
coffee_places["lon"] = coffee_places_proj.centroid.x




#%% do a plot
# Map check
fig = px.scatter_map(coffee_places,
                     lat="lat",
                     lon="lon",
                     hover_name="name",
                     zoom=7,
                     size_max=10,
                     map_style="carto-positron",
                     title="Coffee shops and coffee places in Ohio"
                    )
fig.show()

# Save to GeoPackage
coffee_places.to_file("Data/coffee_places_ohio.gpkg", layer="coffee_places", driver="GPKG")

# %% save as csv if desired

coffee_places.to_csv("Data/coffee_places_ohio.csv", index=False)

# %%
