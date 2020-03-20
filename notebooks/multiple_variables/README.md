# Description

## Overview

Exploring relations between climate and vegetation variables.

## Variables information

- See description of the ERA-INTERIM variables its [Parameter Database](https://apps.ecmwf.int/codes/grib/param-db).
 
| Variable | Units | Label | Parameter ID (ERAI) | Status |
| --- | --- | --- | --- | --- |
| Normalized difference vegetation index | [0.0, 1.0] | NDVI | - | **Target** |
| Soil moisture layer 1 (0-7 cm) | m3 / m3 | SWVL1 | [039](https://apps.ecmwf.int/codes/grib/param-db?id=39) | **Predictor** |
| Soil temperature layer 1 (0-7 cm) | K | STL1 | [139](https://apps.ecmwf.int/codes/grib/param-db?id=139) | **Predictor** |
| Total column water vapour | kg / m2 | TCWV | [137](https://apps.ecmwf.int/codes/grib/param-db?id=137) | **Predictor** |
| Water balance | m | WB | - | **Predictor** |
| Water deficit | m | WD | - | **Predictor** |
| Total precipitation | m | TP | [228](https://apps.ecmwf.int/codes/grib/param-db?id=228) | **Predictor** |
| Evaporation | m of water equivalent | E | [182](https://apps.ecmwf.int/codes/grib/param-db?id=182) | **Predictor** |
| Runoff | m | RO | [205](https://apps.ecmwf.int/codes/grib/param-db?id=205) | **Predictor** |
| Convective available potential energy | J / kg | CAPE | [59](https://apps.ecmwf.int/codes/grib/param-db?id=59) | **Predictor** |
| Surface relative humidity at 2 m | % | RELHUM | - | **Predictor** |
| Surface net solar radiation | J / m2 | SSR | [176](https://apps.ecmwf.int/codes/grib/param-db?id=176) | **Predictor** |
| Surface temperature at 2 m | K | T2M | [167](https://apps.ecmwf.int/codes/grib/param-db?id=167) | **Predictor** |
| Boundary layer height | m | BLH | [159](https://apps.ecmwf.int/codes/grib/param-db?id=159) | **Predictor** |
| Vertical integral of divergence of moisture flux | kg / m2 / s| VIWVD | [162084](https://apps.ecmwf.int/codes/grib/param-db?id=162084) | **Predictor** |
| Total cloud cover | [0.0, 1.0] | TCC | [164](https://apps.ecmwf.int/codes/grib/param-db?id=164) | **Predictor** |
| Wind speed at 10 m | m / s| SI10 | [207](https://apps.ecmwf.int/codes/grib/param-db?id=207) | **Predictor** |

## Better visualization


- [relations.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/relations.ipynb?flush_cache=true): 
    - Verbose mode. Sanity checks.
    - Variables are: `NDVI_mm`, `SWVL1_mm`, `STL1_mm`, `WB_mm`, `WD_mm`, `TP_mm`, `E_mm`, `RELHUM_mm`, `SSR_mm`, and `T2M_mm`.
    - `Linear Pearson correlation` between vegetation and climate variables with and without lags.
    - Lags are 1, 2, 3, and 6.
    - **Cautions** must be considered in analisys statistical of significance of Pearson correlation for climate data, see this reference: Bombardi, R. J. and Carvalho, L. M. V. d. (2017). Simple practices in climatological analyses: A review. Revista Brasileira de Meteorologia, 32(3):311–320.


- [relations2.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/relations2.ipynb?flush_cache=true): 
    - Variables are: `NDVI_mm`, `SWVL1_mm`, `STL1_mm`, `WB_mm`, `WD_mm`, `TP_mm`, `E_mm`, `RELHUM_mm`, `SSR_mm`, and `T2M_mm`.
    - `Spearman rank correlation` between vegetation and climate variables with and without lags.
    - Lags are 1, 2, 3, and 6.
    - Local analysis for Manaus.
        - Plot time series.
        - Autocorrelation.
        - Pair plots.


- [relations3.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/relations3.ipynb?flush_cache=true): 
    - Variables are: `NDVI_ano`, `SWVL1_ano`, `STL1_ano`, `WB_ano`, `WD_ano`, `TP_ano`, `E_ano`, `RELHUM_ano`, `SSR_ano`, and `T2M_ano`.
    - `Spearman rank correlation` between vegetation and climate variables with and without lags.
    - Lags are 1, 2, 3, and 6.
    - Local analysis for Manaus.
        - Plot time series.
        - Autocorrelation.
        - Pair plots.


- [relations4.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/relations4.ipynb?flush_cache=true): 
    - Variables are: `NDVI_mm`, `SWVL1_mm`, `STL1_mm`, `WB_mm`, `WD_mm`, `TP_mm`, `E_mm`, `RELHUM_mm`, `SSR_mm`, and `T2M_mm`.
    - `Spearman rank correlation` between vegetation and climate variables with and without lags.
    - Detrend and normalize data before calculating Spearman rank correlation.
    - Without lag.


- [relations5.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/relations5.ipynb?flush_cache=true): 
    - Variables are: `NDVI_mm`, `SWVL1_mm`, `STL1_mm`, `WB_mm`, `WD_mm`, `TP_mm`, `E_mm`, `RELHUM_mm`, `SSR_mm`, and `T2M_mm`.
    - `Mutual information` between vegetation and climate variables with and without lags.
    - Without lag.


- [relations6.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/relations6.ipynb?flush_cache=true).
    - Variables are vegetation (`NDVI_mm`) and climate (`SWVL1_mm`, `STL1_mm`, `WB_mm`, `WD_mm`, `TP_mm`, `E_mm`, `RELHUM_mm`, `SSR_mm`, and `T2M_mm`).
    - Principal Component Analysis for all South America grid points.
    - K-Means for the first principal component.


- [relations7.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/relations7.ipynb?flush_cache=true).
    - Variables are just for climate (`SWVL1_mm`, `STL1_mm`, `WB_mm`, `WD_mm`, `TP_mm`, `E_mm`, `RELHUM_mm`, `SSR_mm`, and `T2M_mm`).
    - Principal Component Analysis for all South America grid points.
    - K-Means for the first principal component.


- [surface_relative_humidity_mmeans.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/surface_relative_humidity_mmeans.ipynb?flush_cache=true).
    - Notebook intended to calculate monthly means of relative humidity at surface based on ERA-INTERIM datasets of temperature and dew point temperature both at surface (2 m above the ground).

    - **References**:
        - [ERA datasets: near-surface humidity](https://confluence.ecmwf.int/display/CKB/ERA+datasets%3A+near-surface+humidity).
        - [Calculate Temperature, Dewpoint, or Relative Humidity](http://andrew.rsmas.miami.edu/bmcnoldy/Humidity.html).
    - Based on Clausius-Clayperon equation:
        $$ 
        e_s(T) = 6.1094 \exp{\left( \frac{17.625 T}{T + 243.04} \right)}
        $$
        where $T$ is temperature in degree Celsius, you can calculate relative humidity $RH$ as the following:
        $$
        RH = \frac{e_s(T_d)}{e_s(T)} 100 \%
        $$
        where $T_d$ is the dew point temperature.


- [surface_relative_humidity.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/surface_relative_humidity.ipynb?flush_cache=true).
    - Notebook intended to calculate relative humidity at surface based on ERA-INTERIM datasets of temperature and dew point temperature both at surface (2 m above the ground).
    - **References**:
        - [ERA datasets: near-surface humidity](https://confluence.ecmwf.int/display/CKB/ERA+datasets%3A+near-surface+humidity).
        - [Calculate Temperature, Dewpoint, or Relative Humidity](http://andrew.rsmas.miami.edu/bmcnoldy/Humidity.html).
    - Based on Clausius-Clayperon equation:
        $$ 
        e_s(T) = 6.1094 \exp{\left( \frac{17.625 T}{T + 243.04} \right)}
        $$
        where $T$ is temperature in degree Celsius, you can calculate relative humidity $RH$ as the following:
        $$
        RH = \frac{e_s(T_d)}{e_s(T)} 100 \%
        $$
        where $T_d$ is the dew point temperature.


- [water_budget.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/water_budget.ipynb?flush_cache=true)
    - This notebook is intended for constructing water balance (monthly and daily) and cumulative water deficit (monthly) datasets.