"""
This script in intended for generating monthly extremes values from daily 
anomalies of the selected variable, which is choosen below. The extremes are 
all put in the same file, one for each year. The extremes are represented by 
the following codes:

     Code  Meaning
(1)  Xx    Max daily value per month
(2)  Xn    Min daily value per month
(3)  SD    Standard deviation of daily values per month
(4)  DIR   Difference between max and min daily value per month
(5)  X10p  Number of days per month under 10th percentile
(6)  X90p  Number of days per month over 90th percentile
"""

# Load packages.
import glob

import numpy as np
import xarray as xr

from dask.diagnostics import ProgressBar

# My module.
import tools as alextools

# Here comes the few lines which you are allowed to change. 
###############################################################################
###############################################################################
###############################################################################
# Where daily data live.
input_folder = "/LFASGI/sandroal/data_sets/ERA_INTERIM/" + \
               "surface_relative_humidity_daily/"

# Where to put results.
output_folder = "/LFASGI/sandroal/data_sets/ERA_INTERIM/" + \
                "surface_relative_humidity_extremes_ano/"

# Data extension ("grb" or "nc").
extension = "nc"

# Variable code.
code = "relhum"
###############################################################################
###############################################################################
###############################################################################

# Absolute paths.
FILES = sorted(glob.glob(input_folder + "*." + extension))

# Read all data.
if extension == "grb": # Grib files.
    DS = xr.open_mfdataset(FILES, engine="cfgrib")

else: # Netcdf files
    DS = xr.open_mfdataset(FILES)

# Make sure data is time ordered.
DS = DS.sortby("time")

# Daily mean values. These commands seem not to work on xarray DataArray objects.
DSd = DS.resample({"time": "1D"}).mean()

# Data array for daily data.
DAd = getattr(DSd, code)

# Danger zone! Load data into memory. Take some time (30 min).
print("\n>>> Loading data into memory ...")
with ProgressBar():
    DAd = DAd.compute()

# Daily anomalies.
DAd_ano = alextools.daily_detrended_climatologies(DAd)

# Monthly resampled data object.
resampled = DAd_ano.resample({"time": "1MS"})

# Maximum.
DAd_ano_Xx = resampled.max(dim="time") 

# Minimum.
DAd_ano_Xn = resampled.min(dim="time")

# Standard deviation.
DAd_ano_SD = resampled.std(dim="time")

# Difference between maximum and minimum.
DAd_ano_DIR = DAd_ano_Xx - DAd_ano_Xn

# Quantiles along time axis (masks). 
X10p = DAd_ano < DAd_ano.quantile(q=0.1, dim="time", interpolation="linear") 
X90p = DAd_ano > DAd_ano.quantile(q=0.9, dim="time", interpolation="linear")

# Monthly counts.
DAd_ano_X10p = X10p.resample({"time": "1MS"}).sum(dim="time")
DAd_ano_X90p = X90p.resample({"time": "1MS"}).sum(dim="time")

# Delete these new coordinates.
DAd_ano_X10p = DAd_ano_X10p.drop("quantile")
DAd_ano_X90p = DAd_ano_X90p.drop("quantile") 

# Put all calculations in the same xarray Dataset object.
results = xr.Dataset(data_vars={"Xx": DAd_ano_Xx, 
                                 "Xn": DAd_ano_Xn,
                                 "SD": DAd_ano_SD,
                                 "DIR": DAd_ano_DIR,
                                 "X10p": DAd_ano_X10p,
                                 "X90p": DAd_ano_X90p},
                      coords=DAd_ano_Xx.coords)

# Make one file per year.
print("\n>>> Saving results for " + code + " at " + output_folder + " ...")
for year in np.unique(results.time.dt.year):
    print("* year:", str(year))
    results.sel(time=str(year)).to_netcdf(
        output_folder + code + "_extremes_ano_" + str(year) + ".nc"
    )
