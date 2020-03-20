# Description

Trajectories in South America.

## Better visualizations


- [get_data_along.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/trajectories/get_data_along.ipynb?flush_cache=true):
    - Data from ERA-INTERIM and from GIMMS.
    - Specific humidity and moisture flux.
    - Single and multiple trajectories using `cdlearn.trajectories.StaticTrajectory` class.
    - Get observed NDVI data along a single trajectory.


- [get_data_along2.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/trajectories/get_data_along2.ipynb?flush_cache=true):
    - Data from ERA-INTERIM and from GIMMS.
    - Specific humidity and moisture flux.
    - Multiple trajectories using `cdlearn.trajectories.StaticTrajectory` class. All of them begin at the same initial position.
    - Get observed data of water vapour content, NDVI, total precipitation, evaporation along all trajectories.
    - Save these trajectories inside individual `.csv` files (**time consuming operation**).


- [get_data_along3.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/trajectories/get_data_along3.ipynb?flush_cache=true):
    - Data from ERA-INTERIM.
    - Specific humidity and moisture flux.
    - Climatological mean trajectories using `cdlearn.trajectories.StaticTrajectory` class.
    - Get climatological mean of observed data of water vapour content, NDVI, total precipitation, evaporation along all trajectories.
    - Moisture flux equations here in this notebook.