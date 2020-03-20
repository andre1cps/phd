# Description

Trajectories in South America.

## Better visualizations.


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
    - The water vapor content $w$ is the vertically integrated water vapor depth (precipitable water) represented by the vertical integral of specific humidity $q(p)$ from the surface to an elevation where pressure $p$ vanish, as follows:
$$
w = \frac{1}{\rho_L g} \int_{p_0}^{0} q(p) dp
$$
where $\rho_L$ is the liquid water density and $g$ is the acceleration due to gravity. The velocity $\pmb{V} = (u, v)$ is defined through the vertically integrated water vapor flux $\pmb{F} = (F_x, F_y)$, as follows:
$$
u = \frac{F_x}{w}; \hspace{1cm} v = \frac{F_y}{w}
$$
and:
$$
F_x = \frac{1}{\rho_L g} \int_{p_0}^{0} q(p) \hat{u}(p) dp ; \hspace{1cm}
F_y = \frac{1}{\rho_L g} \int_{p_0}^{0} q(p) \hat{v}(p) dp
$$
where $\hat{u}(p)$ and $\hat{v}(p)$ are the wind components in the $x$ and $y$
directions, respectively.