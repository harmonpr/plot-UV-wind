import numpy as np
import xarray as xr
import pandas as pd
import cartopy.crs as ccrs
from cartopy.feature import NaturalEarthFeature
from matplotlib import pyplot as plt

# import the data, you can download it from below
# https://drive.google.com/file/d/1O2sFzvaP43j2DQpviqai1d2_vBPoFsFB/view?usp=sharing
data_set = xr.open_dataset('jan2016-des2020.nc')

# select the wind component want to plot, i.e. 'u10' or 'v10'
wind_component = data_set['u10']
component = 'U' if wind_component.name == data_set['u10'].name else 'V'

# colorbar attributes
cbar_kwargs = {
    'orientation':'horizontal',
    'fraction': 0.045,
    'pad': 0.01,
    'extend':'neither',
    'label': component + ' velocity m/s'
}

# choose the data at specified index time
i = 100
wind = data_set.u10.isel(time=100)

# figure set up
fig = plt.figure(figsize=(12,12))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(NaturalEarthFeature('cultural', 'admin_0_countries', '10m'),
              facecolor='none', edgecolor='black')
ax.set_extent([93, 143, 10, -13])
ax.gridlines()

# plot the data
wind.plot.imshow(ax=ax, transform=ccrs.PlateCarree(), add_colorbar=True,
         cbar_kwargs=cbar_kwargs, interpolation='bicubic')

# save the figure
plt.savefig("map.png", bbox_inches='tight', dpi=150)

plt.show()
