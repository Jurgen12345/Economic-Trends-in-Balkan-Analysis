import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import pandas as pd
import geopandas as gpd
import geodatasets
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon,Patch
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np


# pd.set_option("display.max_columns", None)

matplotlib.use("QtAgg")

countries = ["Albania","Kosovo","Greece","Italy","Republic of Serbia","Montenegro","Bulgaria"
                                                   ,"Croatia","Cyprus","Bosnia and Herzegovina","North Macedonia","Romania"]

countries_v2 = ["Albania","Kosovo","Greece","Italy","Serbia","Montenegro","Bulgaria"
                                                   ,"Croatia","Cyprus","Bosnia and Herzegovina","North Macedonia","Romania"]


world_data = gpd.read_file(r"data\ne_110m_admin_0_countries.shp")
balkan = world_data[world_data["SOVEREIGNT"].isin(countries)]

gdp_growth_data = pd.read_csv(r"data\gdp_growth_annual.csv",skiprows=4)
expenses_data = pd.read_csv(r"data\expenses.csv", skiprows= 4)
inflation_data = pd.read_csv(r"data\inflation.csv", skiprows=4)


year = "2024"
year_expenses = "2022"

balkan_gdp_growth = gdp_growth_data[gdp_growth_data["Country Name"].isin(countries_v2)][
    ["Country Name","Country Code",year]
].copy()
balkan_gdp_growth[year] = pd.to_numeric(balkan_gdp_growth[year], errors="coerce")
gdp_lookup = dict(zip(balkan_gdp_growth["Country Name"], balkan_gdp_growth[year]))

balkan_expenses = expenses_data[expenses_data["Country Name"].isin(countries_v2)][
    ["Country Name", "Country Code", year_expenses]
]
balkan_expenses[year_expenses] = pd.to_numeric(balkan_expenses[year_expenses], errors="coerce")
balkan_expenses = balkan_expenses.sort_values("Country Name", ascending=False)
print(balkan_expenses)


inflation_years = [str(y) for y in range(2000, 2025)]

balkan_inflation = inflation_data[inflation_data["Country Name"].isin(countries_v2)][
    ["Country Name", "Country Code"] + inflation_years
].copy()

balkan_inflation[inflation_years] = balkan_inflation[inflation_years].apply(
    pd.to_numeric, errors="coerce"
)

print(balkan_inflation)


fig, ax = plt.subplots(figsize = (8,6))

fig2, ax2 = plt.subplots(figsize = (8,7))

patches = []
gdp_patches = []

for column, row in balkan.iterrows():
    geom = row["geometry"]
    country_name = row["SOVEREIGNT"]
    gdp_value = gdp_lookup.get(country_name,np.nan)
    if geom.geom_type == "MultiPolygon":
        for polygon in geom.geoms:
            coords = polygon.exterior.coords
            patches.append(Polygon(coords,closed=True))
            gdp_patches.append(gdp_value)
    elif geom.geom_type == "Polygon":
        coords = geom.exterior.coords
        patches.append(Polygon(coords, closed=True))
        gdp_patches.append(gdp_value)


gdp_values = np.array(gdp_patches, dtype = float)

cmap = plt.cm.Blues
valid_gdp_values = gdp_values[~np.isnan(gdp_patches)]
norm = matplotlib.colors.Normalize(vmin=valid_gdp_values.min(),vmax = valid_gdp_values.max())


patch_collection = PatchCollection(
    patches=patches,
    edgecolor = "black",
    linewidth = 0.7,
    cmap=cmap,
    norm=norm
)

patch_collection.set_array(gdp_values)
ax.add_collection(collection=patch_collection)
ax.autoscale()
ax.set_aspect("equal")
ax.set_title(f"GDP Growth ({year})")

sm = matplotlib.cm.ScalarMappable(cmap=cmap,norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax,shrink = 0.7)
cbar.set_label(f"GDP Growth ({year})")

ax.set_axis_off()
fig.tight_layout()


balkan_expenses = balkan_expenses.dropna(subset=[year_expenses]).copy()

balkan_expenses = balkan_expenses.sort_values(year_expenses)

colors = ["#c21f1f" if v < 0 else "#0b82b5" for v in balkan_expenses[year_expenses]]

bars = ax2.barh(
    balkan_expenses["Country Name"],
    balkan_expenses[year_expenses],
    color=colors
)

ax2.axvline(0, color="black", linewidth=1)

for bar, value in zip(bars, balkan_expenses[year_expenses]):
    y = bar.get_y() + bar.get_height() / 2

    if value < 0:
        ax2.text(value, y, f"{value:.1f}", va="center", ha="right")
    else:
        ax2.text(value, y, f"{value:.1f}", va="center", ha="left")

ax2.set_title(f"Expenses ({year_expenses})")
ax2.set_xlabel("Expenses")
ax2.set_ylabel("")

for spine in ["top", "right"]:
    ax2.spines[spine].set_visible(False)


fig3, ax3 = plt.subplots(figsize = (10,6))

for column,row in balkan_inflation.iterrows():
    ax3.plot(inflation_years, row[inflation_years],marker = "o",linewidth = 2, label = row["Country Code"], alpha = 0.7)

ax3.set_title("Inflation Rate Over Time")
ax3.set_xlabel("Years")
ax3.set_ylabel("Inflation (%)")
ax3.legend(title = "Country Code")
ax3.set_xticks(ax3.get_xticks()[::2])

fig.savefig("GDP_Growth.png")
fig2.savefig("Expenses.png")
fig3.savefig("Inflation_over_years.png")


plt.show()