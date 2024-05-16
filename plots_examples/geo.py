import geopandas
from geodatasets import get_path
import matplotlib.pyplot as plt

path_to_data = get_path("nybb")
gdf = geopandas.read_file(path_to_data)

gdf = gdf.set_index("BoroName")
gdf["area"] = gdf.area
gdf["boundary"] = gdf.boundary
gdf["centroid"] = gdf.centroid

ax = gdf.plot("area", legend=True)
gdf["centroid"].plot(ax=ax, color="black")

plt.show()