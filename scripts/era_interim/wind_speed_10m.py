"""
This script calculates wind speed horizontal intensity [sqrt(u^2+v^2)] from 
data of wind's vector components (u, v).
"""

# Load packages.
import glob
import xarray as xr
import numpy as np
from dask.diagnostics import ProgressBar

# Load data.
folder = "/LFASGI/sandroal/data_sets/ERA_INTERIM/wind_speed_10m_daily/"
files = sorted(glob.glob(folder + "*.nc"))
files = [f for f in files if "uv" in f]
DS = xr.open_mfdataset(files)

# Make sure data is time ordered.
DS = DS.sortby("time")

# Extract components.
u = DS.u10
v = DS.v10

# Probably unnecessary.
u, v = xr.align(u, v)

# Calculate horizontal speed.
si10 = xr.ufuncs.sqrt(u ** 2 + v ** 2)

# Daily mean values.
DS = si10.to_dataset(name="si10")

# Load data into memory.
print("\n>>> Loading dada into memory ...")
with ProgressBar():
    DS = DS.compute()

# Make one file per month.
print("\n>>> Saving results for si10 at " + folder + " ...")
for year in np.unique(DS.time.dt.year):
    for month in np.unique(DS.time.dt.month):
        print("* year/month:", str(year) + "/" + "{0:02d}".format(month))
        DS.sel(time=str(year) + "-" + "{0:02d}".format(month)).to_netcdf(
            folder + "si10_daily_" + str(year) + "_{0:02d}.nc".format(month)
        )
