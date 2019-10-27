"""
This script calculates anomalies as proposed by Papagiannopoulou et al.

References:
-----------
[1] Papagiannopoulou, C.et al. 2017. A non-linear Granger-causality 
    framework to investigate climate—vegetation dynamics.Geosci. Model
    Dev.10:1945–1960. 
"""

# Load packages.
import glob
import xarray as xr
import numpy as np
import tools as alextools
from dask.diagnostics import ProgressBar

# Here comes the few lines which you are allowed to change.
###############################################################################              
###############################################################################              
############################################################################### 
# Where monthly means data live
input_folder = "/LFASGI/sandroal/data_sets/ERA_INTERIM/" + \
               "soil_temperature_layer1_mmeans/"

# Where to put results.        
output_folder = "/LFASGI/sandroal/data_sets/ERA_INTERIM/" + \
                "soil_temperature_layer1_ano/"

# Data extension.
extension = "grb"

# Variable code.
code = "stl1" 
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

# Load data.
print("\n>>> Loading data into memory ...")
with ProgressBar():
    DS = DS.sortby("time")

# Extract data array.
DA = getattr(DS, code)

# Calculate linear trends and its parameters.
trends, parameters = alextools.linear_trends(DA)

# Sazonality of detrended data.
seasonal = alextools.climatology(DA)

# Anomalies.
anomalies = alextools.anomalies(DA)

# Put all results in the same xarray Dataset object.
results = xr.Dataset(data_vars={"ano": anomalies,
                                "tre": trends,
                                "sea": seasonal,
                                "par": parameters}) 

# Make one file per year.                                                                    
print("\n>>> Saving results for " + code + " at " + output_folder + " ...")
for year in np.unique(results.time.dt.year):
    print("* year:", str(year))
    results.sel(time=str(year)).to_netcdf(
        output_folder + code + "_ano_" + str(year) + ".nc"
    )
