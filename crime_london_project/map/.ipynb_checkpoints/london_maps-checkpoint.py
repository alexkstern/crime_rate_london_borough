import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv("df_2016_2018_for_maps2.csv", sep = ";")
#df = pd.read_csv("mean_top_five_important_attributes_2016_2018.csv")


df["crime"] = df["crime"].astype(float)
df["population_per_hectare"] = df["population_per_hectare"].astype(float)
df["pubs"] = df["pubs"].astype(float)
df["health"] = df["health"].astype(float)
df["public_admin_and_defense"] = df["public_admin_and_defense"].astype(float)
df["dwellings"] = df["dwellings"].astype(float)

df_crime = df[["borough", "crime"]]
df_population = df[["borough", "population_per_hectare"]]
df_pubs = df[["borough", "pubs"]]
df_health = df[["borough", "health"]]
df_admin = df[["borough", "public_admin_and_defense"]]
df_dwellings = df[["borough", "dwellings"]]

map_df = gpd.read_file("London_Borough_Excluding_MHW.shp")
# map_df.plot()
# plt.show(

print(map_df["NAME"])

merged = map_df.set_index("NAME").join(df_population.set_index("borough"))
merged["population_per_hectare"] = np.log10(merged["population_per_hectare"])

print(merged.head())




# set a variable that will call whatever column we want to visualise on the map
variable = "population_per_hectare"
# set the range for the choropleth
vmin, vmax = 22, 159
# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(10, 6))

merged.plot(column=variable, cmap="Reds", linewidth=0.8, ax=ax, edgecolor="0.8")
# remove the axis
ax.axis("off")

# Create colorbar as a legend
sm = plt.cm.ScalarMappable(cmap="Reds", norm=plt.Normalize(vmin=vmin, vmax=vmax))
# empty array for the data range
sm._A = []
# add the colorbar to the figure
cbar = fig.colorbar(sm)

ax.set_title("Average population per hectare from 2016 to 2018")

plt.show()