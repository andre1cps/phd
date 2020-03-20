# Description

## Overview

Python notebooks intended to explore and analyze climate and vegetation variables one at a time.

## Better visualization


- [invariant_era.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/invariant_era.ipynb?flush_cache=true):
    - These are the variables:
        - 'ANOR': 'angle_of_sub_gridscale_orography.nc',
        - 'CVH': 'high_vegetation_cover.nc',
        - 'CVL': 'low_vegetation_cover.nc',
        - 'ISOR': 'anisotropy_of_sub_gridscale_orography.nc',
        - 'LSM': 'land_sea_mask.nc',
        - 'SDFOR': 'standard_deviation_of_filtered_subgrid_orography.nc',
        - 'SDOR': 'standard_deviation_of_orography.nc',
        - 'SLOR': 'slope_of_sub_gridscale_orography.nc',
        - 'TVH': 'type_of_high_vegetation.nc',
        - 'TVL': 'type_of_low_vegetation.nc',
        - 'Z': 'geopotential.nc'


- [koppen_geiger_classification_kottek2006.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/koppen_geiger_classification_kottek2006.ipynb?flush_cache=true):
    - Maps for the whole globe and South America.


- [land_cover.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/land_cover.ipynb?flush_cache=true):
    - Websites: [ESA-CCI-landcover](https://www.esa-landcover-cci.org/), [Viewer](https://maps.elie.ucl.ac.be/CCI/viewer/), [Publications](https://www.esa-landcover-cci.org/?q=node/184), [Maps legend](https://maps.elie.ucl.ac.be/CCI/viewer/download/CCI-LC_Maps_Legend.pdf), and [Quick user guide](https://maps.elie.ucl.ac.be/CCI/viewer/download/CCI-LC_Maps_Legend.pdf).
    - This is a heavy data set. Just export preprocessed data and try to plot it later in the server!


- [ndvi_gimms.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/ndvi_gimms.ipynb?flush_cache=true): 
    - Data from NASA/GSFC GIMMS NDVI3g version 1 1981-07-01 - 2015-12-31 1/12 x 1/12 degrees 1/24 a year.
    - Original data spatial resolution as well as regridded data in order to fit ERA-INTERIM grid.
    - Monthly means maps.
    - Standard deviation.
    - Seasonal means maps.
    - Empirical orthogonal functions analysis for regridded data.


- [ndvi_gimms2.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/ndvi_gimms2.ipynb?flush_cache=true): 
    - Data from NASA/GSFC GIMMS NDVI3g version 1 1981-07-01 - 2015-12-31 1/12 x 1/12 degrees 1/24 a year.
    - Only reggrided data (ERA-INTERIM grid).
    - Find temporal and spatial occurrences of extreme values.


- [ndvi_gimms3.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/ndvi_gimms3.ipynb?flush_cache=true):
    - Data from NASA/GSFC GIMMS NDVI3g version 1 1981-07-01 - 2015-12-31 1/12 x 1/12 degrees 1/24 a year.
    - Only reggrided data (compatible with ERA-INTERIM grid).
    - Linear trends and its statistics for observed data and anomalies.
    - Kmeans clustering of observed data.


- [ndvi_gimms4.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/ndvi_gimms4.ipynb?flush_cache=true):
    - Data from NASA/GSFC GIMMS NDVI3g version 1 1981-07-01 - 2015-12-31 1/12 x 1/12 degrees 1/24 a year.
    - Only reggrided data (compatible with ERA-INTERIM grid).
    - Methodology for anomalies decomposition.
    - Testing unit roots for all pixels in South America.


- [precipitation_trmm.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/precipitation_trmm.ipynb?flush_cache=true): 
    - Data from TRMM (TMPA) L3 Daily 0.25 x 0.25 degree (TRMM_3B42_Daily) 1998 - 2017.
    - Maps for monthly cumulative mean data.
    - Empirical orthogonal functions analysis.


- [surface_relative_humidity_era.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/surface_relative_humidity_era.ipynb?flush_cache=true): 
    - Data from ERA-INTERIM.
    - Trends of observed data.


- [total_column_water_vapour_era.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/total_column_water_vapour_era.ipynb?flush_cache=true): 
    - Data from ERA-INTERIM.
    - Trends of observed data.


- [total_precipitation_era.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/total_precipitation_era.ipynb?flush_cache=true): 
    - Monthly data from ERA-INTERIM.
    - Methodology for anomalies decomposition.
    - Testing unit roots for all pixels in South America.