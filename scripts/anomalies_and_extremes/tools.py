"""
===============================================================================
Tools

Auxiliar functions for climatologies calculations.
===============================================================================
"""

# Load packages.
import numpy as np
import xarray as xr

# Functions.
###############################################################################
def linear_trends(data_array):
    """
    Calculate linear trends and its coefficients for data at each location.

    Arguments:
    ----------
    data_array : xarray DataArray object
        Observed data.

    Returns:
    -------
    trends : xarray DataArray object
        Linear trends.
    coefficients : xarray DataArray object
        Angular and linear coefficients.        
    """
        
    # Just guarantee that time is the first dimension.
    data_array = data_array.transpose("time", "latitude", "longitude")
    
    # Just guarantee that time is ordered.
    data_array = data_array.sortby("time")

    # New dimensions. Exclude "time" and insert "coefficients".
    dims = list(data_array.dims)
    dims.remove("time")
    dims = ["coefficients"] + dims
    
    # Extract data as numpy arrays.
    y = data_array.values
    shape = y.shape
    x = np.arange(shape[0])
    y = y.reshape((shape[0], -1))
    
    # Linear fits.   
    parameters = np.polyfit(x, y, deg=1)
            
    # Coefficients as xarray DataArray object.
    coefficients = xr.DataArray(data=parameters.reshape((2, *shape[1:])),
                                dims=dims,
                                coords={"coefficients": ["angular", "linear"], 
                                        "latitude": data_array.latitude,
                                        "longitude": data_array.longitude})
    
    # Loop over all fits (locations).
    trends = np.zeros_like(y)
    for i in range(parameters.shape[1]):
        p = parameters[:, i]
        function = np.poly1d(p)
        trends[:, i] = function(x)
           
    # The same shape as the original data.
    trends = trends.reshape(*shape)
        
    # Results as xarray DataArray object.
    trends = xr.DataArray(data=trends, 
                          dims=data_array.dims, 
                          coords=data_array.coords)
    
    return trends, coefficients
                           
###############################################################################
def linear_detrend(data_array):
    """
    This function makes a linear detrend of data for each location.
    
    Arguments:
    ----------
    data_array : xarray DataArray object
        Observed data.

    Returns:
    -------
    detrended : xarray DataArray object
        Linearly detrended data.
    """
    
    # Subtract linear fit from observed data.
    trends, _ = linear_trends(data_array)
    detrended = data_array - trends
    
    return detrended      
        
###############################################################################
def climatology(data_array):
    """
    Calculate monthly climatology from linearly detrended data.
    
    Arguments:
    ----------
    data_array : xarray DataArray object
        Observed data.

    Returns:
    -------
    seasonal : xarray DataArray object
        Monthly means from detrended data.
    """
    
    # Input for grouping.
    detrended = linear_detrend(data_array)
    
    # Group data. This object has only twelve time values.
    grouped = detrended.groupby("time.month").mean("time")
    
    # Initialize results.
    seasonal = xr.DataArray(np.zeros_like(data_array),
                            dims=data_array.dims,
                            coords=data_array.coords)
    
    # Filling results.
    for month in range(1, 13):
        seasonal.loc[seasonal.time.dt.month == month] = \
        grouped.loc[grouped.month == month]
        
    return seasonal

###############################################################################
def anomalies(data_array):
    """
    Calculate anomalies as proposed by Christina Papagiannopoulou et al.
    
    Arguments:
    ----------
    data_array : xarray DataArray object
        Observed data.

    Returns:
    -------
    residuals : xarray DataArray object
        Monthly means of detrended data subtracted from detrended observed 
        data.
    
    References:
    -----------
    [1] Papagiannopoulou, C.et al. 2017. A non-linear Granger-causality 
        framework to investigate climate—vegetation dynamics.Geosci. Model
        Dev.10:1945–1960.     
    """
    
    detrended = linear_detrend(data_array)
    seasonal = climatology(detrended)
    residuals = detrended - seasonal
    
    return residuals

###############################################################################
def daily_detrended_climatologies(data_array):
    """
    Calculate daily anomalies from daily data. First, this function detrends 
    observed daily data. Then, typical values for each day of year are 
    calculated, resulting in 366 values. After that, these typycal values are 
    subtracted of the respective detrended daily data, resulting in daily 
    climatology for detrended data.
    
    Arguments:
    ----------
    data_array : xarray DataArray object
        Observed daily data, not detrended.
    
    Returns:
    --------
    residuals : xarray DataArray object
        Daily climatologies of daily detrended data.
    """
    
    # Detrend daily data.
    detrended = linear_detrend(data_array)
    
    # Subtract each daily data value by the respective daily mean.
    grouped = detrended.groupby("time.dayofyear")
    seasonal = grouped.mean("time")
    residuals = grouped - seasonal
    
    return residuals
